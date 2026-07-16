import pandas as pd


def validate_data(df: pd.DataFrame):

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": df.duplicated().sum(),
        "missing": df.isnull().sum().to_dict()
    }

    return report