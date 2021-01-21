from .common import *  # noqa: F403


SECRET_KEY = "CHANGE-ME!"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),  # noqa: F405
    }
}
