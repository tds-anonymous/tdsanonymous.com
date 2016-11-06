#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

AUTHOR = u'alex'
SITENAME = u'tds-anonymous'
SITEURL = 'tdsanonymous.com'

THEME = "themes/twenty"
PATH = 'content'

from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar, 'pretty_date': filters.pretty_date }

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['better_code_samples']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('github', 'http://github.com/tdsanonymous'),)

DEFAULT_PAGINATION = 3
POST_LIMIT = 3

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%Y-%m-%dT%H:%M:%SZ')

# Formatting for urls
# ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_DIR = 'pages'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = ['images', 'fonts', 'css', 'js',]

import datetime
now = datetime.datetime.utcnow()
YEAR = now.strftime("%Y")
