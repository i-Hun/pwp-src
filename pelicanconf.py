#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Oleg Nagornyy'
SITENAME = 'Oleg Nagornyy'
SITEURL = 'http://nagornyy.me'
SITE_DESCRIPTION = "Hi! I am Oleg — Social researcher, Data analyst and Web-developer from Saint Petersburg, Russia. I'm working as Research assistant and Lecturer at HSE"


PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HEADER_COVER = "/theme/img/background-main.jpg"


DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'rst')

THEME = "nagornyy-theme"
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ['assets', 
	# 'pelican-ipynb.markup', 
	# "photos", 
	# "pelican-cite", 
	# "pdf-img",
	"summary"
	]

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

STATIC_PATHS = ['images', 'pdfs']

TYPOGRIFY = True

SLUGIFY_SOURCE = "basename"
