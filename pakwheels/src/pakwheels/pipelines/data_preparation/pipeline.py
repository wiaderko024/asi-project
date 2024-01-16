"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node
from .nodes import clean_data
def create_pipeline(**kwargs) -> Pipeline: return pipeline([
node(
                func=clean_data,
                inputs=["data1"],
                outputs="cleaned_data",
                name="clean_dataset_node"
) ])
