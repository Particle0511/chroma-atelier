import os
import joblib
import pytest
import numpy as np
from ml_engine.config import MODEL_PATH

def test_model_exists():
    assert os.path.exists(MODEL_PATH)

def test_prediction_shape():
    model = joblib.load(MODEL_PATH)
    test_input = ["ocean blue"]
    prediction = model.predict(test_input)
    
    assert prediction.shape == (1, 15)

def test_prediction_values():
    model = joblib.load(MODEL_PATH)
    prediction = model.predict(["test"])[0]
    
    assert np.all(prediction >= -50) 
    assert np.all(prediction <= 305)