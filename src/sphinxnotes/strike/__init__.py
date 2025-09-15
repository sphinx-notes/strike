# -*- coding: utf-8 -*-
"""
sphinxnotes.strike
~~~~~~~~~~~~~~~~~~

:copyright: Copyright 2021 Shengyu Zhang.
:license: BSD, See LICENSE
"""

from __future__ import annotations
from typing import List, Dict, Tuple

from docutils import nodes
from docutils.utils import unescape
from docutils.nodes import Node, system_message, Text
from docutils.parsers.rst.states import Inliner

from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.builders.latex import LaTeXBuilder

from . import meta


# List of all builders that support render :class:`strike_node`.
SUPPORTED_BUILDERS: list[type[Builder]] = [StandaloneHTMLBuilder, LaTeXBuilder]

class strike_node(nodes.Inline, nodes.TextElement):
    pass


def strike_role(
    typ: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Dict = {},
    content: List[str] = [],
) -> Tuple[List[Node], List[system_message]]:
    env = inliner.document.settings.env  # type: ignore

    if not isinstance(env.app.builder, tuple(SUPPORTED_BUILDERS)):
        # Builder is not supported, fallback to text.
        return [Text(unescape(text))], []

    node = strike_node(rawtext, unescape(text))
    node['docname'] = env.docname
    return [node], []


def html_visit_strike_node(self, node: strike_node) -> None:
    self.body.append(
        self.starttag(
            node,
            'span',
            '',
            CLASS='sphinxnotes-strike',
            STYLE='text-decoration: line-through;',
        )
    )


def html_depart_strike_node(self, node: strike_node) -> None:
    self.body.append('</span>')


def latext_visit_strike_node(self, node: strike_node) -> None:
    self.body.append(r'\sout{')


def latext_depart_strike_node(self, node: strike_node) -> None:
    self.body.append('}')


def setup(app: Sphinx):
    """Sphinx extension entrypoint."""
    meta.pre_setup(app)

    app.add_latex_package('ulem', 'normalem')

    app.add_node(
        strike_node,
        html=(html_visit_strike_node, html_depart_strike_node),
        latex=(latext_visit_strike_node, latext_depart_strike_node),
    )

    app.add_role('strike', strike_role)
    app.add_role('del', strike_role)

    return meta.post_setup(app)
