# ASI-PROJECT

## Pakwheels used car price prediction

### How to run project?

At first create virtual environment and run it.

```shell
python3 -m venv venv
source venv/bin/activate
```

Then install all the dependencies from requirements.txt file.

```shell
pip install --upgrade pip
pip install -r pakwheels/src/requirements.txt
pip install "kedro[pandas]"
```

Now you can run the pipeline using following command.
```shell
cd pakwheels
kedro run
```

To run API execute following command in pakwheels directory.

```shell
uvicorn main:app --reload
```

Done. Project should be run.

### How to predict price?

You should have an API client on your machine like insomnia or postman. Send request with POST method 
at http://127.0.0.1:8000/run_prediction endpoint. The body of the request should look like below. 

```json
{
  "city": "Lahore",
  "assembly": "Local",
  "body": "Sedan",
  "make": "Toyota",
  "model": "Corolla",
  "year": 2020,
  "engine": 2000,
  "transmission": "Automatic",
  "fuel": "Petrol",
  "color": "White",
  "registered": "Punjab",
  "mileage": 80000
}
```
