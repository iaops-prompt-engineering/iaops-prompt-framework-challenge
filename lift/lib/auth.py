import os


def runtime_configured():
    return bool(os.getenv("DATABASE_URL") and os.getenv("API_KEY"))
