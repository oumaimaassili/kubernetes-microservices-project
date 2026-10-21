from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(service="api-produits", pod=socket.gethostname(), products=["laptop", "phone", "tablet"])

@app.route("/load")
def load():
    total = 0
    for i in range(3000000):
        total += i * i
    return jsonify(status="charge CPU terminee", pod=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)