import pandas as pd
import numpy as np

class DepressionAnxietyDataCleaner:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        """Load the dataset from the CSV file."""
        self.df = pd.read_csv(self.input_path)
        print("Data loaded successfully.")

    def initial_transformations(self):
        """Perform initial transformations, such as replacing values and setting data types."""
        self.df['epworth_score'] = pd.to_numeric(self.df['epworth_score'], errors='coerce').fillna(-1).astype(int)
        self.df = self.df.astype({
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
        print("Initial transformations completed.")

    def drop_na_columns(self):
        """Remove rows with NA in critical independent columns."""
        self.df = self.df.dropna(subset=['suicidal', 'anxiety_diagnosis', 'anxiety_treatment', 
                                         'depression_diagnosis', 'depression_treatment'])
        print("Dropped rows with NA in critical independent columns.")

    def calculate_medians(self):
        """Calculate median values for key columns."""
        self.median_bmi = self.df['bmi'].median()
        self.median_phq = self.df['phq_score'].median()
        self.median_epworth = self.df['epworth_score'].median()
        self.median_gad = self.df['gad_score'].median()
        print("Medians calculated.")

    def clean_bmi_column(self):
        """Clean the 'bmi' column by replacing 0 values with the median."""
        self.df['bmi'] = self.df['bmi'].replace(0, self.median_bmi)
        print("BMI column cleaned.")

    def update_who_bmi(self):
        """Update the 'who_bmi' column based on 'bmi' values."""
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

        self.df['who_bmi'] = self.df['bmi'].apply(calculate_who_bmi)
        print("WHO BMI column updated.")

    def clean_epworth_score(self):
        """Clean the 'epworth_score' column by replacing values < 0 or > 27 with the median."""
        self.df['epworth_score'] = self.df['epworth_score'].apply(lambda x: self.median_epworth if x < 0 or x > 27 else x)
        print("Epworth score column cleaned.")

    def update_sleepiness(self):
        """Update the 'sleepiness' column based on 'epworth_score'."""
        self.df['sleepiness'] = self.df['epworth_score'] > 9
        print("Sleepiness column updated.")

    def clean_gad_related_columns(self):
        """Clean the 'gad_score' related columns."""
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

        self.df['anxiety_severity'] = self.df['gad_score'].apply(calculate_anxiety_severity)
        self.df['anxiousness'] = self.df['gad_score'] > 9
        print("GAD-related columns cleaned.")

    def clean_phq_related_columns(self):
        """Clean the 'phq_score' related columns."""
        self.df['phq_score'] = self.df.apply(lambda row: self.median_phq if row['phq_score'] == 0 and row['depression_severity'] == "NA" else row['phq_score'], axis=1)

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

        self.df['depression_severity'] = self.df['phq_score'].apply(calculate_depression_severity)

        self.df['depressiveness'] = self.df.apply(lambda row: "TRUE" if row['phq_score'] < 9 and row['suicidal'] == "TRUE" else ("TRUE" if row['phq_score'] > 9 else "FALSE"), axis=1)
        print("PHQ-related columns cleaned.")

    def reorder_columns(self):
        """Reorder the columns in the DataFrame."""
        self.df = self.df[['id', 'school_year', 'age', 'gender', 'bmi', 'who_bmi', 'phq_score', 
                           'depression_severity', 'depressiveness', 'suicidal', 
                           'depression_diagnosis', 'depression_treatment', 'gad_score', 
                           'anxiety_severity', 'anxiousness', 'anxiety_diagnosis', 
                           'anxiety_treatment', 'epworth_score', 'sleepiness']]
        print("Columns reordered.")

    def final_type_conversions(self):
        """Perform final type conversions to ensure correct data types."""
        self.df = self.df.astype({
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
        print("Final type conversions done.")

    def save_cleaned_data(self):
        """Save the cleaned DataFrame to a new CSV file."""
        self.df.to_csv(self.output_path, index=False)
        print(f"Cleaned data saved to {self.output_path}.")

    def clean_dataset(self):
        """Execute the full data cleaning process."""
        self.load_data()
        self.initial_transformations()
        self.drop_na_columns()
        self.calculate_medians()
        self.clean_bmi_column()
        self.update_who_bmi()
        self.clean_epworth_score()
        self.update_sleepiness()
        self.clean_gad_related_columns()
        self.clean_phq_related_columns()
        self.reorder_columns()
        self.final_type_conversions()
        self.save_cleaned_data()
