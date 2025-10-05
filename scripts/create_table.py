import logging
import psycopg2

logging.basicConfig(
    filename='logs/db_setup.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
                    )

try:

    conn = psycopg2.connect(
        host = "localhost",
        database = 'weather',
        user = "postgres",
        password = 'postgres'
        )
    
    cur = conn.cursor()

    cur.execute("""
CREATE TABLE IF NOT EXISTS raw_weather (
                id SERIAL PRIMARY KEY,
                city VARCHAR(50),
                temperature FLOAT,
                humidity FLOAT,
                timestamp TIMESTAMP
                )
""")
    
    conn.commit()
    logging.info("Table 'raw_weather' created successfully")

except Exception as e:
    logging.error(f"Error creating table: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
        