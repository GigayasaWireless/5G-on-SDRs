import os
import sys
sys.path.insert(0, os.path.abspath("../../"))
import sphinx_rtd_theme
project = "GW-H5GSDR"
project_copyright = "2024-2026, Gigayasa Wireless Private Limited"
author = "Vikram Singh <toolkit5G@gigayasa.com>"

from importlib.machinery import SourceFileLoader
version = "R23a.0.2"
release = "1"

extensions = ["myst_parser",
              "sphinx.ext.autodoc",
              "sphinx_autodoc_typehints",
              "nbsphinx",
              "sphinx_rtd_theme",
              "sphinx.ext.mathjax",
              "sphinx.ext.intersphinx",
              "sphinx_copybutton",
              "sphinx.ext.viewcode",
              "sphinx.ext.napoleon",
              'sphinxcontrib.rsvgconverter',
              "sphinx.ext.autosectionlabel",
              'sphinx_tabs.tabs']


napoleon_custom_sections = [("Input shape", "params_style"),
                            ("Output shape", "params_style"),
                            ("Attributes", "params_style"),
                            ("Input", "params_style"),
                            ("Output", "params_style"),
                            ("Parameters", "params_style")
                            ]

napoleon_google_docstring = True
napoleon_numpy_docstring = True

numfig = True

# do not re-execute jupyter notebooks when building the docs
nbsphinx_execute = 'never'

autodoc_default_options = {
    "exclude-members": "build"
    }

autodoc_docstring_signature = True


myst_enable_extensions = ["colon_fence", ]

templates_path = ['_templates']
html_static_path = ['_static']

html_logo = "_static/logo28.png"
exclude_patterns = ['build', '**.ipynb_checkpoints']

html_theme = "sphinx_rtd_theme"

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'sticky_navigation': False,
    'navigation_depth': 5,
    'titles_only': False,
    'collapse_navigation': False,
    }

html_show_sourcelink = False
pygments_style = "default"

myst_url_schemes = ["http", "https", ]
numpydoc_show_class_members = False
html_css_files = ['css/gigayasa.css']

# Add a custom prolog to each notebook to automatically add github/colab/download links
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. raw:: html

    <style>h3 {display: block !important}</style>
    <div style="margin-bottom:15px;">
        <table>
            <td style="padding: 0px 0px;">
                <a href="https://www.youtube.com/@gigayasa/videos" style="vertical-align:text-bottom">
                    <img alt="YouTube logo" src="../../../_static/YouTube.svg" style="width: 30px; min-width: 30px">
                </a>
            </td>
            <td style="padding: 2px 4px;">
                <a href="https://www.youtube.com/@gigayasa/videos" style="vertical-align:text-bottom">
                    Watch on YouTube
                </a>
            </td>
            
            <td class="wy-breadcrumbs-aside" style="padding: 0 30px;">
                <a href="https://github.com/GigayasaWireless/toolkit5G/blob/website/{{ docname|e }}" style="vertical-align:text-bottom">
                    <i class="fa fa-github" style="font-size:24px;"></i>
                    View on GitHub
                </a>
            </td>
            
            <td class="wy-breadcrumbs-aside" style="padding: 0 35px;">
                <a href="https://github.com/GigayasaWireless/toolkit5G/raw/website/{{ docname|e }}" download target="_blank" style="vertical-align:text-bottom">
                    <i class="fa fa-download" style="font-size:24px;"></i>
                    Download notebook
                </a>
            </td>
            
            <!--
            <td class="wy-breadcrumbs-aside" style="padding: 0 35px;">
                <a href="https://github.com/GigayasaWireless/toolkit5G/raw/website/{{ env.docname.split('.')|first|e + '.zip'}}" download target="_blank" style="vertical-align:text-bottom">
                    <i class="fa fa-download" style="font-size:24px;"></i>
                    Download notebook
                </a>
            </td>
            -->

        </table>

    </div>
"""

