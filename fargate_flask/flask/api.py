import requests

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Success'


@app.route('/health')
def health():
    return 'Yes'


@app.route('/reverse/<string>')
def reverse(string):
    return string[::-1]


@app.route('/es')
def es():
    r = requests.get(
        'http://vpc-rna-expression-dro56qntagtgmls6suff2m7nza.us-west-2.es.amazonaws.com:80'
    )
    return jsonify(r.json())


if __name__ == '__main__':
    app.run()
