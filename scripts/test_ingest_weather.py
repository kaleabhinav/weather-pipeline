import logging
import psycopg2
import pandas as pd
from datetime import datetime

logging.basicConfig(
    filename= 'logs/test_ingest.log',
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

data = [
    {"city" : "New York", "temperature": 22.5, "humidity":55},
    {"city":"London", "temperature":18.3, "humidity": 65},
    {"city":"Toyko", "temperature": 25.0,"humidity":70}
]

try:
    conn = psycopg2.connect(
        host = "localhost",
        database = "weather",
        user = "postgres",
        password = "postgres"
    )

    cur = conn.cursor()
    

    cur.execute("""
    ALTER TABLE raw_weather
    ADD COLUMN IF NOT EXISTS timestamp TIMESTAMP DEFAULT NOW();
""")
    for row in data:
        cur.execute(
            """
INSERT INTO raw_weather (city, temperature, humidity, timestamp)
VALUES (%s,%s,%s,%s)
            """,
            (row['city'], row['temperature'], row['humidity'], datetime.now())
        )

    conn.commit()
    logging.info("Weather data ingested successfully !!!!")

except Exception as e:
    logging.error(f"Error ingesting data: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()