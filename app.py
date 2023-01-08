from flask import Flask, request
from random import choice;

app = Flask(__name__)

outcomes = ["left", "right", "center", "out"]

def ml_stub_predict(data):
    return choice(outcomes)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/player", methods=["POST"])
def get_player_data():
    print(request.data)
    return {"position": ml_stub_predict(request.data)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
