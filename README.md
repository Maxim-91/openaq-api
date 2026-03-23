This project is a REST API built with Flask to access air quality data stored in PostgreSQL.

## Testing in the browser
When the application is running: *Running on http://127.0.0.1:5000*

### 1. Measurements for one day at the selected location
example of a link for day: location_id=2975, date=2023-01-01
http://127.0.0.1:5000/measurements/day?location_id=2975&date=2023-01-01
<img width="609" height="500" alt="DailyData" src="https://github.com/user-attachments/assets/e18a5033-9b36-4f4e-b54c-72feeab0d341" />

### 2. The number of all measurements at the selected measurement location
example of a link for count: location_id=2975
http://127.0.0.1:5000/measurements/count?location_id=2975
<img width="505" height="139" alt="Count" src="https://github.com/user-attachments/assets/7735f843-5276-4424-b6f2-a8a4eea3f301" />

### 3. Daily average value for the selected measurement location and sensor
example of a link for average: location_id=2975, sensor=pm10, date=2023-01-01
http://127.0.0.1:5000/measurements/average?location_id=2975&sensor=pm10&date=2023-01-01
<img width="732" height="176" alt="Average" src="https://github.com/user-attachments/assets/b0b9b12d-673e-4815-b128-72a737288da6" />

---

### This work is a continuation from
[**Maxim-91/openaq-ingestion**](https://github.com/Maxim-91/openaq-ingestion)

---

## Database EER Diagram (MySQL Workbench)
<img width="533" height="431" alt="Model_MySQL_Workbench" src="https://github.com/user-attachments/assets/13dfc683-f9a4-45b6-b2ad-1229e0a0f604" />


The database (DB) utilizes a relational schema to manage air quality data:

* **locations**: Stores monitoring station metadata including name, city, and country.
* **sensors**: A lookup table for unique pollutant types (e.g., PM2.5, NO2).
* **measurements**: The central fact table linking locations and sensors to specific values and timestamps.

**Relationships**: Both the `locations` and `sensors` tables have **1:N non-identifying relationships** linked to the `measurements` table, ensuring data integrity while maintaining independent primary keys for each record.

## Database Schema (PostgreSQL)

The DB is designed to store air quality data from the OpenAQ API. It follows a relational model to ensure data integrity and efficient querying of historical records.

```sql
-- Table for monitoring stations (uses ID from OpenAQ API)
CREATE TABLE locations (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);

-- Table for sensor types (e.g., pm25, co, no2)
CREATE TABLE sensors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Table for historical measurement data
CREATE TABLE measurements (
    id SERIAL PRIMARY KEY,
    location_id INT NOT NULL,
    sensor_id INT NOT NULL,
    value FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,

    -- Relationships
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (sensor_id) REFERENCES sensors(id)
);
```

## requirements.txt

To install the required dependencies using the `requirements.txt` file, run the following command in the PyCharm terminal (**ensure your `.venv` is active**):

```bash
pip install -r requirements.txt
```

---

## AI Disclosure & Credits

This project was developed with the assistance of AI tools.

### **ChatGPT was used for:**
* understanding project requirements;
* explaining Python segments and generating the initial structure for `app.py`;
* debugging issues.

### **Source Code & Originality:**
* for `app.py`, the code examples were taken from the *"Postgres"* training material;
* all code was reviewed, refined, and tested to ensure functionality;
* the DB design and EER diagrams were created independently as part of the course assignment.

---
