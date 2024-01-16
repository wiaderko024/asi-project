from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kedro.io import DataCatalog, MemoryDataset
from kedro.runner import SequentialRunner
from src.pakwheels.pipelines.data_preparation.pipeline import create_pipeline

app = FastAPI()

class PipelineInput(BaseModel):
    input_value: int

@app.post("/pipline")
def run_pipeline(input: PipelineInput):
    # Create the pipeline
    pipeline = create_pipeline()

    # Set up the DataCatalog with the input value from the request
    io = DataCatalog({"input_value": MemoryDataset()})
    io.save("input_value", input.input_value)

    # Run the pipeline and get the result
    result = SequentialRunner().run(pipeline, catalog=io)
    
    return {"result": result}
