from flask import Flask,jsonify,Response,json
from flask import request
# set : export FLASK_APP=app.py
# how to run : python -m flask run --host=0.0.0.0

app = Flask(__name__)
@app.route('/', methods=['POST'])
def add_entry():
    print("p0")
    content = request.get_json()
    sampleout = json.dumps(content)
    print sampleout
    return Response(json.dumps(content), mimetype='application/json')
