import pandas as pd
import numpy as np
import random

# Reproducibility
random.seed(42)
np.random.seed(42)

# Possible categories
sex = ['Male', 'Female']
smoker = ['Yes', 'No']
day = ['Thur', 'Fri', 'Sat', 'Sun']
time = ['Lunch', 'Dinner']
sizes = [1, 2, 3, 4, 5, 6]

# Generate 250 random rows
n = 250
data = {
    'total_bill': np.round(np.random.uniform(10, 50, n), 2),
    'tip': np.round(np.random.uniform(1, 10, n), 2),
    'sex': np.random.choice(sex, n),
    'smoker': np.random.choice(smoker, n),
    'day': np.random.choice(day, n),
    'time': np.random.choice(time, n),
    'size': np.random.choice(sizes, n)
}

# Create DataFrame
tips_large = pd.DataFrame(data)

# Save to CSV
tips_large.to_csv('tips.csv', index=False)

print("✅ tips.csv created with", len(tips_large), "rows")
print(tips_large.head())
