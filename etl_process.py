import pandas as pd
from sqlalchemy import create_engine
import datetime

def run_wine_etl():
    print("Start ETL")

    # extract
    try:
        red_wine = pd.read_csv('data/winequality-red.csv', sep=';')
        white_wine = pd.read_csv('data/winequality-white.csv', sep=';')
        print("Dane wczytane z csv")
    except Exception as e:
        print(f"Error podczas wczytywania: {e}")
        return 

    # transform
    red_wine['ColorBin'] = 1
    white_wine['ColorBin'] = 0

    df = pd.concat([red_wine, white_wine], ignore_index=True)

    df.columns = [c.replace(' ', '') for c in df.columns]

    df['LoadDate'] = datetime.datetime.now()

    # load
    engine = create_engine("mssql+pyodbc://./WineWarehouse?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

    try:
        df.to_sql('WineData', con=engine, if_exists='append', index=False)
        print(f"Przesłano {len(df)} wierszy do tabeli WineData")
    except Exception as e:
        print(f"Error podczas ładowania do sql: {e}")


if __name__ == "__main__":
    run_wine_etl()