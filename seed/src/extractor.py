from collections.abc import Iterator
from pathlib import Path
import pandas as pd

# Define a function to read the csv file
def read_csv_chunks(csv_path: str, chunk_size: int) -> Iterator[pd.DataFrame]:

# Create a path object
    csv_file = Path(csv_path)

    # Check if there´s an existing csv file
    if not csv_file.exists():
        raise FileNotFoundError(f"No CSV file found: {csv_file}")

# Read csv file in chunks and return each as a DataFrame
    yield from pd.read_csv(csv_file, chunksize=chunk_size)