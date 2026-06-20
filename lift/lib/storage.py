import os


def database_url():
    return os.getenv("DATABASE_URL", "")
