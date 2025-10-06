import logging
import psycopg2
import pandas as pd
from datetime import datetime

logging.basicConfig(
    filename= "logs/file_ingest.log",
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CSV_FILE = 'D:\JOB\personal_project\weather_pipeline\sample_data\weather_data.csv'

try:

    df = pd.read_csv(CSV_FILE)

    logging.info(f"Read {len(df)} rows from {CSV_FILE}")

    conn = psycopg2.connect(
        host = 'localhost',
        database = 'weather',
        user = "postgres",
        password = "postgres"
    )
    
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
        INSERT INTO raw_weather (city, temperature, humidity, timestamp)
                    VALUES (%s,%s,%s,%s)
""",
(row['city'], row['temperature'], row['humidity'],datetime.now()))
        
        conn.commit()
    logging.info("CSV data ingested successfully!")

except Exception as e:
    logging.error(f"Error Ingesting date from file: {e}")

finally:

    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()