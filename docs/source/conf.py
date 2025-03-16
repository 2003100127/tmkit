# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TMKit'
copyright = '2024, Jianfeng Sun'
author = 'Jianfeng Sun'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
]
myst_enable_extensions = ["colon_fence"]

# source_suffix = {
#     ".rst": "restructuredtext",
#     ".md": "markdown",
# }

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'pydata_sphinx_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']


html_theme_options = {
    "show_navbar_depth": 1, # 3
    "collapse_navigation": True, # False
    "show_prev_next": True,
    "use_edit_page_button": False,

    "repository_url": "https://github.com/2003100127/tmkit",
    "use_repository_button": True,


    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/2003100127?tab=repositories",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?hl=en&user=TfLBR9kAAAAJ&view_op=list_works&sortby=pubdate",
            "icon": "fa-brands fa-google-scholar",
            "type": "fontawesome",
        },
        {
            "name": "Twitter",
            "url": "https://x.com/Jianfeng_Sunny",
            "icon": "fa-brands fa-square-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/jianfeng-sun-2ba9b1132/",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}

html_logo = "img/tmkit_logo.png"

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
    ]
}



# html_theme_options = {
#     "show_prev_next": False,  # Hide previous/next buttons at bottom
#     "show_toc_level": 2,  # Number of heading levels shown in the right TOC
#     "navigation_depth": 3,  # Sidebar depth (how many subheadings appear)
#     "collapse_navigation": False,  # Keep all levels expanded
#     "sticky_navigation": True,  # Keep the sidebar visible when scrolling
#     "navigation_with_keys": True,  # Enable keyboard navigation for sidebar
#     "use_edit_page_button": True,  # Enable edit button for GitHub
#     "header_links_before_dropdown": 5,  # Number of links before "More" menu
# }
# html_sidebars = {
#     "**": [
#         "search-field.html",  # Search bar at the top
#         "sidebar-nav-bs.html",  # Main sidebar navigation (like Scanpy)
#         "sidebar-ethical-ads.html",  # Optional: Ads or extra content
#     ]
# }
