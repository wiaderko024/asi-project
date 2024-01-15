import pandas as pd
import numpy as np
from scipy.special import boxcox1p
from scipy.stats import boxcox_normmax

def clean_data(df: pd.DataFrame) -> pd.DataFrame: # Remove duplicates
    df["assembly"] = df["assembly"].fillna("Local")
    df.dropna(subset=['engine', 'year', 'fuel', 'price', 'body', 'color'], inplace=True)
    df.drop(columns='addref', inplace=True)
    df = df.drop_duplicates()
    df["price"] = np.log1p(df["price"])
    df["engine"] = boxcox1p(df["engine"], boxcox_normmax(df["engine"] + 1))
    df["mileage"] = boxcox1p(df["mileage"], boxcox_normmax(df["mileage"] + 1))
    card_feat = ['year', 'body', 'make', 'city', 'color', 'registered', 'model']

    for cols in card_feat:
        data = df.groupby(cols)["price"].mean()
        for value in data.index:
            df[cols] = df[cols].replace({value: data[value]})
    cat_cols = ['assembly', 'transmission', 'fuel']

    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df