from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger
from validate import validate_data
from sqlalchemy import text
from database import engine

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
# Verification
# --------------------------------------------------------

with engine.connect() as conn:

    result = conn.execute(
        text(
            "SELECT COUNT(*) FROM sales"
        )
    )

    total_rows = result.scalar()

print(f"Rows in PostgreSQL : {total_rows}")

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