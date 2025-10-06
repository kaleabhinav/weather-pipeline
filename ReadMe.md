# Weather Data Pipeline

## Overview
This project demonstrates a local weather data ingestion pipeline using **Python**, **PostgreSQL**, and **CSV files**.  
The goal is to build a foundational data engineering pipeline that can later be extended to APIs or cloud storage.

---

## Work Done So Far

### 1. Database Setup
- **What:** Created a PostgreSQL database `weather` with a table `raw_weather`.
- **Why:** Stores structured weather data for further processing and analytics.
- **Expected Output:** Table `raw_weather` with columns: `id, city, temperature, humidity, timestamp`.
- **Actual Output:**  
```
weather=# \dt
             List of tables
 Schema |    Name     | Type  |  Owner
--------+-------------+-------+----------
 public | raw_weather | table | postgres
(1 row)
```


---

### 2. Hardcoded Data Ingestion
- **What:** Inserted sample weather data from a Python list into `raw_weather`.
- **Why:** Verify database connectivity and ingestion logic.
- **Expected Output:** Data inserted with correct timestamps.
- **Actual Output:**
```
weather=# select * from raw_weather;
 id |   city   | temperature | humidity |         timestamp
----+----------+-------------+----------+----------------------------
  1 | New York |        22.5 |       55 | 2025-10-05 23:13:48.68011
  2 | London   |        18.3 |       65 | 2025-10-05 23:13:48.947163
  3 | Toyko    |          25 |       70 | 2025-10-05 23:13:48.948166
  4 | New York |        22.5 |       55 | 2025-10-06 00:20:21.933257
  5 | London   |        18.3 |       65 | 2025-10-06 00:20:21.944783
(5 rows)
```

---

### 3. CSV File Ingestion
- **What:** Read weather data from a CSV file (`sample_data/weather_data.csv`) and inserted it into `raw_weather`.
- **Why:** Demonstrates scalable ingestion from external sources rather than hardcoding.
- **Expected Output:** All rows from the CSV are added to the database with timestamps.
- **Actual Output:** Logs show the number of rows read and successful ingestion.
```
2025-10-06 22:54:56,906 - INFO - Read 5 rows from D:\JOB\personal_project\weather_pipeline\sample_data\weather_data.csv
2025-10-06 22:54:57,278 - INFO - CSV data ingested successfully!
```

### 4. Logging
- **What:** Logging implemented to track ingestion steps and errors.  
- **Why:** Provides transparency and debugging support for data ingestion processes.  
- **Actual Output:** `logs/file_ingest.log` contains detailed logs of ingestion attempts and successes.


## Next Steps

- Ingest data from external APIs (e.g., OpenWeather API).  
- Implement cloud storage or cloud database (AWS/GCP/Azure).  
- Add data validation and transformation steps.

---

## Local Setup Instructions

1. Install **PostgreSQL** locally or via Docker.  
2. Create a database called `weather` with table `raw_weather`.  
3. Set up Python virtual environment and install dependencies:
   ```
   bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install psycopg2-binary sqlalchemy pandas (requirements.txt)
   ```