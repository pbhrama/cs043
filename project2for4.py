import wsgiref.simple_server
import urllib.parse
from database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    db = Simpledb('dbtest.txt')

    if path == '/insert':
        db.insert(params['key'][0], params['value'][0])
        start_response('200 OK', headers)
        return ['Inserted'.encode()]
    elif path == '/select':
        s = db.select_one(params['key'][0])
        print(s)
        start_response('200 OK', headers)
        if s != None:
            return [s.encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/delete':
        s = db.delete(params['key'][0])
        print(s)
        start_response('200 OK', headers)
        if s:
            return ["Deleted".encode()]
        else:
            return ['NULL'.encode()]
    elif path == '/update':
        s = db.update(params['key'][0], params['value'][0])
        print(s)
        start_response('200 OK', headers)
        if s == None:
            return ["Updated".encode()]
        else:
            return ['NULL'.encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()