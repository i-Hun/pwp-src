#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Oleg Nagornyy'
SITENAME = 'Oleg Nagornyy'
SITEURL = 'http://nagornyy.me'

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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 50

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
	]

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'

STATIC_PATHS = ['img', 'pdfs']

TYPOGRIFY = True
