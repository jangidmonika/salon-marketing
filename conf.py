import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Salon Marketing Documentation'
copyright = '2024, Your Name'
author = 'Your Name'

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