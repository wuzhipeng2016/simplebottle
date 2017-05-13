from simplebottle import *

@route('/hello')
def hello():
    return "hello world"

run(port=8080)

