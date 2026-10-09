
import pandas as pd
from pathlib import Path

# Load the experimental dataset
DATA_FILE = Path("experimental_data_M0-M9.csv")

def load_experimental_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}. "
            "Place the CSV file in the same folder as main.py."
        )

    data = pd.read_csv(DATA_FILE)

    print("Dataset loaded successfully.")
    print(f"Number of experimental mixes: {len(data)}")
    print(f"Available columns: {list(data.columns)}")
    print("\nFirst five rows:")
    print(data.head().to_string(index=False))

    return data

if __name__ == "__main__":
    dataset = load_experimental_data()
