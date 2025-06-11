import json
import importlib
import pkgutil
import inspect
from pathlib import Path
from pydantic import BaseModel


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
