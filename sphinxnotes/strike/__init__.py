# -*- coding: utf-8 -*-
"""
    sphinxnotes.strike
    ~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2021 Shengyu Zhang.
    :license: BSD, See LICENSE
"""

from __future__ import annotations
from os import path
from typing import List, Dict, Tuple

from docutils import nodes
from docutils.utils import nodes, unescape
from docutils.nodes import Node, system_message, Text
from docutils.parsers.rst.states import Inliner

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.latex import LaTeXBuilder

__title__ = 'sphinxnotes-strike'
__package__ = 'strike'
__author__ = 'Shengyu Zhang'
__description__ = 'Sphinx extension for strikethrough text support'
__license__ = 'BSD'
__version__ = '1.2'
__url__ = 'https://sphinx.silverrainz.me/strike'
__keywords__ = 'documentation, sphinx, extension'


class strike_node(nodes.Inline, nodes.TextElement): pass


def strike_role(typ:str, rawtext:str, text:str, lineno:int,
             inliner:Inliner, options:Dict={}, content:List[str]=[]
             ) -> Tuple[List[Node],List[system_message]]:
    env = inliner.document.settings.env # type: ignore

    if not isinstance(env.app.builder, (StandaloneHTMLBuilder, LaTeXBuilder)):
        # Builder is not supported, fallback to text.
        return [Text(unescape(text))], []

    node = strike_node(rawtext, unescape(text))
    node['docname'] = env.docname
    return [node], []


def html_visit_strike_node(self, node:strike_node) -> None:
    self.body.append(self.starttag(node, 'span', '',
                                   CLASS='sphinxnotes-strike',
                                   STYLE='text-decoration: line-through;'))


def html_depart_strike_node(self, node:strike_node) -> None:
    self.body.append('</span>')


def latext_visit_strike_node(self, node:strike_node) -> None:
    self.body.append(r'\sout{')


def latext_depart_strike_node(self, node:strike_node) -> None:
    self.body.append('}')


def setup(app:Sphinx):
    app.add_latex_package('ulem', 'normalem')

    app.add_node(strike_node,
                 html=(html_visit_strike_node, html_depart_strike_node),
                 latex=(latext_visit_strike_node, latext_depart_strike_node))

    app.add_role('strike', strike_role)
    app.add_role('del', strike_role)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
