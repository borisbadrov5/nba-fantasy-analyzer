from flask import request, jsonify
from app import app

@app.route('/draftool/', methods=['GET'])
def respond():
    name = request.args.get("name", None)

    response = {}

    if not name:
        response["ERROR"] = "no name found, please send a name."
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    return jsonify(response)

@app.route('/')
def index():
    return "<h1>STATS</h1>"