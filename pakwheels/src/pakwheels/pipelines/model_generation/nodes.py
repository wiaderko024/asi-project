import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib


def generate_model(df: pd.DataFrame):
    X = df.drop(columns="price", axis=1)
    y = df["price"]
    scalar = RobustScaler()
    X_scaled = scalar.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=45
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, "data/07_model_output/linear_regression_model.joblib")

    return model
