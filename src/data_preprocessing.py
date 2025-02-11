import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(filepath):
    """
    Load raw data from CSV file.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(filepath)

def clean_data(df):
    """
    Clean the data by dropping unnecessary columns, filling missing values,
    and encoding categorical variables.
    Args:
        df (pd.DataFrame): The raw data.
    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Drop unnecessary columns
    columns_to_drop = ['policy_number', 'policy_bind_date', 'incident_date', 'insured_zip', 
                       'incident_location', '_c39']
    df.drop(columns=columns_to_drop, inplace=True)
    
    # Forward fill missing values
    df.ffill(inplace=True)  # Fill missing values using forward fill

    # Encode categorical features
    categorical_columns = ['policy_state', 'insured_sex', 'insured_education_level', 
                           'insured_occupation', 'incident_type', 'collision_type', 'incident_severity']
    encoder = LabelEncoder()
    for col in categorical_columns:
        df[col] = encoder.fit_transform(df[col])
    
    return df
