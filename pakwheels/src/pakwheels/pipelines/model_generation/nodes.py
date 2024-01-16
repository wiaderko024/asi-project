import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def generate_pickle(df: pd.DataFrame):
    X = df.drop(columns="price", axis=1)
    y = df["price"]
    scalar = RobustScaler()
    X_scaled = scalar.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=45)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pkl_model = pickle.dumps(model)

    return(pkl_model)
