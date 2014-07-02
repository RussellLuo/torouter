#!/usr/bin/env python

from tornado.util import import_object

__version__ = '0.0.1'


def urls(prefix, *args):
    urlspecs = []
    for t in args:
        urlspec = url(*t, prefix=prefix)
        if isinstance(urlspec, list):
            # a list of tuples
            urlspecs.extend(urlspec)
        else:
            # a tuple
            urlspecs.append(urlspec)
    return urlspecs


def url(pattern, handler, kwargs=None, name=None, prefix=''):
    if isinstance(handler, (list, tuple)):
        # For include(...) processing.
        return [
            (pattern + h_pattern, h_handler, h_kwargs, k_name)
            for h_pattern, h_handler, h_kwargs, k_name in handler
        ]
    else:
        if isinstance(handler, basestring):
            if not prefix:
                handler = prefix + '.' + handler
            handler = import_object(handler)
        return (pattern, handler, kwargs, name)


def include(url_list_name):
    return import_object(url_list_name)
