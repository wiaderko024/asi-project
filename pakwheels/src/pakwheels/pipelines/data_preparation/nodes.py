import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df["assembly"] = df["assembly"].fillna("Local")
    df.dropna(subset=["engine", "year", "fuel", "price", "body", "color"], inplace=True)
    df = df.drop_duplicates()

    return df
