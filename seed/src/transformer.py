import pandas as pd

# Import the regular expression library to clean data from (COM), (EDT) etc.
import re

# Define a function to covert NaNs, remove whitespaces, parentheses and "By" from authors names
def text_clean(rawDataValue):
    if pd.isna(rawDataValue):
        return None # Convert NaN to None to tell PostgreSQL to store NULL
    
    rawDataValue = str(rawDataValue) # Convert to string
    rawDataValue = re.sub(r'\s*\(.*?\)\s*', '', rawDataValue) # Remove text within and parentheses and whitespaces

    rawDataValue = re.sub(r'^by\s+', '', rawDataValue, flags=re.IGNORECASE) # Remove "By" before authors names

    return rawDataValue.strip() # Remove whitespaces at the beginning and end of string

def extract_authors(rawAuthorsValue):
    rawAuthorsValue = text_clean(rawAuthorsValue) # Clean the raw authors value
    if not rawAuthorsValue:
        return [] # Return empty list if no value (None, NaN, empty string)
    
    authors = []
    
    for author in rawAuthorsValue.split(" and "): # Split authors by "and"
        author_clean = author.strip() # Remove whitespaces before and after
        authors.append(author_clean) # Add "cleaned" author to list of authors
    return authors