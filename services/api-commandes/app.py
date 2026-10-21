from flask import Flask, jsonify
import socket, os, json
from urllib.request import urlopen

app = Flask(__name__)
PRODUCT_URL = os.environ.get("PRODUCT_URL", "http://api-produits")

@app.route("/")
def home():
    try:
        with urlopen(PRODUCT_URL, timeout=3) as r:
            products = json.loads(r.read())
    except Exception as e:
        return jsonify(service="api-commandes", error=str(e)), 503
    return jsonify(service="api-commandes", pod=socket.gethostname(), reponse_produits=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)