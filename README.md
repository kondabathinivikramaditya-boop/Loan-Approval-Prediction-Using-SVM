# Loan Approval Prediction Using Support Vector Machine (SVM)

## Project Overview

This project aims to predict whether a loan application will be approved using a Support Vector Machine (SVM).

The project is currently in the data preprocessing stage. The dataset has been loaded, explored, cleaned, and prepared for model training.

---

## Dataset

- Dataset: Loan Approval Prediction
- Total Records: 614
- Total Features: 13
- Target Variable: Loan_Status

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow (Completed)

### 1. Imported Required Libraries

Imported all the required Python libraries for data analysis and machine learning.

### 2. Loaded the Dataset

Loaded the Loan Approval dataset into a Pandas DataFrame.

### 3. Explored the Dataset

Performed basic data exploration using:

- `head()`
- `shape`
- `info()`
- `describe()`
- `isnull().sum()`

### 4. Data Cleaning

- Checked for missing values.
- Handled missing values.
- Verified that the dataset contains no missing values.

### 5. Feature Selection

Separated the dataset into:

- **Features (X)**
- **Target Variable (y)**

### 6. Train-Test Split

Split the dataset into:

- **80% Training Data**
- **20% Testing Data**

Output:

```
X_train : (491, 14)
X_test  : (123, 14)

y_train : (491,)
y_test  : (123,)
```

---

## Current Project Status

Completed:

- Import Libraries
- Load Dataset
- Explore Dataset
- Handle Missing Values
- Feature Selection
- Train-Test Split

Upcoming Steps:

- Encode Categorical Variables (if required)
- Feature Scaling
- Train Support Vector Machine (SVM)
- Model Evaluation
- Confusion Matrix
- Classification Report
- Save the Model
- Build a Streamlit Web Application

---

## Repository Structure

```
Loan-Approval-Prediction-Using-SVM/
│
├── dataset/
│   └── Loan_approval.csv
│
├── loan_prediction_svm.ipynb
│
└── README.md
```

---

## Author

**Vikramaditya Kondabathini**

GitHub:
https://github.com/kondabathinivikramaditya-boop
