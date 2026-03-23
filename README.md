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


## Testing and Execution

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
