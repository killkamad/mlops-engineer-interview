import os

import joblib


def prepare_joblib_model():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    joblib_model_path = os.path.join(parent_directory, 'joblib_models', 'model.joblib')
    model = joblib.load(joblib_model_path)
    return model
