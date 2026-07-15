import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardize the extracted dataset.
    """

    # --------------------------------------------------------
    # Standardize column names
    # Example:
    #   Order ID -> order_id
    #   Ship Date -> ship_date
    # --------------------------------------------------------
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # --------------------------------------------------------
    # Convert date columns
    # --------------------------------------------------------
    df["order_date"] = pd.to_datetime(df["order_date"])

    df["ship_date"] = pd.to_datetime(df["ship_date"])

    # --------------------------------------------------------
    # Remove duplicate rows
    # --------------------------------------------------------
    df = df.drop_duplicates()

    return df