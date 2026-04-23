"""
Production settings.
Usage: DJANGO_SETTINGS_MODULE=settings.prod
All secrets come from environment variables — never hard-code them here.
"""

from .base import *  # noqa: F401, F403

DEBUG = False

# Security headers
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files served via CDN / whitenoise
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE[1:],  # noqa: F405
]
INSTALLED_APPS += ["whitenoise.runserver_nostatic"]  # noqa: F405
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Cache — update DATABASE_CACHE_URL or REDIS_URL as infrastructure is decided
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
