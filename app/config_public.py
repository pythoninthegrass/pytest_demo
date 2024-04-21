#!/usr/bin/env python

from decouple import config

DEBUG = True

# Flatpages
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_ROOT = "pages"
FLATPAGES_EXTENSION = [".md", ".markdown"]
FLATPAGES_MARKDOWN_EXTENSION = ["codehilite", "fenced_code", "tables"]
FREEZER_DESTINATION_IGNORE = ['.git*', 'CNAME']
PAGES_NUMBER_PER_PAGE = 5

# Mail server
MAIL_SERVER = config("MAIL_SERVER", default="smtp.server.com")
MAIL_PORT = config("MAIL_PORT", default="465", cast=int)
MAIL_USE_SSL = config("MAIL_USE_SSL", default=True, cast=bool)
MAIL_USERNAME = config("MAIL_USERNAME", default="user@example.net")
MAIL_PASSWORD = config("MAIL_PASSWORD", default="password")

# Protection for Cross-site Request Forgery (CSRF)
CSRF_ENABLED = config("CSRF_ENABLED", default=True, cast=bool)
CSRF_SESSION_KEY = config("CSRF_SESSION_KEY", default="secretcsrf")

# Secret key for signing cookies
SECRET_KEY = config("SECRET_KEY", default="secret")
