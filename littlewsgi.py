'''https://docs.python.org/3.5/library/wsgiref.html'''
def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

class Upperware:
   def __init__(self, app):
      self.wrapped_app = app

   def __call__(self, environ, start_response):
      for data in self.wrapped_app(environ, start_response):
         return data.upper()

from wsgiref.simple_server import make_server
wrapped_app = Upperware(simple_app)
httpd = make_server('localhost', 8051, wrapped_app)
httpd.serve_forever()

