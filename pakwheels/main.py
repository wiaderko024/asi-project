from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner
from src.pakwheels.pipelines.data_preparation.pipeline import create_pipeline

app = FastAPI()


class PipelineInput(BaseModel):
    input_value: int


@app.get("/pakwheels")
def run_pipeline(input: PipelineInput = None):
    input = PipelineInput(input_value=10)
    # Create the pipeline
    pipeline = create_pipeline()

    # Set up a DataCatalog to load the dataset
    io = DataCatalog({"data1": MemoryDataset()})

    # Assuming `data1` is the dataset you want to pass to the pipeline
    data1 = io.load("data1")

    # Run the pipeline and get the result
    result = SequentialRunner().run(pipeline, catalog={"data1": data1})

    return {"result": result}


@app.get("/test")
def test():
    return {"result": {"test": "success"}}
