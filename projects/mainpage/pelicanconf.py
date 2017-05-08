#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'raa'
SITENAME = 'Sicherheitshinweise - PodCast zur EDV-Sicherheit'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['../../plugins']
PLUGINS = ['pelican-podcast-feed',]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('raise an issue', '#'),
         ('pad', 'https://sicherheitshinweise.pads.ccc.de/'),)

# Social widget
SOCIAL = (('plushkatze', 'https://github.com/plushkatze'),
          ('raa', 'https://github.com/rickmer'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-simplegrey'

PODCAST_FEED_PATH = 'podcast.xml'
PODCAST_FEED_LANGUAGE = 'de'
PODCAST_FEED_COPYRIGHT = 'http://creativecommons.org/licenses/by-sa/4.0/'
PODCAST_FEED_EXPLICIT = 'Yes'
PODCAST_FEED_TITLE = 'Sicherheitshinweise'
PODCAST_FEED_SUBTITLE = 'PodCast zur EDV Sicherheit'
PODCAST_FEED_AUTHOR = 'plushkatze, raa'
PODCAST_FEED_SUMMARY = ''
PODCAST_FEED_IMAGE= 'http://imga.ge/file.jpg'
PODCAST_FEED_OWNER_NAME = ''
PODCAST_FEED_OWNER_EMAIL = ''
PODCAST_FEED_CATEGORY = ['category1','cat2']

