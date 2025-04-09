import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler  # Import StandardScaler
import numpy as np


# 1. Load the Model and Scaler
try:
    model = joblib.load('model.pkl')
    scaler = joblib.load('scaler.pkl')  # Load the scaler as well.  Crucial!
except Exception as e:
    st.error(
        f"Error: Unable to load the model or scaler. Please check the file path and ensure the files exist. Error details: {e}")
    st.stop()

# 2. Define the Input Features and their Scales (Corrected Ranges)
input_features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
feature_ranges = {  # Use the correct ranges from your training data
    "sepal_length": (4.3, 7.9),
    "sepal_width": (2.0, 4.4),
    "petal_length": (1.0, 6.9),
    "petal_width": (0.1, 2.5)
}

# 3. Create the Streamlit App
st.title('Iris Species Prediction')

# 4. Input Fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=feature_ranges["sepal_length"][0],
                            max_value=feature_ranges["sepal_length"][1], step=0.01)
sepal_width = st.number_input("Sepal Width (cm)", min_value=feature_ranges["sepal_width"][0],
                           max_value=feature_ranges["sepal_width"][1], step=0.01)
petal_length = st.number_input("Petal Length (cm)", min_value=feature_ranges["petal_length"][0],
                            max_value=feature_ranges["petal_length"][1], step=0.01)
petal_width = st.number_input("Petal Width (cm)", min_value=feature_ranges["petal_width"][0],
                           max_value=feature_ranges["petal_width"][1], step=0.01)



# 6. Prepare Input Data
input_data = pd.DataFrame({
    "sepal_length": [sepal_length],
    "sepal_width": [sepal_width],
    "petal_length": [petal_length],
    "petal_width": [petal_width],
})

# 7. Make Prediction
if st.button('Predict Species'):
    try:
        # 7.1 Scale the input data using the loaded scaler
        scaled_input_data = scaler.transform(input_data)  # Use .transform, not .fit_transform

        # 7.2 Make the prediction
        prediction = model.predict(scaled_input_data)
        predicted_species_index = prediction[0]  # Get the index (0, 1, or 2)

        # 7.3 Map the numerical prediction to a species name
        species_names = {
            0: "Iris Setosa",
            1: "Iris Versicolor",
            2: "Iris Virginica"
        }
        predicted_species_name = species_names.get(predicted_species_index, "Unknown Species")  #handles the default

        # 7.4 Display the result
        st.success(f"Predicted Species: {predicted_species_name}")

    except Exception as e:
        st.error(f"Error making prediction: {e}")

# 8. Important Considerations
st.markdown("""
**Important Considerations:**

* **Model Accuracy:** The accuracy of this prediction depends entirely on the quality of the trained machine learning model. A poorly trained model will produce unreliable results.
* **Feature Scaling:** The input values are scaled using the `StandardScaler` that was used during training.  It is **CRUCIAL** that you load and use the same scaler.  If the scaling is not consistent, the predictions will be incorrect.
* **Data Range:** The input values should fall within a reasonable range, similar to the data the model was trained on. Extrapolation (predicting outside the trained range) can lead to inaccurate predictions.
* **Model File:** The `model.pkl` file MUST be present in the correct location for this app to function.  Double-check the filename.
* **Scaler File:** A `scaler.pkl` file (or similar, depending on how you saved your scaler) MUST also be present.  This file contains the scaling parameters (mean, standard deviation) learned during training.
* **Dependencies:** This app requires the `streamlit`, `pandas`, `joblib`, and `scikit-learn` libraries.  Make sure these are installed (`pip install streamlit pandas joblib scikit-learn`).
* **Error Handling:** The code includes basic error handling for model loading and prediction.
* **Input Data:** The application expects four numerical inputs: sepal length, sepal width, petal length, and petal width, in centimeters.  It's crucial that the model you loaded was trained with data in this format and order.
* **Output Interpretation:** The model predicts a numerical value (0, 1, or 2), which is then mapped to the corresponding Iris species name.
""")
