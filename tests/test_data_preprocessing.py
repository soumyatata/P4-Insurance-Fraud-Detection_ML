import pytest
import pandas as pd
from src.data_preprocessing import load_data, clean_data

@pytest.fixture
def sample_data():
    # Fixture to create a sample DataFrame for testing
    return pd.DataFrame({
        'policy_number': [123, 456],
        'policy_bind_date': ['2021-01-01', '2021-02-01'],
        'incident_date': ['2022-03-05', '2022-04-10'],
        'insured_zip': [12345, 67890],
        'incident_location': ['City1, State1', 'City2, State2'],
        '_c39': [None, None],  # Empty column
        'policy_state': ['CA', 'NY'],
        'insured_sex': ['MALE', 'FEMALE'],
        'insured_education_level': ['PhD', 'High School'],
        'insured_occupation': ['Engineer', 'Teacher'],
        'incident_type': ['Single Vehicle Collision', 'Multi-vehicle Collision'],
        'collision_type': ['Rear Collision', 'Side Collision'],
        'incident_severity': ['Major Damage', 'Minor Damage']
    })

def test_clean_data(sample_data):
    # Test the clean_data function
    cleaned_df = clean_data(sample_data.copy())  # Pass a copy of the sample data

    # Ensure unwanted columns are dropped
    dropped_columns = ['policy_number', 'policy_bind_date', 'incident_date', 'insured_zip', 'incident_location', '_c39']
    for col in dropped_columns:
        assert col not in cleaned_df.columns, f"{col} should be dropped!"

    # Check if missing values are handled (no NaNs should remain)
    assert not cleaned_df.isnull().values.any(), "There should be no missing values after cleaning!"

    # Check if categorical columns are encoded as integers
    categorical_columns = ['policy_state', 'insured_sex', 'insured_education_level', 
                           'insured_occupation', 'incident_type', 'collision_type', 'incident_severity']
    for col in categorical_columns:
        assert pd.api.types.is_integer_dtype(cleaned_df[col]), f"{col} should be encoded as integer!"
