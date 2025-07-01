import os
import pandas as pd
from prophet import Prophet
import math
import numpy as np

def nan_to_none(x):
    return None if isinstance(x, float) and math.isnan(x) else x


def prophet_function(csv_path=None, steps=12):

    if csv_path is None:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(BASE_DIR, "data", "monthly_sales_volume.csv")

    data = pd.read_csv(csv_path, dtype={"시점": "str"})
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
    return result
