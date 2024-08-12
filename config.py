import os
import dotenv



dotenv.load_dotenv()

# Объявление переменных из окружения
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def get_auth():
    return USERNAME, PASSWORD