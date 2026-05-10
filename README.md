# Intelligent Diabetes Predicition and Clinical Decision Support System

## Overview
This project presents an intelligent diabetes prediction and clinical decision support system developed using machine learning techniques and deployed through Streamlit.
The system performs diabetes risk prediction based on clinical patient parameters and provides supportive clinical risk analysis using a trained Logistic Regression model.
The project initially involved a comparative analysis of multiple machine learning algorithms, including Logistic Regression, Decision Tree, Random Forest, XGBoost, and Naive Bayes, to identify the most effective classifier for diabetes prediction using clinical patient data obtained from SGPGI Hospital.
After comparative evaluation using Accuracy, Precision, Recall, F1-score, Confusion Matrix, and ROC-AUC metrics, Logistic Regression emerged as the best-performing model and was further deployed as an interactive clinical prediction system.


## Machine Learning Models used

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost Classifier
- Naive Bayes Classifier

## Techniques and Methodologies

- Exploratory Data Analysis(EDA)
- SMOTE for class balancing
- Feature Encoding
- ROC_AUC Analysis
- Confusion Matrix Evaluation
- Comparative Performance Analysis
- Diabetes risk prediction using Machine Learning
- Clinical risk factor analysis
- Interactive Streamlit web application
- Logistic Regression deployment model
- User-friendly clinical input interface

## Results
Among all evaluated machine learning models, Logistic Regression achieved the best overall predictive performance on the cleaned clinical dataset.
The model demonstrated the highest ROC-AUC score along with strong accuracy, precision, recall, and F1-score performance, indicating excellent capability in distinguishing diabetic and non-diabetic patients.
The final Logistic Regression model was deployed as an interactive clinical decision support system using Streamlit.

## Clinical Decision Support System
The deployed system allows users to enter clinical patient parameters such as age, obesity status, hypertension, cholesterol level, smoking habit, fasting blood sugar, and hemoglobin level.
Based on the entered parameters, the application predicts diabetes likelihood and provides supportive clinical risk analysis along with major contributing risk factors.


## Future Scope

- Integration with larger clinical datasets
- Hyperparameter optimization
- Explainable AI integration
- Real-time hospital deployment
- Deep learning-based prediction systems
- Electronic Health Record (EHR) integration

## Dataset

The dataset used in this project was obtained from SGPGI Hospital. Due to privacy and ethical considerations, the original datset is not publicly shared.
