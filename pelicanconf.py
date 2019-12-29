#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path


CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site settings
AUTHOR = 'efavdb'
SITENAME = 'EFAVDB'
SITEURL = 'http://frangipane.github.io'
#SITEURL = 'localhost'
THEME = f'{CURRENT_DIR_PATH}/attila-theme'
PATH = 'content'

# General settings
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 80
#SUMMARY_BEGIN_MARKER = '<!--summary-->'
#SUMMARY_END_MARKER = '<!--more-->'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Page Settings
#PAGE_URL = '{path}'
#PAGE_SAVE_AS = '{path}'
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archive.html'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'wp-content']
PAGE_EXCLUDES = ['wp-content']
ARTICLE_EXCLUDES = ['wp-content']
# have output paths mirror source content's filesystem path hierarchy
# n.b. does not play well with wp-content static path references
#PATH_METADATA = '(?P<path_no_ext>.*)\..*'
#ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'

# Blogroll
LINKS = (('Home', '/index.html'),
         ('About', '/about.html'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/efavdb'),
          ('Another social link', '#'),)



# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'summary']

# Theme specific setting
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False  # turn this off so we can specify ordering
MENUITEMS = [('Home', '/'),
             ('About', '/pages/about.html'),
             ('Archive', '/archives.html'),
             ('Tags', '/tags.html'),
             ('linselect - feature selection','/pages/linselect.html'),
]
HOME_COVER = 'images/home_cover_santa_barbara.jpg'

# theme specific settings
# AUTHORS_BIO = {
#   "jslandy": {
#     "name": "Jonathan Landy",
#     "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
#     "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
#     "website": "http://blog.arulraj.net",
#     "location": "Chennai",
#     "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
#   }
# }


# publish
DELETE_OUTPUT_DIRECTORY = False
