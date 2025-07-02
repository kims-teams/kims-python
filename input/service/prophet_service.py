import pandas as pd
from prophet import Prophet
import numpy as np

def prophet_function(data, steps=12):
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
    result = result.replace({np.nan: None, pd.NA: None, pd.NaT: None, float('nan'): None})
    result = result.where(pd.notnull(result), None)
    return result.to_dict(orient="records")
