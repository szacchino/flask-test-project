from flask import Flask, render_template

app = Flask(__name__)

@app.route("/api/dati")
def hello_world():
    lista = [10,30,20,40,50,9,33,22]
    return lista


@app.route("/api/dati2")
def hello_world2():
    lista = {"ciao": "mondo", "hello": "world"}
    return lista


@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    lista = [10,30,20,40,50,9,33,22]
    return render_template('hello.html', param=lista)