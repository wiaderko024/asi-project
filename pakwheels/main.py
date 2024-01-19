import os
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax

app = FastAPI()


class PredictionInput(BaseModel):
    year: int
    assembly: str
    body: str
    make: str
    city: str
    color: str
    registered: str
    model: str
    engine: float
    transmission: str
    fuel: str
    mileage: float


@app.post("/run_prediction")
def run_prediction(prediction_data: PredictionInput):
    model_path = "data/07_model_output/linear_regression_model.joblib"

    if os.path.exists(model_path):
        with open(model_path, "rb") as generated_model:
            model: LinearRegression = joblib.load(generated_model)
    else:
        return {"error": "Model not found"}

    input_df = pd.DataFrame([prediction_data.model_dump(exclude_unset=True)])

    input_df["engine"] = np.log1p(input_df["engine"])

    if "mileage" in input_df.columns and len(input_df["mileage"].unique()) > 1:
        input_df["mileage"] = boxcox1p(
            input_df["mileage"], boxcox_normmax(input_df["mileage"] + 1)
        )

    # FIXME: fucks up the code
    cat_cols = ["assembly", "transmission", "fuel"]
    input_df = pd.get_dummies(input_df, columns=cat_cols, drop_first=True)

    scalar = RobustScaler()
    scaled_input = scalar.fit_transform(input_df)

    predictions = model.predict(scaled_input)

    predictions_list = predictions.tolist()

    return {"result": {"model_predictions": predictions_list}}
