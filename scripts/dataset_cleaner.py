import pandas as pd
import numpy as np

# 1. Load the data
df = pd.read_csv("data/depression_anxiety_data.csv")

# 2. Initial data transformations
# Ensure correct data types
df['epworth_score'] = df['epworth_score'].replace("NA", -1).fillna(-1).astype(int)


df = df.astype({
    'id': 'int64',
    'school_year': 'int64',
    'age': 'int64',
    'bmi': 'float',
    'who_bmi': 'str',
    'phq_score': 'int64',
    'depression_severity': 'str',
    'depressiveness': 'str',
    'gad_score': 'int64',
    'anxiety_severity': 'str',
    'epworth_score': 'int64'
})

# 3. Remove rows with NA in critical independent columns
df = df.dropna(subset=['suicidal', 'anxiety_diagnosis', 'anxiety_treatment', 
                       'depression_diagnosis', 'depression_treatment'])

# 4. Calculate median values for key columns
median_bmi = df['bmi'].median()
median_phq = df['phq_score'].median()
median_epworth = df['epworth_score'].median()
median_gad = df['gad_score'].median()

# 5. Clean the 'bmi' column by replacing 0 values with the median
df['bmi'] = df['bmi'].replace(0, median_bmi)

# 6. Update the 'who_bmi' column based on 'bmi' values
def calculate_who_bmi(bmi):
    if bmi < 18.4:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    elif bmi < 34.9:
        return "Class I Obesity"
    elif bmi < 40:
        return "Class II Obesity"
    elif bmi > 40:
        return "Class III Obesity"
    else:
        return "NA"

df['who_bmi'] = df['bmi'].apply(calculate_who_bmi)

# 7. Clean the 'epworth_score' column by replacing values < 0 or > 27 with the median
df['epworth_score'] = df['epworth_score'].apply(lambda x: median_epworth if x < 0 or x > 27 else x)

# 8. Update the 'sleepiness' column based on 'epworth_score'
df['sleepiness'] = df['epworth_score'] > 9

# 9. Clean the 'gad_score' related columns
def calculate_anxiety_severity(gad_score):
    if gad_score < 4:
        return "None-minimal"
    elif gad_score < 9:
        return "Mild"
    elif gad_score < 14:
        return "Moderate"
    elif gad_score < 21:
        return "Severe"
    else:
        return "NA"

df['anxiety_severity'] = df['gad_score'].apply(calculate_anxiety_severity)
df['anxiousness'] = df['gad_score'] > 9

# 10. Clean the 'phq_score' related columns
df['phq_score'] = df.apply(lambda row: median_phq if row['phq_score'] == 0 and row['depression_severity'] == "NA" else row['phq_score'], axis=1)

def calculate_depression_severity(phq_score):
    if phq_score < 4:
        return "None-minimal"
    elif phq_score < 9:
        return "Mild"
    elif phq_score < 14:
        return "Moderate"
    elif phq_score < 19:
        return "Moderately severe"
    elif phq_score < 27:
        return "Severe"
    else:
        return "NA"

df['depression_severity'] = df['phq_score'].apply(calculate_depression_severity)

df['depressiveness'] = df.apply(lambda row: "TRUE" if row['phq_score'] < 9 and row['suicidal'] == "TRUE" else ("TRUE" if row['phq_score'] > 9 else "FALSE"), axis=1)

# 11. Reorder the columns
df = df[['id', 'school_year', 'age', 'gender', 'bmi', 'who_bmi', 'phq_score', 
         'depression_severity', 'depressiveness', 'suicidal', 
         'depression_diagnosis', 'depression_treatment', 'gad_score', 
         'anxiety_severity', 'anxiousness', 'anxiety_diagnosis', 
         'anxiety_treatment', 'epworth_score', 'sleepiness']]

# 12. Final type conversions
df = df.astype({
    'id': 'int64',
    'school_year': 'int64',
    'age': 'int64',
    'bmi': 'float',
    'who_bmi': 'str',
    'phq_score': 'int64',
    'depression_severity': 'str',
    'depressiveness': 'str',
    'gad_score': 'int64',
    'anxiety_severity': 'str',
    'epworth_score': 'int64',
    'sleepiness': 'bool',
    'anxiety_treatment': 'bool',
    'anxiety_diagnosis': 'bool',
    'anxiousness': 'bool',
    'depression_treatment': 'bool',
    'depression_diagnosis': 'bool',
    'suicidal': 'bool'
})

# Optional: Save the cleaned DataFrame to a new CSV file
output_path = "data/cleaned_data.csv"
df.to_csv(output_path, index=False)
