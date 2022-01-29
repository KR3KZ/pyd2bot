#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.tag import Tag
from wdom.document import get_document


class App(Tag):
    tag = 'sci-app'


class H1(Tag):
    tag = 'h1'


class Div(Tag):
    tag = 'div'


def sample_page() -> Tag:
    app = App()
    text = H1(parent=app)
    text.textContent = 'Click!'
    div = Div(parent=app)
    count = 0

    def insert(data):
        nonlocal count
        count += 1
        child = Div()
        child.textContent = 'count {}'.format(str(count))
        if not div.hasChildNodes():
            div.appendChild(child)
        else:
            div.insertBefore(child, div.firstChild)

    text.addEventListener('click', insert)

    page = get_document(app=app)

    return page
