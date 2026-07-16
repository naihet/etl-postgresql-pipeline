import pandas as pd
from database import engine

def load_data(df: pd.DataFrame):

    df.to_sql(
        name="sales",
        con=engine,
        if_exists="replace",
        index=False
    )