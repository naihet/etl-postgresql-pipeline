from extract import extract_data
from transform import transform_data

# --------------------------------------------------------
# Extract
# --------------------------------------------------------

df = extract_data(
    "data/Sample - Superstore.csv"
)

print("Extract completed")

print(df.head())

# --------------------------------------------------------
# Transform
# --------------------------------------------------------

df = transform_data(df)

print("Transform completed")

print(df.head())

# --------------------------------------------------------
# Validation
# --------------------------------------------------------

print()

print("Rows :", len(df))

print("Columns :", len(df.columns))

print()

print(df.dtypes)

# --------------------------------------------------------
# Missing Values Check
# --------------------------------------------------------

print()

print(df.isnull().sum())

# --------------------------------------------------------
# Duplicate Check
# --------------------------------------------------------

duplicate_count = df.duplicated().sum()

print()

print(f"Duplicate Rows : {duplicate_count}")

# --------------------------------------------------------
# Numeric Column
# --------------------------------------------------------

print()

print(
    df[
        [
            "sales",
            "quantity",
            "discount",
            "profit"
        ]
    ].describe()
)