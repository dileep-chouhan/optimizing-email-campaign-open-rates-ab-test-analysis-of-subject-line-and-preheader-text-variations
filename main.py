import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Define A/B test variations
subject_lines = ['Subject Line A', 'Subject Line B', 'Subject Line C']
preheaders = ['Preheader A', 'Preheader B']
# Generate synthetic data
num_emails = 1000
data = {
    'Subject Line': np.random.choice(subject_lines, size=num_emails),
    'Preheader Text': np.random.choice(preheaders, size=num_emails),
    'Open Rate': np.random.uniform(0.1, 0.4, size=num_emails) # Open rates between 10% and 40%
}
df = pd.DataFrame(data)
# --- 2. Data Analysis ---
# Calculate average open rates for each combination
open_rates = df.groupby(['Subject Line', 'Preheader Text'])['Open Rate'].mean().reset_index()
# Find the best performing combination
best_combination = open_rates.loc[open_rates['Open Rate'].idxmax()]
# --- 3. Visualization ---
plt.figure(figsize=(12, 6))
sns.barplot(x='Subject Line', y='Open Rate', hue='Preheader Text', data=df)
plt.title('Email Open Rates by Subject Line and Preheader Text')
plt.xlabel('Subject Line')
plt.ylabel('Average Open Rate')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Save the plot to a file
output_filename = 'open_rates_barplot.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
print("\n--- Analysis Summary ---")
print("Best performing combination:")
print(best_combination)
#Further analysis could include statistical significance testing (e.g., chi-squared test) to confirm the results are not due to chance.  This example omits that for brevity.