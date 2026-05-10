import streamlit as st
import numpy as np
import pickle

# Load Trained Logistic Regression Model
model = pickle.load(
    open('ML_model/logisticReg_model.pickle', 'rb')
)

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Diabetes Prediction and Clinical Risk Analysis System")

st.markdown("""
This intelligent clinical support system predicts the likelihood of diabetes based on patient clinical parameters using Logistic Regression model.

---

## Input Guidelines

### Binary Inputs
Enter values according to the following criteria:

| Parameter | Value = 1 | Value = 0 |
|---|---|---|
| Gender | Female | Male |
| Obesity | Obese | Not Obese |
| Hypertension | Present | Absent |
| Blood Pressure | High | Normal |
| Smoker | Smoker | Non-Smoker |
| Cholesterol | High | Normal |
| Angina | Present | Absent |

---
""")

st.header("Enter Patient Clinical Details")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

gender = st.selectbox(
    "Gender",
    [0, 1],
    help="0 = Male, 1 = Female"
)

obesity = st.selectbox(
    "Obesity",
    [0, 1],
    help="0 = Not Obese, 1 = Obese"
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1],
    help="0 = No, 1 = Yes"
)

blood_pressure = st.selectbox(
    "Blood Pressure",
    [0, 1],
    help="0 = Normal, 1 = High"
)

smoker = st.selectbox(
    "Smoker",
    [0, 1],
    help="0 = Non-Smoker, 1 = Smoker"
)

cholesterol = st.selectbox(
    "Cholesterol",
    [0, 1],
    help="0 = Normal, 1 = High"
)

angina = st.selectbox(
    "Angina",
    [0, 1],
    help="0 = No, 1 = Yes"
)

fbs = st.number_input(
    "Fasting Blood Sugar (FBS)",
    min_value=0.0,
    max_value=500.0,
    value=90.0
)

hemoglobin = st.number_input(
    "Hemoglobin",
    min_value=0.0,
    max_value=25.0,
    value=13.0
)

if st.button("Predict Diabetes Risk"):

    features = np.array([[
        age,
        gender,
        obesity,
        hypertension,
        blood_pressure,
        smoker,
        cholesterol,
        angina,
        fbs,
        hemoglobin
    ]])

    prediction = model.predict(features)

    risk_factors = []

    if obesity == 1:
        risk_factors.append("Obesity")

    if hypertension == 1:
        risk_factors.append("Hypertension")

    if blood_pressure == 1:
        risk_factors.append("High Blood Pressure")

    if smoker == 1:
        risk_factors.append("Smoking Habit")

    if cholesterol == 1:
        risk_factors.append("High Cholesterol")

    if angina == 1:
        risk_factors.append("Angina")


    if fbs > 120:
        risk_factors.append("Elevated Fasting Blood Sugar")

    if hemoglobin < 12:
        risk_factors.append("Low Hemoglobin")


    if prediction[0] == 0:

        st.error(
            "The patient is likely to have diabetes."
        )

        st.markdown("""
### Clinical Risk Analysis

The prediction indicates that the patient may be at a higher risk of diabetes based on the entered clinical parameters.
""")

        if len(risk_factors) > 0:

            st.warning("### Major Contributing Risk Factors")

            for factor in risk_factors:
                st.write(f"• {factor}")

        st.markdown("""
### Medical Recommendation

- Consult a healthcare professional for proper medical evaluation.
- Maintain regular blood sugar monitoring.
- Follow a balanced diet and healthy lifestyle.
- Engage in regular physical activity.
- Avoid smoking and excessive unhealthy food consumption.
""")



    else:

        st.success(
            "The patient is unlikely to have diabetes."
        )

        st.markdown("""
### Clinical Risk Analysis

The entered clinical parameters indicate a comparatively lower risk of diabetes.
""")

        if len(risk_factors) > 0:

            st.info("### Observed Risk Indicators")

            for factor in risk_factors:
                st.write(f"• {factor}")

        st.markdown("""
### Preventive Health Suggestions

- Continue maintaining a healthy lifestyle.
- Exercise regularly and maintain balanced nutrition.
- Monitor blood sugar periodically.
- Avoid smoking and unhealthy dietary habits.
- Schedule regular medical checkups.
""")



st.markdown("---")

st.caption(
    "This system is intended for educational and research purposes only and should not replace professional medical diagnosis."
)