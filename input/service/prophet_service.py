import os
import pandas as pd
from prophet import Prophet
import numpy as np

def prophet_function(excel_path=None, steps=12):
    if excel_path is None:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, "data", "monthly_sales_volume.xlsx")

    ext = os.path.splitext(file_path)[-1].lower()
    if ext in [".xls", ".xlsx"]:
        data = pd.read_excel(file_path, dtype={"시점": "str"})
    elif ext == ".csv":
        data = pd.read_csv(file_path, dtype={"시점": "str"})
    else:
        raise ValueError("지원하지 않는 파일 형식입니다.")

    data = pd.read_excel(excel_path, dtype={"시점": "str"})   # ← 수정!

    data.columns = ["ds", "y"]
    data["ds"] = pd.to_datetime(data["ds"], format="%Y.%m")

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=steps, freq='MS')
    forecast = model.predict(future)

    df_actual = pd.DataFrame({
        "date": data["ds"].astype(str),
        "value": data["y"].astype(float),
        "type": "actual"
    })

    df_pred = pd.DataFrame({
        "date": forecast["ds"].astype(str).tail(steps),
        "value": forecast["yhat"].tail(steps),
        "yhat_lower": forecast["yhat_lower"].tail(steps),
        "yhat_upper": forecast["yhat_upper"].tail(steps),
        "type": "forecast"
    })

    result = pd.concat([df_actual, df_pred], ignore_index=True)
    result = result.replace({np.nan: None})
    records = result.to_dict(orient="records")
    print(records)
    return records
