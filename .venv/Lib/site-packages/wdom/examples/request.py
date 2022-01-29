#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.tag import Tag, H1, Button
from wdom.document import get_document


def sample_page() -> Tag:
    doc = get_document()
    text = H1(parent=doc.body)
    text.textContent = 'Title!'
    btn = Button('click!', parent=doc.body)

    def get_rect(data):
        print('send query')

        def show_rect(fut):
            print('DONE')
            print(fut.result())
        fut = text.getBoundingClientRect()
        fut.add_done_callback(show_rect)
        print(fut)

    btn.addEventListener('click', get_rect)

    return doc
