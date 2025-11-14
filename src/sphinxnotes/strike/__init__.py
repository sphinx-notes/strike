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
from sphinx.util import logging
from sphinx.environment import BuildEnvironment

from . import meta

logger = logging.getLogger(__name__)

# NOTE: DEPRECATED since 1.3, DO NOT use it.
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
    env: BuildEnvironment = inliner.document.settings.env  # type: ignore
    builder = env.app.builder

    if not _is_supported_builder(builder):
        logger.warning(
            f'role {typ} is not supported for builder {builder.name}, fallback to text',
            location=(env.docname, lineno),
            type='strike',
            subtype='unspported_builder',
        )
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


def _is_supported_builder(builder: Builder) -> bool:
    if isinstance(builder, tuple(SUPPORTED_BUILDERS)):
        return True  # NOTE: Compatible with version 1.2.

    # a dict of builder name -> dict of node name -> visitor and departure functions
    handlers = builder.app.registry.translation_handlers[builder.name]
    return handlers.get(strike_node.__name__) is not None


def setup(app: Sphinx):
    """Sphinx extension entrypoint."""
    meta.pre_setup(app)

    latex_packages = ('ulem', 'normalem')
    for latex_package in latex_packages:
        # If the package is already added and we add it again, Sphinx will warn.
        if not app.registry.has_latex_package(latex_package):
            app.add_latex_package(latex_package)

    app.add_node(
        strike_node,
        html=(html_visit_strike_node, html_depart_strike_node),
        latex=(latext_visit_strike_node, latext_depart_strike_node),
    )

    app.add_role('strike', strike_role)
    app.add_role('del', strike_role)

    return meta.post_setup(app)
