import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load  the dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv")

# First, let's visualize Blood Pressure distribution by Age and Gender
plt.figure(figsize=(12, 6))
sns.boxplot(x='Age', y='Blood Pressure', hue='Gender', data=df, palette="Set3")
plt.title('Blood Pressure Distribution by Age and Gender')
plt.xticks(rotation=45)  # Rotate Age labels for better readability
plt.show()

# Next, visualize Cholesterol Levels by Age and Gender
plt.figure(figsize=(12, 6))
sns.boxplot(x='Age', y='Cholesterol Level', hue='Gender', data=df, palette="Set2")
plt.title('Cholesterol Levels Distribution by Age and Gender')
plt.xticks(rotation=45)  # Rotate Age labels for better readability
plt.show()
