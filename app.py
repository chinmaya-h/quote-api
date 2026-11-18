from random import choice

from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = [
    "It always seems impossible until it's done.",
    "Great things are done by a series of small things brought together.",
    "The secret of getting ahead is getting started.",
]


@app.get("/quote")
def random_quote():
    return jsonify({"quote": choice(QUOTES)})


@app.get("/quotes")
def all_quotes():
    return jsonify(QUOTES)


@app.get("/health")
def health():
    return jsonify({"status": "UP"})
    
@app.get("/")
def home():
    return jsonify({"app": "Quote API", "status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
