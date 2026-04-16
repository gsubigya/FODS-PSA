'''
reads health.csv, calculates BMI, and assigns 
a Health Status category based on the BMI value.
'''
import pandas as pd

def categorize_health(bmi):
    if bmi < 18.5: return "Underweight"
    elif 18.5 <= bmi <= 24.9: return "Healthy range"
    elif 25 <= bmi <= 29.9: return "Overweight risk"
    elif 30 <= bmi <= 34.9: return "High risk (Diabetes/Heart)"
    elif bmi >= 40: return "Critical health condition"
    else: return "Obese" # Covers the gap between 35 and 40

try:
    df = pd.read_csv("health.csv")

    # BMI = Weight (kg) / [Height (m)]^2 
    # (Assuming Height in CSV is in meters; if in cm, divide by 100 first)
    df['BMI'] = df['weight'] / (df['height'] ** 2)

    # Apply health status logic
    df['Health_Status'] = df['BMI'].apply(categorize_health)

    # Save to a new file to verify
    df.to_csv("health_updated.csv", index=False)
    print("New columns added. Sample of updated data: \n")
    print(df[['weight', 'height', 'BMI', 'Health_Status']].head())

except FileNotFoundError:
    print("Error: 'health.csv' not found.")