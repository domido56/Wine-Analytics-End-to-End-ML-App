import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine


features = ['VolatileAcidity', 'TotalSulfurDioxide', 'Chlorides', 'Sulphates']
target = 'ColorBin'

def get_full_dataset():
    engine = create_engine("mssql+pyodbc://./WineWarehouse?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

    query = """
    SELECT
        VolatileAcidity,
        TotalSulfurDioxide,
        Chlorides,
        Sulphates,
        ColorBin
    FROM WineData"""

    df = pd.read_sql(query, engine)
    return df

def get_test_data():
    df = get_full_dataset()
    X = df[features]
    y = df[target]
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    return X_test, y_test

def load_models():
    rf = joblib.load("models/rf.pkl")
    knn = joblib.load("models/knn.pkl")
    svm = joblib.load("models/svm.pkl")
    return rf, knn, svm

if __name__ == "__main__":
    try:
        print("test")
        X_test, y_test = get_test_data()
        print(f"pobrano {len(X_test)} rekordow testowych")
        print("\npierwsze 5 wierszy danych:")
        print(X_test.head())
        print("\npierwsze 5 etykiet:")
        print(y_test.head())
    except Exception as e:
        print(f"bład testu: {e}")
