from sklearn.pipeline import Pipeline
import joblib


def generate_model(pipeline: Pipeline):
    joblib.dump(pipeline, "data/07_model_output/prediction_ready_model.joblib")

    return pipeline
