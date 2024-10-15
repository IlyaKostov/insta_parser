import os

from dotenv import load_dotenv

load_dotenv()


LOGIN_USERNAME = os.getenv('USERNAME')
LOGIN_PASSWORD = os.getenv('PASSWORD')
PROFILE_NAME = os.getenv('PROFILE_NAME')
DB_NAME = os.getenv('DB_NAME')
