import os

class Config:
    # API keys
    API_KEY = os.getenv('API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database settings
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    # Bot parameters
    BOT_NAME = os.getenv('BOT_NAME')
    BOT_VERSION = os.getenv('BOT_VERSION')
    DEBUG = os.getenv('DEBUG') == 'True'