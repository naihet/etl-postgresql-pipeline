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