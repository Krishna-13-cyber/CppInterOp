# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CppInterOp'
copyright = '2023, Vassil Vassilev'
author = 'Vassil Vassilev'
release = 'Dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    "github_user": "vgvassilev",
    "github_repo": "CppInterOp",
    "github_banner": True,
    "fixed_sidebar": True,
}

highlight_language = "C++"

todo_include_todos = True

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# Add latex physics package
mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {"packages": {"[+]": ["physics"]}},
}
import os

current_file_dir = os.path.dirname(os.path.realpath(__file__))
INTEROP_ROOT = '..' + current_file_dir

# html_extra_path = [INTEROP_ROOT + '/build/docs/doxygen/html']

import subprocess
command = 'mkdir {0}/build; cd {0}/build; cmake ../ -DClang_DIR=/usr/lib/llvm-10/lib/cmake/clang\
         -DLLVM_DIR=/usr/lib/llvm-10 -DINTEROP_ENABLE_DOXYGEN=ON\
         -DINTEROP_INCLUDE_DOCS=ON'.format(INTEROP_ROOT)
subprocess.call(command, shell=True)
subprocess.call('doxygen {0}/build/docs/doxygen.cfg'.format(INTEROP_ROOT), shell=True)