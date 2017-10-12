# -*- coding: utf-8 -*-

from functools import wraps


class HttpRouter(object):

    def __init__(self):
        self.routes = {}

    def add_route(self, path, view, method='GET'):
        self.routes[(path, method)] = view

    def route(self, path, method='GET'):
        def decorator(fn):
            self.routes[(path, method)] = fn

            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(*args, **kwargs)
            return wrapper

        return decorator

    def __call__(self, environ, start_response):
        request_uri = environ['REQUEST_URI']
        request_method = environ['REQUEST_METHOD']

        for (path, method), view in self.routes.items():
            if path == request_uri and method == request_method:
                body, status, headers = view()
                if not isinstance(body, bytes):
                    body = bytes(body, 'utf-8')
                start_response(status, list(headers.items()))
                return [body]

        body, status, headers = b'Not found.', '404 Not Found', {}
        start_response(status, list(headers.items()))
        return [body]


application = HttpRouter()


@application.route('/')
def home():
    return 'Ok', '200 OK', {}
