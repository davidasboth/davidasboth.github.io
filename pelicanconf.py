from datetime import date

CURRENTYEAR = date.today().year

AUTHOR = 'David Asboth'
SITENAME = 'David Asboth - Data Solutions &amp; Consultancy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'files', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Social widget
SOCIAL = (('@davidasboth', 'https://twitter.com/davidasboth'),
          ('davidasboth', 'https://github.com/davidasboth'),
	  ('LinkedIn', 'https://www.linkedin.com/in/david-asboth'))

TWITTER_USERNAME = "davidasboth"

# Use subfolders to categorise posts
USE_FOLDER_AS_CATEGORY = True

PLUGIN_PATHS = ['plugins/pelican-plugins/']
PLUGINS = ['jinja2content', 'render_math', 'pelican.plugins.embed_tweet']

# Pages
PAGE_URL = 'pages/{slug}'
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Articles
HIDE_AUTHORS = True
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Tags and Categories
#CATEGORY_URL = 'category/{slug}'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#TAG_URL = 'tag/{slug}'
#TAG_SAVE_AS = 'tag/{slug}/index.html'
#AUTHOR_SAVE_AS = ''

LOAD_CONTENT_CACHE = False

#MENUITEMS = (
#  ('Home','/'),
#  ('Blog','/blog/'),
#  ('Contact','/contact/')
#)

# Set the theme
THEME = "themes/davidasboth-dot-com"

# enable code highlights in markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            "pygments_style": "rrt",
            "noclasses": False,
            "lineseparator": "<br />"
        },
        'markdown.extensions.extra': {}
    }
}

# Static pages of the website that will be generated
#TEMPLATE_PAGES = {
#    "pages/index.html": "index.html",
#    "pages/404.html": "404.html",
#}