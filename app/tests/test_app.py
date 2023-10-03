from fastapi.testclient import TestClient
from app.main import app
from app import TEST_SAMPLE_1, TEST_SAMPLE_2
client = TestClient(app)


def test_predict_model():
    json_data = {
        "data": [
            TEST_SAMPLE_1,
            TEST_SAMPLE_2
        ]
    }
    response = client.post("/model-predict/", json=json_data)
    assert response.status_code == 200
    assert response.json() == {'result': [237.2720892643453, 81.60671354729905]}
