#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Central title
AUTHOR = 'Spurious Correlations AI'

# Link top-left
SITENAME = "About"
SITEURL = ''

# Helpful defaults
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "nest"
NEST_CSS_MINIFY = True

# This image was removed from the base.html template
NEST_HEADER_LOGO = ""#'/images/logo_small.svg'

# Banner background
NEST_HEADER_IMAGES = 'backdrop.jpg'

# In order to display menu items in order, hard-code them
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Team', '/pages/the-team.html'),
    ('Projects', '/pages/projects.html'),
    ('Consulting', '/pages/consulting.html'),
)

# Various titles
NEST_COPYRIGHT = u'&copy; Spurious Correlations AI, 2017'
NEST_INDEX_HEAD_TITLE = u'Spurious Correlations AI'
NEST_INDEX_HEADER_TITLE = u'Spurious Correlations AI'
NEST_INDEX_HEADER_SUBTITLE = u'Machine Learning for the Biomedical World'
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
