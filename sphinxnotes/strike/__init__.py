# -*- coding: utf-8 -*-
"""
    sphinxnotes.strike
    ~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2021 Shengyu Zhang.
    :license: BSD, See LICENSE
"""

from __future__ import annotations
from os import path
from typing import TYPE_CHECKING, List, Dict, Tuple

from docutils import nodes, utils
if TYPE_CHECKING:
    from docutils.nodes import Node, system_message
    from docutils.parsers.rst.states import Inliner

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.config import Config

__title__ = 'sphinxnotes-strike'
__package__ = 'strike'
__author__ = 'Shengyu Zhang'
__description__ = 'Sphinx extension for HTML strikethrough text support'
__license__ = 'BSD'
__version__ = '1.0'
__url__ = 'https://sphinx-notes.github.io/strike'
__keywords__ = 'documentation, sphinx, extension'


class strike_node(nodes.Inline, nodes.TextElement): pass


def strike_role(typ:str, rawtext:str, text:str, lineno:int,
             inliner:Inliner, options:Dict={}, content:List[str]=[]
             ) -> Tuple[List[Node],List[system_message]]:
    node = strike_node(text=utils.unescape(text))
    node['docname'] = inliner.document.settings.env.docname
    node['rawtext'] = rawtext
    return [node], []


def html_visit_strike_node(self, node:strike_node) -> None:
    self.body.append(self.starttag(node, 'span', '', CLASS='sphinxnotes-strike'))


def html_depart_strike_node(self, node:strike_node) -> None:
    self.body.append('</span>')


def on_config_inited(app:Sphinx, cfg:Config) -> None:
    static_path = path.abspath(path.join(path.dirname(__file__), '_static'))
    cfg.html_static_path.append(static_path)
    app.add_css_file('sphinxnotes-strike.css')


def setup(app:Sphinx):
    app.add_node(strike_node,
                 html=(html_visit_strike_node, html_depart_strike_node))
    app.add_role('strike', strike_role)
    app.add_role('del', strike_role)

    # Add static path and include css file
    app.connect("config-inited", on_config_inited)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
