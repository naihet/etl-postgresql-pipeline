import logging
from pathlib import Path

# ------------------------------------------------------------
# Create logs directory if it does not exist
# ------------------------------------------------------------
Path("logs").mkdir(exist_ok=True)

# ------------------------------------------------------------
# Configure logging
# ------------------------------------------------------------
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)