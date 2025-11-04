"""
Django settings for MyProject project (Render Production Version)
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECURITY SETTINGS
# -------------------------
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-v3us$9a_-mhmeu+63l8f-p3gvcl#b+yxgjj+81xy=-fc@*p3_g"
)

# ✅ Turn off debug for production
DEBUG = False

# ✅ Render domain and local dev hosts
ALLOWED_HOSTS = [
    "sicat-peitel-backend.onrender.com",
    "localhost",
    "127.0.0.1",
    "192.168.30.227",
]

# ✅ CSRF trusted origins (must include scheme)
CSRF_TRUSTED_ORIGINS = [
    "https://sicat-peitel-backend.onrender.com",
    "http://127.0.0.1:8000",
    "http://192.168.30.227:8000",
]

# ✅ Tell Django that requests from Render’s proxy are HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ✅ Enable HTTPS-only cookies in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ✅ Redirect all HTTP traffic to HTTPS
SECURE_SSL_REDIRECT = True

# -------------------------
# APPLICATIONS
# -------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "registration",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "MyProject.urls"

CORS_ALLOW_ALL_ORIGINS = True  # You can tighten this later if needed

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "MyProject.wsgi.application"

# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES (Render setup)
# -------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Optional: whitenoise for efficient static file serving on Render
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# -------------------------
# DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -------------------------
# LOCAL DEVELOPMENT HELPERS
# -------------------------
# If you’re running locally and want to debug again, just set:
# DEBUG = True
# SECURE_SSL_REDIRECT = False
# CSRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
