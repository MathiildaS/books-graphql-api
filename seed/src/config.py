import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Define immutable EtlConfig dataclass
@dataclass(frozen=True)
class EtlConfig:
    csv_path: str
    chunk_size: int
    sql_uri: str

# Define function to return EtlConfig object with .env variables
def load_config() -> EtlConfig:
    load_dotenv() # From .env file to os.environ

    return EtlConfig(
        csv_path=os.environ.get("CSV_PATH"),
        chunk_size=int(os.environ.get("CHUNK_SIZE")),
        sql_uri=os.environ.get("SQL_URI"),
    )