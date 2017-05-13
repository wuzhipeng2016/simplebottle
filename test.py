from simplebottle import *

@route('/hello')
def hello():
    return "hello world"
@route('/hello/<name>')
def hello2(name):
    return template('Hello {{name}}, how are you?', name=name)

run(port=8080,debug=True)

