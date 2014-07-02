#!/usr/bin/env python

import tornado.web

from torouter import urls, include


class IndexHandler(tornado.web.RequestHandler):
    pass


handlers = urls('',
    (r'/', IndexHandler),
    (r'/auth', include('auth.handlers')),
)


if __name__ == '__main__':
    from pprint import pprint
    pprint(handlers)
