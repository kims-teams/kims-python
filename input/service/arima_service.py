import os
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_function(data, steps=12):
    data.columns = ["date", "sales_volume"]
    data["date"] = pd.to_datetime(data["date"], format="%Y.%m")
    data = data.set_index("date")
    ts = data["sales_volume"].astype(float)

    model = ARIMA(ts, order=(1, 1, 1))
    fit = model.fit()
    forecast = fit.forecast(steps=steps)

    last_date = ts.index[-1]
    forecast_index = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=steps, freq="MS")
    forecast = pd.Series(forecast.values, index=forecast_index)

    df_actual = pd.DataFrame({'date': ts.index.astype(str), 'value': ts.values, 'type': 'actual'})
    df_pred = pd.DataFrame({'date': forecast.index.astype(str), 'value': forecast.values, 'type': 'forecast'})

    result = pd.concat([df_actual, df_pred], ignore_index=True)
    result = result.replace({pd.NA: None, pd.NaT: None, float('nan'): None})
    result = result.where(pd.notnull(result), None)

    return result
