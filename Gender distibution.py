import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv")

# Calculate the distribution of genders
gender_distribution = df['Gender'].value_counts()

# Generate labels and sizes for the pie chart
labels = gender_distribution.index
sizes = gender_distribution.values

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Gender Distribution of Patients')

# Display the plot
plt.show()
