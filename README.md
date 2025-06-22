# Predictive-Analytics-in-E-Commerce-Sales-Forecasting-and-Customer-Segmentation
Built predictive models with regression and classification techniques to optimize stock levels and targeted promotions.

# 🏥 Predictive Modeling in Healthcare Using Decision Trees

This project focuses on predicting the type of medical care a patient needs—ranging from routine check-ups to specialist consultations—using decision tree classifiers. It leverages real-world symptom and demographic data to support optimized healthcare planning and early diagnosis strategies.

---

## 🎯 Objective

To develop a decision tree-based predictive model that categorizes patient needs into:
- 🟢 **Routine Check-up**
- 🟠 **Urgent Care**
- 🔴 **Specialist Consultation**

This model assists healthcare providers in triaging patients efficiently based on symptoms and risk factors.

---

## 🛠️ Tools & Libraries

- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- DecisionTreeClassifier from Scikit-learn
- Graphical visualizations for:
  - Confusion Matrix
  - Feature Importance
  - Symptom Frequency
  - Age, Gender, Blood Pressure Distributions

---

## 📁 Dataset Overview

- **Source**: Disease symptom and patient profile dataset
- **Features Used**:
  - Age
  - Gender
  - Symptoms: Fever, Cough, Fatigue, Difficulty Breathing
  - Health Metrics: Blood Pressure, Cholesterol Level

- **Target Variable**: Type of Care Needed

---

## 📊 Exploratory Data Analysis (EDA)

Scripts used:
- `Age distribution.py`: Histogram of patient ages  
- `Gender distribution.py`: Pie chart of gender breakdown  
- `Blood pressure distribution.py`: Boxplot of BP vs. age and gender  
- `frequency analysis.py`: Symptom frequency chart  
- `Outliers.py`: Detection of outliers in age  
- `Skewness of Sales Data.py` (if reused): Skew analysis for numeric health data

---

## 🌲 Modeling & Evaluation

### Decision Tree Classification

Scripts:
- `Decision_Tree_Evaluation.py`: Full pipeline for model training and evaluation  
- `Decision_Tree_Gender.py`: Separate model performance analysis for male and female patients  
- `Decision_Tree_Visualization.py`: Confusion matrix and feature importance plots

### Evaluation Metrics:
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)
- Feature Importances

📷 _Sample Outputs (to upload as images in GitHub):_
- Confusion matrix heatmaps  
- Feature importance bar charts  
- Tree structure visualizations

---

## ✅ Key Results

- Achieved high classification accuracy on test data  
- Gender-based modeling showed slightly different feature importances  
- Blood Pressure and Age were most influential in predicting “Specialist Consultation” needs  
- Fever and Cough were strong indicators for “Urgent Care”

---

## 📈 Feature Importance (Top Features)

1. **Age**
2. **Blood Pressure**
3. **Difficulty Breathing**
4. **Fever**
5. **Cholesterol Level**

---

## 🚀 Future Enhancements

- Deploy model using Flask as an API for real-time triage
- Use ensemble techniques (Random Forest, Gradient Boosting)
- Apply SHAP for explainable model outputs
- Balance dataset using SMOTE if class imbalance exists

---

## 📬 Author

**Sajith Pemarathna**  
📫 Email: sajiths.pemarathna@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sajith-pemarathna)

---

