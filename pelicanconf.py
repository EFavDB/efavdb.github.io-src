#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path


CURRENT_DIR_PATH = Path(__file__).resolve().parent

# Site settings
AUTHOR = 'efavdb'
SITENAME = 'EFAVDB'
SITESUBTITLE = "Everybody's Favorite Data Blog"
SITEURL = ''
GITHUB_URL = 'https://github.com/efavdb'
THEME = f'{CURRENT_DIR_PATH}/elegant-theme'
PATH = 'content'

# General settings
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 6
SUMMARY_MAX_LENGTH = 50
#SUMMARY_BEGIN_MARKER = '<!--summary-->'
#SUMMARY_END_MARKER = '<!--more-->'
DEFAULT_METADATA = {
    'status': 'draft',
}

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
ARCHIVES_URL = 'archives.html'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'wp-content']
PAGE_EXCLUDES = ['wp-content']
ARTICLE_EXCLUDES = ['wp-content', 'articles/drafts']

# clean-url (lacks .html) -- n.b. disqus mapping assumes slug is
# missing .html, would have to redo it if we revert this
ARTICLE_URL = "{slug}"

# have output paths mirror source content's filesystem path hierarchy
# n.b. does not play well with wp-content static path references
#PATH_METADATA = '(?P<path_no_ext>.*)\..*'


# Blogroll
LINKS = (('Home', '/index.html'),
         ('About & Consulting', '/about.html'),
         ('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/efavdb'),
          ('Github', 'https://github.com/efavdb'),
          ('Youtube', 'https://www.youtube.com/channel/UClfvjoSiu0VvWOh5OpnuusA'),)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap',
           'summary',
           'render_math',
           'neighbors',
           'tipue_search',
           'share_post',
]
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

# Theme specific setting
LANDING_PAGE_TITLE = 'EFAVDB'
PROJECTS_TITLE = 'Projects'
PROJECTS = [{'name': 'linselect', 'url': '/pages/linselect.html',
             'description': 'Fast, flexible, performant feature selection package for python'},
            {'name': 'nba predictions', 'url': '/pages/nba-dash.html',
             'description': 'NBA Dashboard'},]


DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
CACHE_CONTENT = False
CACHE_PATH = '.cache'
LOAD_CONTENT_CACHE = False
TYPOGRIFY = True
RECENT_ARTICLE_SUMMARY = False
RESPONSIVE_IMAGES = True


# theme specific settings
# for more settings, see https://github.com/iranzo/blog-o-matic/blob/source/pelicanconf.py
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
RECENT_ARTICLES_COUNT = 5
SHOW_CREDITS = True
SHARE_POST_INTRO = "Like this post?  Share on:"
RELATED_POSTS_LABEL = "Keep reading"

AUTHORS = {
    "Jonathan Landy": {
        "avatar": "/wp-content/uploads/2014/12/JonathanLinkedIn.jpg",
        "blurb": "Jonathan grew up in the midwest and then went to school at Caltech and UCLA. Following this, he did two postdocs, one at UCSB and one at UC Berkeley.  His academic research focused primarily on applications of statistical mechanics, but his professional passion has always been in the mastering, development, and practical application of slick math methods/tools. He worked as a data-scientist at Square for four years and is now working on a quantitative investing startup."
    },
    "Dustin McIntosh": {
        "avatar": "/wp-content/uploads/2014/12/DustinLinkedIn2.png",
        "blurb": "Dustin got a B.S in Engineering Physics from the Colorado School of Mines (Golden, CO) before moving to UC Santa Barbara for graduate school. There he became interested in Soft Condensed Matter Physics and Polymer Physics, studying the interaction between single DNA molecules and salt ions. After a brief postdoc at UC San Diego studying the physics of bacterial growth, Dustin decided to move into the data science business for good - he is now a Quantitative Analyst at Google in Mountain View."
    },
    "Damien RJ": {
        "avatar": "/wp-content/uploads/2014/12/headshot.jpg",
        "blurb": "Damien is a highly experienced researcher with a background in clinical and applied research. Like JSL, he got his PhD at UCLA. He has many years of experience working with imaging, and has a particularly strong background in image segmentation, registration, detection, data analysis, and more recently machine learning. He now works as a data-scientist at Square in San Francisco."
    },
    "Cathy Yeh": {
        "avatar": "/images/cy_efavdb_headshot.jpg",
        "blurb": "Cathy Yeh got a PhD at UC Santa Barbara studying soft-matter/polymer physics. She is currently looking to transition to a career in data science after wrapping up work with the translational modeling group in a pharmaceutical company in San Diego. She enjoys mining big data and big ice cream and seeing how both can help make the world a better place."
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
