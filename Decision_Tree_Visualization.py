import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load and preprocess your dataset
# Replace 'path_to_your_dataset.csv' with the actual path to your dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv")

# Example categorization and encoding - adjust according to your dataset
def categorize_care(row):
    if (row['Fever'] == 'Yes' or row['Cough'] == 'Yes' or
        row['Fatigue'] == 'Yes' or row['Difficulty Breathing'] == 'Yes'):
        if row['Age'] > 60 or row['Blood Pressure'] == 'High' or row['Cholesterol Level'] == 'High':
            return 'Specialist Consultation'
        else:
            return 'Urgent Care'
    else:
        return 'Routine Check-up'

df['Type of Care Needed'] = df.apply(categorize_care, axis=1)
df.replace({'No': 0, 'Yes': 1, 'Low': 0, 'Normal': 0, 'High': 1, 'Male': 1, 'Female': 0}, inplace=True)

# Define features and target variable
X = df[['Age', 'Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Gender', 'Blood Pressure', 'Cholesterol Level']]
y = df['Type of Care Needed']

# Split the dataset (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Plotting the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Plotting Feature Importances
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(12, 6))
plt.title('Feature Importances')
plt.bar(range(X_train.shape[1]), importances[indices], color='blue', align='center')
plt.xticks(range(X_train.shape[1]), [X_train.columns[i] for i in indices], rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.show()
