import streamlit as st
import joblib
import numpy as np

# Load the Trained Model and Scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function Which Predicts if a Heart Disease is Present
def predictHeartDisease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # Reshape Input Data for the Prediction
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)

    # Indices of Numeric Features which are age, trestbps, chol, thalach and oldpeak
    numeric_indices = [0, 3, 4, 7, 9]  
    # Apply Scaling to Numeric Features
    input_data[:, numeric_indices] = scaler.transform(input_data[:, numeric_indices])

    # Predict if a Heart Disease is Present
    prediction = model.predict(input_data)

    # Returns 1 if there is No Heart Disease Present or 0 If there is a Heart Disease Present
    return int(prediction[0])

# Web Layour using Streamlit
def main():
    st.title("Heart Disease Prediction Application")
    st.write("Enter the Patient's Details Below to Predict if a Heart Disease is Present")

    # Input Fields
    age = st.slider("Age", 20, 100)
    sex = st.radio("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", 90, 200)
    chol = st.slider("Cholesterol (mg/dl)", 100, 600)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Probable or definite left ventricular hypertrophy"])
    thalach = st.slider("Maximum Heart Rate Achieved", 60, 220)
    exang = st.radio("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.slider("ST Depression Induced by Exercise", 0.0, 6.2)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.slider("Number of Major Vessels Colored by Flourosopy", 0, 4)
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Converts Categorical Inputs to Numerical Inputs
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0
    cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
    restecg = ["Normal", "ST-T wave abnormality", "Probable or definite left ventricular hypertrophy"].index(restecg)
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

    # Predict if a Heart Disease is Present
    if st.button("Predict"):
        prediction = predictHeartDisease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        if prediction == 1:
            st.success("The patient is unlikely to have heart disease.")
        else:
            st.error("The patient is likely to have heart disease. Please refer the patient for further tests or treatment.")

if __name__ == "__main__":
    main()