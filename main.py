
import pandas as pd
from pathlib import Path

DATA_FILE = Path("experimental_data_M0-M9_complete.csv")

INPUT_COLUMNS = [
    "Cement_kg_m3",
    "PET_kg_m3",
    "Fine_Aggregate_kg_m3",
    "RHA_kg_m3",
    "Coarse_Aggregate_kg_m3",
    "Water_kg_m3",
    "Superplasticizer_kg_m3",
]

TARGET_COLUMNS = [
    "CS_MPa",
    "STS_MPa",
    "FS_MPa",
    "WA_Percent",
    "MoE_GPa",
    "RCPT_Coulombs",
]


def load_experimental_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {DATA_FILE}. "
            "Keep the CSV file in the same folder as main.py."
        )

    data = pd.read_csv(DATA_FILE)

    required = ["Mix_ID"] + INPUT_COLUMNS + TARGET_COLUMNS
    missing = [column for column in required if column not in data.columns]

    if missing:
        raise ValueError(f"Missing CSV columns: {missing}")

    print("Dataset loaded successfully.")
    print(f"Number of mixes: {len(data)}")
    print(f"Input features: {len(INPUT_COLUMNS)}")
    print(f"Prediction targets: {len(TARGET_COLUMNS)}")
    print("\nAvailable data:")
    print(data[required].to_string(index=False))

    return data


if __name__ == "__main__":
    dataset = load_experimental_data()
