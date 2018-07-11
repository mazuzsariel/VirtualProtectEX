from flask import json,Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    response = app.response_class(
    response=json.dumps(open("table.txt",'r').read()),
        status=200,
        mimetype='application/json'
    )
    return response


