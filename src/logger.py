import logging
from pathlib import Path

# ------------------------------------------------------------
# Create logs directory
# ------------------------------------------------------------
Path("logs").mkdir(exist_ok=True)

# ------------------------------------------------------------
# Configure Logger
# ------------------------------------------------------------
logger = logging.getLogger("etl")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

#
# Write log to file
#
file_handler = logging.FileHandler("logs/etl.log")
file_handler.setFormatter(formatter)

#
# Show log on Docker console
#
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)