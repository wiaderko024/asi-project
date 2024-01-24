"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs=["cleaned_data"],
                outputs="trained_model",
                name="train_model_node",
            )
        ]
    )
