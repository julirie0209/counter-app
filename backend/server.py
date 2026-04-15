from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
from pathlib import Path

app = Flask(__name__)
CORS(app)

DB_PATH = Path(__file__).parent / "counter.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS counter (
            id INTEGER PRIMARY KEY,
            value INTEGER NOT NULL
        )
    """)

    cursor.execute("SELECT value FROM counter WHERE id = 1")
    row = cursor.fetchone()

    if row is None:
        cursor.execute("INSERT INTO counter (id, value) VALUES (1, 0)")

    conn.commit()
    conn.close()


def get_counter_value():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM counter WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row["value"]


def set_counter_value(new_value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE counter SET value = ? WHERE id = 1", (new_value,))
    conn.commit()
    conn.close()
    return new_value


@app.route("/api/counter", methods=["GET"])
def get_counter():
    return jsonify({"count": get_counter_value()})


@app.route("/api/counter/increment", methods=["POST"])
def increment_counter():
    current_value = get_counter_value()
    new_value = current_value + 1
    set_counter_value(new_value)
    return jsonify({"count": new_value})


@app.route("/api/counter/decrement", methods=["POST"])
def decrement_counter():
    current_value = get_counter_value()
    new_value = current_value - 1
    set_counter_value(new_value)
    return jsonify({"count": new_value})


@app.route("/api/counter/reset", methods=["POST"])
def reset_counter():
    set_counter_value(0)
    return jsonify({"count": 0})


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)