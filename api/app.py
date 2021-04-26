from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/draftool/', methods=['GET'])
def respond():
    name = request.args.get("name", None)

    print(f"got name {name}")

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


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')