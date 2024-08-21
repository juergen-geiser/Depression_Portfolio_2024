import pandas as pd
import numpy as np

class DepressionAnxietyDataCleaner:
    """
    A class used to clean and preprocess the depression and anxiety dataset.
    
    Attributes:
    ----------
    input_path : str
        The file path to the input CSV file.
    output_path : str
        The file path where the cleaned CSV file will be saved.
    df : pd.DataFrame
        The DataFrame that holds the data being processed.
    """

    def __init__(self, input_path, output_path):
        """
        Initializes the data cleaner with paths for input and output files.

        Parameters:
        ----------
        input_path : str
            The path to the input CSV file.
        output_path : str
            The path where the cleaned data will be saved.
        """
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        """
        Loads the dataset from the specified CSV file into a DataFrame.
        """
        self.df = pd.read_csv(self.input_path)
        print("Data loaded successfully.")

    def initial_transformations(self):
        """
        Performs initial data transformations:
        - Replaces 'NA' with -1 in the 'epworth_score' column and converts it to integers.
        - Sets appropriate data types for key columns.
        """
        self.df['epworth_score'] = pd.to_numeric(self.df['epworth_score'], errors='coerce').fillna(-1).astype(int)
        
        # Apply type conversions to other columns
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
        """
        Drops rows where critical independent columns contain NA values.
        These columns are crucial for the analysis and must not have missing values.
        """
        self.df = self.df.dropna(subset=['suicidal', 'anxiety_diagnosis', 'anxiety_treatment', 
                                         'depression_diagnosis', 'depression_treatment'])
        print("Dropped rows with NA in critical independent columns.")

    def calculate_medians(self):
        """
        Calculates the median values for key numerical columns in the dataset.
        The medians are used later to impute missing or invalid data.
        """
        self.median_bmi = self.df['bmi'].median()
        self.median_phq = self.df['phq_score'].median()
        self.median_epworth = self.df['epworth_score'].median()
        self.median_gad = self.df['gad_score'].median()
        print("Medians calculated.")

    def clean_bmi_column(self):
        """
        Cleans the 'bmi' column by replacing zero values with the calculated median.
        This ensures that invalid BMI values are corrected.
        """
        self.df['bmi'] = self.df['bmi'].replace(0, self.median_bmi)
        print("BMI column cleaned.")

    def update_who_bmi(self):
        """
        Updates the 'who_bmi' column based on the values in the 'bmi' column.
        The BMI categories are classified according to WHO standards.
        """
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
            elif bmi >= 40:
                return "Class III Obesity"
            else:
                return "NA"

        self.df['who_bmi'] = self.df['bmi'].apply(calculate_who_bmi)
        print("WHO BMI column updated.")

def clean_epworth_score(self):
    """
    Cleans the 'epworth_score' column based on the following rules:
    - If the score is less than 0, replace it with the median.
    - If the score is 31 or 32 and 'sleepiness' is TRUE, set it to the dynamic average of the closed interval [10, 24] where sleepiness = TRUE.
    - If the score is greater than 24 and 'sleepiness' is not TRUE, replace it with the median.
    - Otherwise, keep the original score.
    """

    # Calculate the dynamic average of the closed interval [10, 24] where sleepiness = TRUE
    interval_avg = self.df[(self.df['epworth_score'] >= 10) & 
                           (self.df['epworth_score'] <= 24) & 
                           (self.df['sleepiness'] == True)]['epworth_score'].mean()

    def adjust_epworth_score(row):
        if row['epworth_score'] < 0:
            return self.median_epworth
        elif row['epworth_score'] in [31, 32] and row['sleepiness']:
            return interval_avg  # Dynamically calculated average value
        elif row['epworth_score'] > 24 and not row['sleepiness']:
            return self.median_epworth
        else:
            return row['epworth_score']

    self.df['epworth_score'] = self.df.apply(adjust_epworth_score, axis=1)
    print("Epworth score column cleaned.")



    self.df['epworth_score'] = self.df.apply(adjust_epworth_score, axis=1)
    print("Epworth score column cleaned.")

    def update_sleepiness(self):
        """
        Updates the 'sleepiness' column based on the values in the 'epworth_score' column.
        A score greater than 9 indicates sleepiness.
        """
        self.df['sleepiness'] = self.df['epworth_score'] > 9
        print("Sleepiness column updated.")

    def clean_gad_related_columns(self):
        """
        Cleans and updates columns related to 'gad_score':
        - 'anxiety_severity' is derived based on the GAD score.
        - 'anxiousness' is a boolean value indicating if the GAD score is above 9.
        """
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
        """
        Cleans and updates columns related to 'phq_score':
        - 'depression_severity' is derived based on the PHQ score.
        - 'depressiveness' is updated based on the PHQ score and suicidal tendencies.
        """
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
        """
        Reorders the columns in the DataFrame to match the desired output structure.
        This ensures consistency in the final dataset.
        """
        self.df = self.df[['id', 'school_year', 'age', 'gender', 'bmi', 'who_bmi', 'phq_score', 
                           'depression_severity', 'depressiveness', 'suicidal', 
                           'depression_diagnosis', 'depression_treatment', 'gad_score', 
                           'anxiety_severity', 'anxiousness', 'anxiety_diagnosis', 
                           'anxiety_treatment', 'epworth_score', 'sleepiness']]
        print("Columns reordered.")

    def final_type_conversions(self):
        """
        Performs final type conversions to ensure all columns have the correct data types.
        This is crucial for consistent data analysis and output.
        """
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
        """
        Saves the cleaned DataFrame to the specified output CSV file.
        """
        self.df.to_csv(self.output_path, index=False)
        print(f"Cleaned data saved to {self.output_path}.")

    def clean_dataset(self):
        """
        Executes the full data cleaning process, including:
        - Loading the data
        - Performing initial transformations
        - Dropping rows with critical NAs
        - Calculating median values
        - Cleaning and updating relevant columns
        - Reordering columns
        - Applying final type conversions
        - Saving the cleaned data to the output path
        """
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
