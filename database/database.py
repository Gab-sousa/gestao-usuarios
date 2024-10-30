import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

URL_POSTGRESQL = os.getenv("URL_POSTGRESQL")
db = PostgresqlDatabase(URL_POSTGRESQL)
