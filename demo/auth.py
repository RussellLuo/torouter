#!/usr/bin/env python

import tornado.web

from torouter import urls


class MainHandler(tornado.web.RequestHandler):
    pass


class RegisterHandler(tornado.web.RequestHandler):
    pass


class LoginHandler(tornado.web.RequestHandler):
    pass


class LogoutHandler(tornado.web.RequestHandler):
    pass


handlers = urls('',
    (r'/', MainHandler),
    (r'/register', RegisterHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
)
