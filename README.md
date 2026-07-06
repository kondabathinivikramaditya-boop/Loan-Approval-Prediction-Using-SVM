# 🏦 Loan Approval Prediction Using Support Vector Machine (SVM)

A Machine Learning project that predicts whether a loan application is likely to be **Approved** or **Rejected** using the **Support Vector Machine (SVM)** algorithm. The project includes complete data preprocessing, model training, evaluation, and an interactive **Streamlit web application** for real-time loan prediction.

---

## 📌 Project Overview

Loan approval is an important decision-making process for financial institutions. This project uses historical loan application data to build a machine learning model that predicts loan approval status based on applicant details.

The project covers the complete machine learning pipeline, including:

- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Scaling
- Model Training using Support Vector Machine (SVM)
- Hyperparameter Tuning using GridSearchCV
- Model Evaluation
- Model Deployment using Streamlit

---

## 🚀 Features

- 📊 Complete Data Preprocessing
- 🧹 Missing Value Imputation
- 🔄 One-Hot Encoding for Categorical Features
- 📈 Feature Scaling using StandardScaler
- 🤖 Loan Prediction using Support Vector Machine (SVM)
- 🎯 Hyperparameter Tuning with GridSearchCV
- 📉 Model Evaluation using Accuracy, Confusion Matrix and Classification Report
- 🌐 Interactive Streamlit Web Application
- 💾 Saved Model using Joblib

---

## 📂 Project Structure

```
Loan-Approval-Prediction-Using-SVM/
│
├── dataset/
│   └── Loan_Approval.csv
│
├── loan_prediction_svm.ipynb
├── app.py
├── loan_approval_svm_model.pkl
├── scaler.pkl
├── README.md
└── requirements.txt
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 📊 Machine Learning Workflow

### 1. Data Collection

- Loan Approval Dataset

### 2. Data Preprocessing

- Missing Value Imputation
- Duplicate Removal
- Feature Selection
- One-Hot Encoding
- Feature Scaling

### 3. Train-Test Split

- 80% Training Data
- 20% Testing Data

### 4. Model Building

- Support Vector Machine (SVM)

### 5. Hyperparameter Tuning

- GridSearchCV

### 6. Model Evaluation

- Accuracy Score
- Confusion Matrix
- Classification Report

### 7. Deployment

- Streamlit Web Application

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Support Vector Machine (SVM) |
| Accuracy | **85%** |
| Hyperparameter Tuning | GridSearchCV |
| Feature Scaling | StandardScaler |

---

## 📸 Streamlit Application

The Streamlit application allows users to enter applicant details and instantly predict whether the loan is likely to be approved or rejected.

### Input Features

- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Gender
- Marital Status
- Dependents
- Education
- Self Employed
- Property Area

### Output

- ✅ Loan Approved
- ❌ Loan Rejected

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/kondabathinivikramaditya-boop/Loan-Approval-Prediction-Using-SVM.git
```

### Navigate to Project

```bash
cd Loan-Approval-Prediction-Using-SVM
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

```
streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
seaborn
```

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Preprocessing
- Feature Engineering
- Machine Learning Pipeline
- Support Vector Machine (SVM)
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization using Joblib
- Streamlit Deployment
- Git & GitHub Version Control

## 👨‍💻 Author

**Vikramaditya Kondabathini**

B.Tech CSE (Data Science)

St. Peters Engineering College


## 📜 License

This project is created for educational and learning purposes.
