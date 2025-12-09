# src/data_loader.py
"""Load and validate ocean temperature data."""
import pandas as pd

def load_temperature_data(filepath):
    """
    Load ocean temperature data from CSV.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Temperature data with datetime index
    """
    # BUG: Missing parse_dates parameter
    df = pd.read_csv(filepath)
    return df


def validate_data(df):
    """Check for missing values and valid temperature ranges."""
    if df.isnull().any().any():
        print("Warning: Dataset contains missing values")
    
    temp_col = 'temperature'
    if (df[temp_col] < -2).any() or (df[temp_col] > 35).any():
        print("Warning: Temperature values outside expected range")
    
    return True