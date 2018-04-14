from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/bye")
def bye_world():
    return "Bye World!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"


@app.route("/list_of_numbers")
def list_of_numbers():
    return jsonify(list(range(10)))


@app.route("/get_object")
def get_object():
    return jsonify(create_object())


@app.route("/get_list_of_objects/<num>")
def get_list_of_objects(num):
    return jsonify(create_list_of_objects(int(num)))


def create_list_of_objects(num: int):
    """Create a list of objects"""
    xs = list(range(num))
    ys = list(map(create_object, xs))
    return ys

def create_object(x: int):
    """create a single object"""
    return {
        "name": "Dennis",
        "age": x,
        "lucky_numbers": [1, 2, 3, 4]
    }


if __name__ == "__main__":
    app.run(debug=True)


def main():
    """Launch Flask"""
    app.run()