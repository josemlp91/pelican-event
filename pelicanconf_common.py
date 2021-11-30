#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pelicanconf_flags import *

AUTHOR = 'Python España Org'
SITENAME = 'PyConES 2022 GRX'
PATH = 'content'
THEME = "theme"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", "assets",]

IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False
IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output')), ('h2', ('id', 'Header-2'))]
IPYNB_GENERATE_SUMMARY = True


DIRECT_TEMPLATES = ['index', 'blog', 'keynoters', 'sponsorship', 'schedule']
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

DEFAULT_PAGINATION = False

# Theme config
MENUITEMS_NAVBAR = [
    ("La ciudad", "/pages/granada.html"),
    ("Código de conducta", "/pages/code-of-conduct.html"),
    ("Organizadores", "/pages/organizers.html")
]

if ENABLED_SPEAKERS:
    MENUITEMS_NAVBAR.append(tuple(("Ponentes", "/keynoters.html")))

if ENABLED_SPONSORSHIPS:
    MENUITEMS_NAVBAR.append(tuple(("Patrocinadores", "/sponsorship.html")))

if ENABLED_SCHEDULE:
    MENUITEMS_NAVBAR.append(tuple(("Horario", "/schedule.html")))

if ENABLED_BLOG:
    MENUITEMS_NAVBAR.append(tuple(("Blog", "/blog.html")))

NAVBAR_STYLE = "is-primary"
THEME_LOGO = "/theme/images/logo_grande.svg"
FOOTER= "Copyright © Python España & PyConES 2022 Org"
