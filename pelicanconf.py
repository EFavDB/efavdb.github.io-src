#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path


CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site settings
AUTHOR = 'efavdb'
SITENAME = 'EFAVDB'
SITESUBTITLE = "Everybody's Favorite Data Blog"
SITEURL = 'http://frangipane.github.io'
#SITEURL = 'localhost'
THEME = f'{CURRENT_DIR_PATH}/theme'
PATH = 'content'

# General settings
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50
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
         ('About & Consulting', '/about.html'),
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
PLUGINS = ['sitemap',
           'summary',
           'render_math',
           'neighbors',
]

# Theme specific setting
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False  # turn this off so we can specify ordering
MENUITEMS = [('Home', '/'),
             ('About & Consulting', '/pages/about.html'),
             ('Archive', '/archives.html'),
             ('Tags', '/tags.html'),
             ('linselect - feature selection','/pages/linselect.html'),
]
#HOME_COVER = 'images/home_cover_santa_barbara.jpg'

# theme specific settings
SHOW_CREDITS = False
AUTHORS_BIO = {
    "jonathan landy": {
        "name": "Jonathan Landy",
        "cover": "/images/home_cover_santa_barbara.jpg",
        "image": "/wp-content/uploads/2014/12/JonathanLinkedIn.jpg",
        "bio": "Jonathan grew up in the midwest and then went to school at Caltech and UCLA. Following this, he did two postdocs, one at UCSB and one at UC Berkeley.  His academic research focused primarily on applications of statistical mechanics, but his professional passion has always been in the mastering, development, and practical application of slick math methods/tools. He worked as a data-scientist at Square for four years and is now working on a quantitative investing startup."
    },
    "dustin mcintosh": {
        "name": "Dustin McIntosh",
        "cover": "/images/home_cover_santa_barbara.jpg",
        "image": "/wp-content/uploads/2014/12/DustinLinkedIn2.png",
        "bio": "Dustin got a B.S in Engineering Physics from the Colorado School of Mines (Golden, CO) before moving to UC Santa Barbara for graduate school. There he became interested in Soft Condensed Matter Physics and Polymer Physics, studying the interaction between single DNA molecules and salt ions. After a brief postdoc at UC San Diego studying the physics of bacterial growth, Dustin decided to move into the data science business for good - he is now a Quantitative Analyst at Google in Mountain View."
    },
    "damien rj": {
        "name": "Damien Ramunno-Johnson",
        "cover": "/images/home_cover_santa_barbara.jpg",
        "image": "/wp-content/uploads/2014/12/headshot.jpg",
        "bio": "Damien is a highly experienced researcher with a background in clinical and applied research. Like JSL, he got his PhD at UCLA. He has many years of experience working with imaging, and has a particularly strong background in image segmentation, registration, detection, data analysis, and more recently machine learning. He now works as a data-scientist at Square in San Francisco."
    },
    "cathy yeh": {
        "name": "Cathy Yeh",
        "cover": "/images/home_cover_santa_barbara.jpg",
        "image": "/wp-content/uploads/2014/12/cathy_photo.jpg",
        "bio": "Cathy Yeh got a PhD at UC Santa Barbara studying soft-matter/polymer physics. She is currently looking to transition to a career in data science after wrapping up work with the translational modeling group in a pharmaceutical company in San Diego. She enjoys mining big data and big ice cream and seeing how both can help make the world a better place."
    },
}

## plugin settings
# render_math
MATH_JAX = {
    'process_summary': True
}

# sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}



# publish
DELETE_OUTPUT_DIRECTORY = False
