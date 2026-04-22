from mysql.connector import connect
from app.config import Config

# Create and return a database connection
def get_connection():
    return connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )