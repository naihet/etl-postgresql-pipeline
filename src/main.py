from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger
from validate import validate_data

# --------------------------------------------------------
# Extract
# --------------------------------------------------------

df = extract_data(
    "data/Sample - Superstore.csv"
)

logger.info("Extract completed")

print(df.head())

# --------------------------------------------------------
# Transform
# --------------------------------------------------------

df = transform_data(df)

logger.info("Transform completed")

print(df.head())

# --------------------------------------------------------
# Load
# --------------------------------------------------------

load_data(df)

logger.info("Load completed")

# --------------------------------------------------------
# Validation
# --------------------------------------------------------

report = validate_data(df)

print(report)

print(df.dtypes)

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