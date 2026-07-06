import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="Loan Approval Prediction using SVM",
    page_icon="🏦",
    layout="centered"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("loan_approval_svm_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🏦 Loan Approval Prediction")

st.sidebar.info(
"""
Machine Learning Model

✔ Support Vector Machine (SVM)

Dataset

Loan Approval Dataset

Model Accuracy

79.67%

Developer

Vikramaditya Kondabathini
"""
)

# ---------------- TITLE ---------------- #

st.title("🏦 Loan Approval Prediction using SVM")

st.write(
"""
Predict whether a loan application is likely to be approved
using a trained Support Vector Machine (SVM) model.

Fill in all the applicant details below.
"""
)

st.markdown("---")

# ---------------- INPUTS ---------------- #

ApplicantIncome = st.number_input(
    "💰 Monthly Applicant Income (₹)",
    min_value=0,
    value=5000,
    step=500
)

CoapplicantIncome = st.number_input(
    "💰 Monthly Co-applicant Income (₹)",
    min_value=0,
    value=1500,
    step=500
)

LoanAmount = st.number_input(
    "🏦 Loan Amount Required (in Thousands ₹)",
    min_value=1,
    value=120
)

Loan_Amount_Term = st.selectbox(
    "📅 Loan Repayment Period (Months)",
    [12,36,60,84,120,180,240,300,360],
    index=8
)

Credit_History = st.selectbox(
    "👍 Have you maintained a good credit history?",
    ["Yes","No"]
)
Gender = st.selectbox(
    "👤 Gender",
    ["Male", "Female"]
)

Married = st.selectbox(
    "💍 Marital Status",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "👨‍👩‍👧 Number of Dependents",
    ["0", "1", "2", "3+"]
)

Education = st.selectbox(
    "🎓 Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.selectbox(
    "💼 Self Employed",
    ["No", "Yes"]
)

Property_Area = st.selectbox(
    "🏡 Property Area",
    ["Rural", "Semiurban", "Urban"]
)

st.markdown("---")

# ---------------- CONVERT INPUTS ---------------- #

Gender_Male = 1 if Gender == "Male" else 0

Married_Yes = 1 if Married == "Yes" else 0

Dependents_1 = 1 if Dependents == "1" else 0
Dependents_2 = 1 if Dependents == "2" else 0
Dependents_3 = 1 if Dependents == "3+" else 0

Education_Not_Graduate = 1 if Education == "Not Graduate" else 0

Self_Employed_Yes = 1 if Self_Employed == "Yes" else 0

Property_Area_Semiurban = 1 if Property_Area == "Semiurban" else 0

Property_Area_Urban = 1 if Property_Area == "Urban" else 0
# ---------------- CREATE INPUT DATA ---------------- #

input_data = pd.DataFrame([{
    "ApplicantIncome": ApplicantIncome,
    "CoapplicantIncome": CoapplicantIncome,
    "LoanAmount": LoanAmount,
    "Loan_Amount_Term": Loan_Amount_Term,
    "Credit_History": 1 if Credit_History == "Yes" else 0,
    "Gender_Male": Gender_Male,
    "Married_Yes": Married_Yes,
    "Dependents_1": Dependents_1,
    "Dependents_2": Dependents_2,
    "Dependents_3+": Dependents_3,
    "Education_Not Graduate": Education_Not_Graduate,
    "Self_Employed_Yes": Self_Employed_Yes,
    "Property_Area_Semiurban": Property_Area_Semiurban,
    "Property_Area_Urban": Property_Area_Urban
}])

# Keep the same column order used while training

input_data = input_data[[
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
    "Gender_Male",
    "Married_Yes",
    "Dependents_1",
    "Dependents_2",
    "Dependents_3+",
    "Education_Not Graduate",
    "Self_Employed_Yes",
    "Property_Area_Semiurban",
    "Property_Area_Urban"
]]

# Scale the user input

input_scaled = scaler.transform(input_data)

st.markdown("---")
# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict Loan Approval", use_container_width=True):

    prediction = model.predict(input_scaled)

    st.markdown("---")
    st.subheader("📋 Prediction Result")

    if prediction[0] == 1:
        st.success("✅ Congratulations! The loan is likely to be **APPROVED**.")
    else:
        st.error("❌ Sorry! The loan is likely to be **REJECTED**.")

    st.markdown("---")
    st.subheader("📄 Applicant Details")

    result = pd.DataFrame({
        "Feature": [
            "Monthly Applicant Income (₹)",
            "Monthly Co-applicant Income (₹)",
            "Loan Amount (₹ Thousands)",
            "Loan Repayment Period (Months)",
            "Good Credit History",
            "Gender",
            "Marital Status",
            "Dependents",
            "Education",
            "Self Employed",
            "Property Area"
        ],
        "Value": [
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_History,
            Gender,
            Married,
            Dependents,
            Education,
            Self_Employed,
            Property_Area
        ]
    })

    st.dataframe(result, use_container_width=True)

    st.markdown("---")
    st.info(
        """
        **Note:** This prediction is generated using a Support Vector Machine (SVM)
        model trained on the Loan Approval dataset. It is intended for educational
        and demonstration purposes only.
        """
    )

