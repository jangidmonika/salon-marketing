import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Salon Marketing Documentation'
copyright = '2024, Monika Jangid'
author = 'Monika Jangid'

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable automatic rebuild on file changes
watchdog_events = ['modified', 'created', 'deleted']
watchdog_patterns = ['*.md', '*.rst']

# GitHub Pages specific settings
html_baseurl = 'https://jangidmonika.github.io/salon-marketing/'
html_theme_options = {
    'analytics_id': 'G-XXXXXXXXXX',  # Add your Google Analytics ID if needed
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
} 