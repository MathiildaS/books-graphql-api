import pandas as pd

df = pd.read_csv("./data/BooksDatasetClean.csv", nrows=5)
print(list(df.columns))
print(df.head(5))

print(df.info())

from config import load_config

config = load_config()
print("csv_path:", config.csv_path)
print("chunk_size:", config.chunk_size)
print("sql_uri:", config.sql_uri)