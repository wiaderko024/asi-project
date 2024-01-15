"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.14
"""
from kedro.pipeline import Pipeline, pipeline, node from .nodes import merge_datasets, clean_data, generate_datetime_features
def create_pipeline(**kwargs) -> Pipeline: return pipeline([
node(
                func=clean_data,
                inputs=["data1"],
                outputs="cleaned_data",
                name="clean_dataset_node"
) ])
