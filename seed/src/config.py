import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

@dataclass(frozen=True)
class EtlConfig:
    csv_path: str
    chunk_size: int
    sql_uri: str