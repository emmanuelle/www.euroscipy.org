#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'The EuroSciPy team <info@euroscipy.org>'
SITENAME = u'EuroSciPy'
SITEURL = ''

TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'


# Set the article URL
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Euroscipy 2017', 'index.html'),  # i.e. home
             ('About', 'about.html'),  # contact info and who makes up the org and committees
             ('Venue', 'venue.html'),
             ('Program', 'program.html'),
             ('Code of Conduct', 'coc.html'),
             ]

NEWEST_FIRST_ARCHIVES = False

DIRECT_TEMPLATES = ('index', )
 # Theme
THEME_DIR = os.path.join(os.getcwd(), "theme")
THEME_NAME = "tuxlite_zf"
THEME = os.path.join(THEME_DIR, THEME_NAME)
RECENT_ARTICLES_COUNT = 3


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['images', 'pdf', 'CNAME']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
