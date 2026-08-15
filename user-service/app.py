from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "User Service is running!"


@app.route("/users")
def users():
    return {
        "service": "User Service",
        "users": ["Shivani", "Rahul", "Priya"]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
