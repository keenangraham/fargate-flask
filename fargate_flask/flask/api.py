from flask  import Flask


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


if __name__ == '__main__':
    app.run()
