import pandas as pd

# Import the regular expression library to clean data from (COM), (EDT) etc.
import re

# Define a function to covert NaNs and remove whitespaces
def text_clean(rawDataValue):
    if pd.isna(rawDataValue):
        return None # Convert NaN to None to tell PostgreSQL to store NULL
    
    rawDataValue = str(rawDataValue) # Convert to string
    rawDataValue = re.sub(r'\s*\(.*?\)\s*', '', rawDataValue) # Remove text within and parentheses and whitespaces

    rawDataValue = re.sub(r'^by\s+', '', rawDataValue, flags=re.IGNORECASE) # Remove "By" before authors names

    return rawDataValue.strip() # Remove whitespaces at the beginning and end of string