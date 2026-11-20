import sqlite3

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    return "ok"


@app.route("/users", methods=["POST"])
def find_user():
    name = request.json["name"]
    cur = sqlite3.connect("app.db").cursor()
    cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return jsonify(cur.fetchall())


if __name__ == "__main__":
    app.run(debug=True)
