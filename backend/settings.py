from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('USER')
TEST_DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DATABASE')
TEST_DB_NAME = os.getenv('TEST_DATABASE')
DEV_DB_NAME = os.getenv('DEV_DATABASE')