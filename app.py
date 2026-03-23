from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)
conn = get_connection()
cur = conn.cursor()

# Get measurements for a day
@app.route("/measurements")
def measurements():
    location = request.args.get("location")
    date = request.args.get("date")

    cur.execute("""
        SELECT * FROM measurements
        WHERE location_id=%s AND DATE(timestamp)=%s
    """, (location, date))

    return jsonify(cur.fetchall())


# Count measurements
@app.route("/count")
def count():
    location = request.args.get("location")

    cur.execute("""
        SELECT COUNT(*) FROM measurements WHERE location_id=%s
    """, (location,))

    return jsonify(cur.fetchone())


# Average value
@app.route("/average")
def average():
    location = request.args.get("location")
    sensor = request.args.get("sensor")
    date = request.args.get("date")

    cur.execute("""
        SELECT AVG(value)
        FROM measurements
        WHERE location_id=%s AND sensor_id=%s AND DATE(timestamp)=%s
    """, (location, sensor, date))

    return jsonify(cur.fetchone())

if __name__ == "__main__":
    app.run(debug=True)