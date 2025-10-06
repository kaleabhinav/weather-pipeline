# Weather Pipeline

A Python + PostgreSQL pipeline for ingesting weather data
This project demonstrats the basics of a **data engineering workflow** (ingestion, logging and databse interaction)

---
## Work Done, Expected Output, Actual Output and WHY

| Step | Work Done | Expected Output | Actual Output | Why |
|-|-|-|-|-|
|1| Setup PostgreSQL database using Docker | PostgreSQL container running, database `weather` created | Docket container `weather-postgres` running, `weather` DB created | Docker ensures a **reproducible local environemnet** for the database|
|2| Create table  `raw_weather` | Table with columns: `id`, `city`, `temperature`, `humidity` and `timestamp` | Table created successfully | Defines the **schema for weather data ingestion** |
| 3 | Ingested hardcoded weather data | Rows inserted into `raw_weather` | 3 rows inserted (New York, London, Tokyo) | Demonstrates **end-to-end data flow** from Python → PostgreSQL |
| 4 | Added logging | Log file `logs/ingest.log` with successful ingestion messages | Log file created with entries like: `Weather data ingested successfully` | Logging **tracks pipeline execution and errors**, useful for debugging |
| 5 | Verified data in database | Able to query `raw_weather` and see inserted rows | Query shows 3 rows with timestamps | Confirms that **data ingestion worked as intended** |
| 6 | Prepared virtual environment & installed dependencies | Isolated Python environment with `psycopg2-binary`, `pandas`, `sqlalchemy` installed | Dependencies installed and importable in Python | Ensures **reproducibility and package management** |


---

## Next Steps (Future Work)

1. Replace hardcoded data with **CSV or API ingestion**.
2. Add **transformations** before inserting data.
3. Schedule pipeline to run automatically using **Airflow / Cron**.
4. Extend logging to **track individual row insertions and errors**.