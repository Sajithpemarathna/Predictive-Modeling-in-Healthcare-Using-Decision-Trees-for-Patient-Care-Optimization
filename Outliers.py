import pandas as pd

# path of my dataset
dataset_path = r'C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv'

# Load the dataset
df = pd.read_csv(dataset_path)

# Calculate Q1, Q3, and IQR for 'Age'
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

# Define outliers as those beyond 1.5 times the IQR from the Q1 and Q3
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers in 'Age'
outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print("Number of outliers in Age:", outliers.shape[0])
print("lower_bound is:",lower_bound, "upper_bound is:",upper_bound )
print("Outliers:\n", outliers)
