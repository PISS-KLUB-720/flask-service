from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/player", methods=["POST"])
def get_player_data():
    print(request.data)
    return {"position": "right"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
