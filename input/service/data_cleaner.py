import json
import importlib
import pkgutil
import inspect
from pathlib import Path
from pydantic import BaseModel
import pandas as pd



def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])



# 1. DTO 자동 로딩
def load_all_dtos_from_package(package_name: str):
    dto_map = {}
    package = importlib.import_module(package_name)
    package_path = Path(package.__file__).parent

    for _, module_name, _ in pkgutil.iter_modules([str(package_path)]):
        full_module_name = f"{package_name}.{module_name}"
        module = importlib.import_module(full_module_name)

        # 클래스만 찾아서 map에 넣기
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseModel) and obj.__module__ == full_module_name:
                key = module_name.replace('_dto', '').lower()
                dto_map[key] = obj

    return dto_map

# 2. 자동 DTO 매핑
DTO_MAP = load_all_dtos_from_package("input.dto")




# 업로드된 df 정제 처리
def clean_uploaded_dataframe(entity: str, df: pd.DataFrame) -> dict:
    try:
        dto_key = entity.lower()
        dto_class = DTO_MAP.get(dto_key)
        if not dto_class:
            return {'error': f'지원하지 않는 entity(DTO): {entity}'}

        print(f"✅ 로딩된 DTO 클래스: {dto_class.__name__}")

        # 결측치 처리
        df = df.where(pd.notnull(df), None)

        cleaned_data = []
        cleaned_columns = set()

        for idx, row in enumerate(df.to_dict(orient='records')):
            row = {k: (None if pd.isna(v) else v) for k, v in row.items()}

            try:
                dto_instance = dto_class(**row)
                filtered = dto_instance.dict(exclude_none=True)
                camel_dict = {to_camel_case(k): v for k, v in filtered.items()}
                cleaned_data.append(camel_dict)
                cleaned_columns.update(camel_dict.keys())
            except Exception as e:
                print("❌ DTO 변환 실패!")
                print(f"👉 실패한 행 index: {idx}")
                print(f"👉 데이터: {json.dumps(row, ensure_ascii=False)}")
                print(f"👉 에러 내용: {str(e)}")
                return {'error': f'DTO 변환 실패: {str(e)}'}

        return {
            'entity': entity,
            'columns': sorted(cleaned_columns),
            'data': cleaned_data
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {'error': str(e)}