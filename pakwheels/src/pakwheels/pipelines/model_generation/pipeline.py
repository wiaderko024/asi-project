"""
This is a boilerplate pipeline 'model_generation'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import generate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_model,
                inputs=["cleaned_data"],
                outputs="generated_model",
                name="generate_model_node",
            )
        ]
    )
