from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

# 1. Get measurements for a specific day
@app.route("/measurements/day", methods=["GET"])
def get_measurements_by_day():
    location_id = request.args.get("location_id")
    date = request.args.get("date")  # format: YYYY-MM-DD

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT m.value, m.timestamp, s.name
        FROM measurements m
        JOIN sensors s ON m.sensor_id = s.id
        WHERE m.location_id = %s
        AND DATE(m.timestamp) = %s
    """

    cur.execute(query, (location_id, date))
    rows = cur.fetchall()

    result = []
    for row in rows:
        result.append({
            "value": row[0],
            "timestamp": row[1],
            "sensor": row[2]
        })

    cur.close()
    conn.close()

    return jsonify(result)


# 2. Count measurements
@app.route("/measurements/count", methods=["GET"])
def get_measurements_count():
    location_id = request.args.get("location_id")

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT COUNT(*)
        FROM measurements
        WHERE location_id = %s
    """

    cur.execute(query, (location_id,))
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify({"count": count})


# 3. Average value per day (by sensor)
@app.route("/measurements/average", methods=["GET"])
def get_average():
    location_id = request.args.get("location_id")
    sensor_name = request.args.get("sensor")
    date = request.args.get("date")

    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT AVG(m.value)
        FROM measurements m
        JOIN sensors s ON m.sensor_id = s.id
        WHERE m.location_id = %s
        AND s.name = %s
        AND DATE(m.timestamp) = %s
    """

    cur.execute(query, (location_id, sensor_name, date))
    avg = cur.fetchone()[0]

    cur.close()
    conn.close()

    return jsonify({
        "location_id": location_id,
        "sensor": sensor_name,
        "date": date,
        "average": avg
    })


if __name__ == "__main__":
    app.run(debug=True)
