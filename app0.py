

from flask import Flask

app = Flask(__name__)

#CAMBIOS

@app.route('/')
def hello_world():
    return 'Hello 3 from Flask!'


