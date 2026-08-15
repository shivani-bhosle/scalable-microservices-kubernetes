from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Product Service is running!"


@app.route("/products")
def products():
    return {
        "service": "Product Service",
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Mobile"},
            {"id": 3, "name": "Keyboard"}
        ]
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
