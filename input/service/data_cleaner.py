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

# 3. 정제 로직
def process_input_data(input_data: dict) -> dict:
    try:
        for key, value in input_data.items():
            dto_class = DTO_MAP.get(key.lower())
            if not dto_class:
                return {"error": f"지원하지 않는 DTO 유형: {key}"}

            dto_instance: BaseModel = dto_class(**value)
            return dto_instance.dict(exclude_none=True)

        return {"error": "데이터가 비어 있음"}

    except Exception as e:
        return {"error": str(e)}

# 4. JSON 변환
def get_json_result(input_data: dict) -> str:
    result = process_input_data(input_data)
    return json.dumps(result, ensure_ascii=False, indent=2)



# 업로드된 df 정제 처리
def clean_uploaded_dataframe(entity: str, df: pd.DataFrame) -> dict:
    try:
        dto_key = entity.lower()
        dto_class = DTO_MAP.get(dto_key)
        if not dto_class:
            return {'error': f'지원하지 않는 entity(DTO): {entity}'}

        # 결측치 처리
        df = df.where(pd.notnull(df), None)

        cleaned_data = []
        cleaned_columns = set()

        for row in df.to_dict(orient='records'):

            row = {k: (None if pd.isna(v) else v) for k, v in row.items()}

            try:
                dto_instance = dto_class(**row)
                filtered = dto_instance.dict(exclude_none=True)
                camel_dict = {to_camel_case(k): v for k, v in filtered.items()}
                cleaned_data.append(camel_dict)
                cleaned_columns.update(camel_dict.keys())
            except Exception as e:
                return {'error': f'DTO 변환 실패: {str(e)}'}

        return {
            'entity': entity,
            'columns': sorted(cleaned_columns),
            'data': cleaned_data
        }

    except Exception as e:
        return {'error': str(e)}
