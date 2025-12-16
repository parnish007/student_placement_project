import pickle
import pandas as pd

# Load the trained pipeline
with open('model/student_placement_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

def predict_student(data: dict) -> dict:
    """
    Accepts a dictionary of student features and returns prediction and probability.
    """
    # Convert input dict to DataFrame
    input_df = pd.DataFrame([data])

    # Ensure categorical column is string
    input_df['Internship_Experience'] = input_df['Internship_Experience'].astype(str)

    # Make prediction
    prediction = model_pipeline.predict(input_df)[0]

    # Optional: get probability if available
    probability = None
    if hasattr(model_pipeline.named_steps['model'], "predict_proba"):
        probability = model_pipeline.predict_proba(input_df)[0]

    # Return dictionary
    return {
        "prediction": prediction,      # "Yes" or "No"
        "probability": probability     # array: [Not Placed, Placed]
    }
