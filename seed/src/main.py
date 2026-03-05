import pandas as pd
df = pd.read_csv("./data/BooksDatasetClean.csv", nrows=5)
print(list(df.columns))
print(df.head(5))

print(df.info())