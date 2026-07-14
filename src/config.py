from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = "postgres"

DB_PORT = os.getenv("POSTGRES_PORT")

DB_NAME = os.getenv("POSTGRES_DB")

DB_USER = os.getenv("POSTGRES_USER")

DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")