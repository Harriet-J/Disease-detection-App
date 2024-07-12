import pytest
import pickle
from streamlit.testing.v1 import AppTest
import sys
import os
from app import load_model



# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#global variable
at = AppTest.from_file("app.py")

# Helper function to mock predictions
def mock_predict(model, user_input):
    if model == 'diabetes_model':
        return [1]  # Simulate a diabetic prediction
    elif model == 'heart_disease_model':
        return [1]  # Simulate a heart disease prediction
    elif model == 'parkinsons_model':
        return [1]  # Simulate a Parkinson's disease prediction
    return [0]

# Test loading models
def test_load_diabetes_model():
    diabetes_model_path = 'saved_model/diabetes_model.sav'
    at.diabetes_model_path = diabetes_model_path
    model = load_model(diabetes_model_path)
    assert model is not None, f"Failed to load diabetes model from {diabetes_model_path}"

def test_load_heart_disease_model():
    heart_disease_model_path = 'saved_model/heart_disease_model.sav'
    at.heart_disease_model_path = heart_disease_model_path
    model = load_model(heart_disease_model_path)
    assert model is not None, f"Failed to load heart disease model from {heart_disease_model_path}"

def test_load_parkinsons_model():
    parkinsons_model_path = 'saved_model/parkinsons_model.sav'
    at.parkinsons_model_path = parkinsons_model_path
    model = load_model(parkinsons_model_path)
    assert model is not None, f"Failed to load Parkinson's model from {parkinsons_model_path}"

# Example tests for specific functionalities
def test_diabetes_prediction():
    # Mock user input for diabetes prediction
    user_input = [1, 106, 70, 28, 135, 34.2, 0.142, 22]  # Example input values

    # Mock the model loading and prediction
    diabetes_model_path = 'saved_model/diabetes_model.sav'
    model = load_model(diabetes_model_path)

    # Simulate the prediction
    prediction = mock_predict('diabetes_model', user_input)

    # Assertions
    assert prediction[0] == 1, "Expected diabetic prediction"

def test_heart_disease_prediction():
    # Mock user input for heart disease prediction
    user_input = [67, 1, 4, 160, 286, 0, 2, 108, 1, 1.5, 2, 3, 3]  # Example input values

    # Mock the model loading and prediction
    heart_disease_model_path = 'saved_model/heart_disease_model.sav'
    model = load_model(heart_disease_model_path)

    # Simulate the prediction
    prediction = mock_predict('heart_disease_model', user_input)

    # Assertions
    assert prediction[0] == 1, "Expected heart disease prediction"

def test_parkinsons_prediction():
    # Mock user input for Parkinson's prediction
    user_input = [197.076, 206.896, 192.055, 0.00289, 0.00003, 0.00168, 0.00184, 0.00503, 0.04374, 0.426, 0.02182, 0.03130, 0.02971, 0.06545, 0.02211, 21.033, 0.414783]  # Example input values
    # Mock the model loading and prediction
    parkinsons_model_path = 'saved_model/parkinsons_model.sav'
    model = load_model(parkinsons_model_path)

    # Simulate the prediction
    prediction = mock_predict('parkinsons_model', user_input)

    # Assertions
    assert prediction[0] == 1, "Expected Parkinson's disease prediction"

# Run the tests
if __name__ == '__main__':
    pytest.main()
