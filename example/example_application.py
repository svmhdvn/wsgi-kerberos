#!/usr/bin/env python3

import logging
from wsgiref.simple_server import make_server

from wsgi_kerberos import KerberosAuthMiddleware


def example(environ, start_response):
    user = environ.get('REMOTE_USER', 'ANONYMOUS')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    data = f"Hello {user}"
    return [data.encode()]


application = KerberosAuthMiddleware(example)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    server = make_server('', 8080, application)
    server.serve_forever()
