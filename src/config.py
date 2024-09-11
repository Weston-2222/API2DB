import os
from dotenv import load_dotenv
load_dotenv()


class Api:
    URL_NEW_INFO = os.getenv("API_URL_NEW_INFO")

    SECRET = os.getenv("API_SECRET")


class DB:
    IP = os.getenv("DATABASE_IP")
    PORT = os.getenv("DATABASE_PORT")
    NAME = os.getenv("DATABASE_NAME")
    USER = os.getenv("DATABASE_USER")
    PASSWORD = os.getenv("DATABASE_PASSWORD")
    CLOUD_SQL_CONNECTION_NAME = os.getenv("CLOUD_SQL_CONNECTION_NAME")
    is_production = os.getenv('GAE_ENV', '').startswith('standard')
