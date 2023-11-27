import os
from dotenv import load_dotenv

load_dotenv()

# Acceder a las variables de entorno
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME= os.getenv("DB_NAME", "postgres")
DB_PORT= os.getenv("PORT", "5432")
