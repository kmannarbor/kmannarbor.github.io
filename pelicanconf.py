#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Mendiola'
SITENAME = 'Alex Mendiola: Coder'
SITEURL = ''

PATH = 'content'
THEME = 'notmyidea'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'), 
    ('Code with Mosh', 'https://codewithmosh.com/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/kmannarbor'), 
    ('Linkedin', 'https://www.linkedin.com/in/alexmendiola/'), 
    ('Youtube', 'https://www.youtube.com/channel/UCWqk6iBabEXpEQqNSY3BdSw'), )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True