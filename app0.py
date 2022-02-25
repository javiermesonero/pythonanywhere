
# PRueba

from flask import Flask

app = Flask(__name__)
#cambios222222
@app.route('/')
def hello_world():
    return 'Hello 3 from Flask!'

#Cambios