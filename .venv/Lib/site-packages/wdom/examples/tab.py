#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wdom.document import get_document
from wdom.tag import Div, Style


style = '''
body {
    color: #333;
}
'''


class TabButton(Div):
    def activate(self) -> None:
        self.addClass('tab-active')

    def deactivate(self) -> None:
        self.removeClass('tab-active')


class TabNav(Div):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


def sample_app(**kwargs) -> Div:
    doc = get_document()
    css = Style(style)
    doc.head.append(css)
    app = Div('hello')
    return app


if __name__ == '__main__':
    from wdom.document import set_app
    from wdom import server
    set_app(sample_app())
    server.start()
