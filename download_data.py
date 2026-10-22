
import requests
import pandas as pd
from pathlib import Path

# Create a folder to store CSV files
output_folder = Path("data")
output_folder.mkdir(exist_ok=True)

# Art Institute of Chicago datasets
datasets = ["artworks", "agents", "exhibitions"]

for dataset in datasets:
    url = f"https://api.artic.edu/api/v1/{dataset}"
    all_records = []

    # Download 2 pages of 100 records each
    for page in [1, 2]:
        response = requests.get(
            url,
            params={"limit": 100, "page": page},
            headers={
                "User-Agent": "IS477-Student-Research/1.0",
                "Accept": "application/json"
        },
        timeout=30
        )
        response.raise_for_status()

        records = response.json()["data"]
        all_records.extend(records)

    # Convert JSON records to a table
    df = pd.json_normalize(all_records)

    # Save to CSV
    filename = output_folder / f"{dataset}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved {len(df)} records to {filename}")
