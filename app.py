from flask import Flask, jsonify
import psycopg2
import os
import json

app = Flask(__name__)

DB_CONFIG = {
    "host": "80.85.241.153",
    "database": "rfad",
    "user": "stark",
    "password": "stark6640"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@app.route("/getAll", methods=["GET"])
def get_getAll():
    result = {}
    result['blessings'] =  get_blessings()
    result['races'] = get_races()
    result['stones'] = get_stones()
    
    return jsonify(json.dumps(result, ensure_ascii=False))

def get_blessings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM blessings;")
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "bonuses": row[2]
        })

    cur.close()
    conn.close()
    return result

@app.route("/blessings", methods=["GET"])
def get_blessings_route():
    result = get_blessings()
    return jsonify(json.dumps(result, ensure_ascii=False))

def get_races():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM races;")
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "hp": row[2],
            "mp": row[3],
            "stamina": row[4],
            "hp_regen": row[5],
            "stamina_regen": row[6],
            "mp_regen": row[7],
            "weight": row[8],
            "unarmed_damage": row[9],
            "traits": row[10],
            "skills": row[11],
        })

    cur.close()
    conn.close()
    return result

@app.route("/races", methods=["GET"])
def get_races_route():
    result = get_races()

    return jsonify(json.dumps(result, ensure_ascii=False))

def get_stones():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM stones;")
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "effects": row[3]
        })

    cur.close()
    conn.close()
    return result

@app.route("/stones", methods=["GET"])
def get_stones_route():
    result = get_stones()

    return jsonify(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
