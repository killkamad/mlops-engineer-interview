from fastapi import FastAPI
from numpy import array

from app.models.ml_input import MLInput, MLResponse
from app.utils.prepare import prepare_joblib_model


app = FastAPI(
    title='ML test task',
    version='1.0'
)

model = prepare_joblib_model()


@app.post('/model-predict/', response_description="Predict Data", response_model=MLResponse)
async def predict_model(data_set: MLInput):
    test_data = array(data_set.data)
    predicted_output = model.predict(test_data)
    response = MLResponse()
    response.result = predicted_output.tolist()
    return response
