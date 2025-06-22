import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load my dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv")

# Function to categorize 'Type of Care Needed'
def categorize_care(row):
    if (row['Fever'] == 'Yes' or row['Cough'] == 'Yes' or
        row['Fatigue'] == 'Yes' or row['Difficulty Breathing'] == 'Yes'):
        if row['Age'] > 60 or row['Blood Pressure'] == 'High' or row['Cholesterol Level'] == 'High':
            return 'Specialist Consultation'
        else:
            return 'Urgent Care'
    else:
        return 'Routine Check-up'

# Apply the function to create a new column
df['Type of Care Needed'] = df.apply(categorize_care, axis=1)

# Encode categorical data
df.replace({'No': 0, 'Yes': 1, 'Low': 0, 'Normal': 0, 'High': 1, 'Male': 1, 'Female': 0}, inplace=True)

# Define features and target variable
X = df[['Age', 'Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Gender', 'Blood Pressure', 'Cholesterol Level']]
y = df['Type of Care Needed']

# Split the dataset (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predictions on the test set
y_pred = clf.predict(X_test)

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Combine test data with predictions for display
test_set_with_predictions = X_test.copy()
test_set_with_predictions['Actual Care Needed'] = y_test
test_set_with_predictions['Predicted Care Needed'] = y_pred

# Display the test set with actual and predicted 'Type of Care Needed'
print("\nTest Set with Predicted and Actual 'Type of Care Needed':")
print(test_set_with_predictions)
