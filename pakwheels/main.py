from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import joblib

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
    pipeline = "data/07_model_output/prediction_ready_model.joblib"

    pipeline = joblib.load(pipeline)

    prediction_df = pd.DataFrame([prediction_data.model_dump()])
    predictions = pipeline.predict(prediction_df)

    predictions_list = predictions.tolist()

    return {
        "result": {
            "price_prediction": {
                prediction_data.make: {
                    prediction_data.model: {
                        "rupees": predictions_list[0],
                        "dollars": predictions_list[0] * 0.0067,
                        "zlotys": predictions_list[0] * 0.026,
                    }
                }
            }
        }
    }
