
import pandas as pd
from pathlib import Path

FILE = Path("experimental_data_M0-M9_complete.csv")

def main():
    if not FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {FILE}")

    df = pd.read_csv(FILE)

    targets = [
        "CS_MPa", "STS_MPa", "FS_MPa",
        "WA_Percent", "MoE_GPa", "RCPT_Coulombs"
    ]

    print("Rows:", len(df))
    print("Mix IDs:", df["Mix_ID"].tolist())

    missing_columns = [c for c in targets if c not in df.columns]
    if missing_columns:
        print("Missing target columns:", missing_columns)
        return

    print("\nMissing values per target:")
    print(df[targets].isna().sum())

    print("\nTarget summary:")
    print(df[targets].describe())

    if len(df) == 10 and df["Mix_ID"].nunique() == 10:
        print("\nMix count check: PASSED")
    else:
        print("\nMix count check: FAILED")

    if df[targets].isna().any().any():
        print("Completeness check: FAILED")
    else:
        print("Completeness check: PASSED")

if __name__ == "__main__":
    main()
