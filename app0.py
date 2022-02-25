
#Hola
from flask import Flask

app = Flask(__name__)


#CAMBIOS 123456789
#CAMBIOS 123456

@app.route('/')
def hello_world():
    return 'Hello 3 from Flask!'


