import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="air_quality",
        user="postgres",
        password="12345",
        host="localhost"
    )