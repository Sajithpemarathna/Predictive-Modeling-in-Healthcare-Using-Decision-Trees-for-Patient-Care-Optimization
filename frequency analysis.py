import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# path of dataset file
file_path = r'C:\Users\PC\OneDrive\Desktop\MSc Data Analytics\Fundamentals-of-Data-Analytics-1023-234-UCA-MSC-DA-BER-FDA-T1-G4--2023-Nov-16_20-26-03-477\Assignment\Disease_symptom_and_patient_profile_dataset.csv'
df = pd.read_csv(file_path)

# Count the occurrences of 'Yes' and 'No' for each symptom
yes_counts = df[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']].apply(lambda x: x.value_counts()).loc['Yes']
no_counts = df[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']].apply(lambda x: x.value_counts()).loc['No']

# Preparing data for plotting
symptoms = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']

# Setting up the bar chart
x = np.arange(len(symptoms))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, yes_counts, width, label='Yes')
bars2 = ax.bar(x + width/2, no_counts, width, label='No')

# Adding text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Symptoms')
ax.set_ylabel('Frequency')
ax.set_title('Frequency of Yes/No Responses for Each Symptom')
ax.set_xticks(x)
ax.set_xticklabels(symptoms)
ax.legend()

# Function to attach a text label above each bar, displaying its height
def autolabel(bars):
    """Attach a text label above each bar in *bars*, displaying its height."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(bars1)
autolabel(bars2)
fig.tight_layout()

plt.show()
