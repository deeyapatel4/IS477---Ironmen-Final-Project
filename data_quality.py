
import pandas as pd

datasets = {
    "Artworks": "data/artworks.csv",
    "Agents": "data/agents.csv",
    "Exhibitions": "data/exhibitions.csv"
}

for name, path in datasets.items():
    df = pd.read_csv(path)

    print(f"\n===== {name} =====")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Duplicate rows:", df.duplicated().sum())

    print("\nMissing values:")
    print(df.isnull().sum().sort_values(ascending=False).head(10))

    print("\nColumn names:")
    print(df.columns.tolist())
