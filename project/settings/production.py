import os

import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import *  # noqa: F403


SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {"default": dj_database_url.config()}

ALLOWED_HOSTS = [
    "project-production.herokuapp.com",
    "project-staging.herokuapp.com",
]

if "HEROKU_APP_NAME" in os.environ:
    app_name = os.environ["HEROKU_APP_NAME"]
    ALLOWED_HOSTS.append(f"{app_name}.herokuapp.com")

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")  # noqa: F405
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

sentry_sdk.init(
    os.environ["SENTRY_DSN"],
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.5,
    send_default_pii=True,
)

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
