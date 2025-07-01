import os
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_function(file_path=None, steps=12):
    if file_path is None:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, "data", "monthly_sales_volume.xlsx")

    ext = os.path.splitext(file_path)[-1].lower()
    if ext in [".xls", ".xlsx"]:
        data = pd.read_excel(file_path, dtype={"시점": "str"})
    elif ext == ".csv":
        data = pd.read_csv(file_path, dtype={"시점": "str"})
    else:
        raise ValueError("지원하지 않는 파일 형식입니다.")

    data.columns = ["date", "sales_volume"]
    data["date"] = pd.to_datetime(data["date"], format="%Y.%m")
    data = data.set_index("date")
    ts = data["sales_volume"].astype(float)
    model = ARIMA(ts, order=(1,1,1))
    fit = model.fit()
    forecast = fit.forecast(steps=steps)
    last_date = ts.index[-1]
    forecast_index = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=steps, freq='MS')
    forecast = pd.Series(forecast.values, index=forecast_index)

    df_actual = pd.DataFrame({'date': ts.index.astype(str), 'value': ts.values, 'type': 'actual'})
    df_pred = pd.DataFrame({'date': forecast.index.astype(str), 'value': forecast.values, 'type': 'forecast'})

    result = pd.concat([df_actual, df_pred], ignore_index=True)
    # NaN → None 변환
    result = result.replace({pd.NA: None, pd.NaT: None, float('nan'): None})
    result = result.where(pd.notnull(result), None)

    return result
