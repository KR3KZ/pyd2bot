#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.tag import Tag, H1, Div
from wdom.document import get_document


def sample_page() -> Tag:
    doc = get_document()
    text = H1(parent=doc.body)
    text.textContent = 'Title'
    box = Div(style='width:200px;height:10000px;background-color:red;')
    doc.body.appendChild(box)

    def scroll(data):
        box.scrollBy(100, 100)

    box.addEventListener('click', scroll)

    return doc
