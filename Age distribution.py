import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv")

# let's visualize its distribution
plt.figure(figsize=(10, 6))

# Calculate bins and histogram
n, bins, patches = plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')

# Round bins to integer and calculate bin centers
bins = np.round(bins).astype(int)  # Round bins and convert to integer
bin_centers = np.round((bins[:-1] + bins[1:]) / 2, 0).astype(int)  # Calculate bin centers as integers

# Adding bin ranges on the x-axis with labels rotated for better visualization
plt.xticks(bin_centers, labels=[f"{bins[i]}-{bins[i+1]}" for i in range(len(bins)-1)], rotation=45)

plt.title('Age Distribution of Patients')
plt.xlabel('Age Range')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Display the plot
plt.show()
