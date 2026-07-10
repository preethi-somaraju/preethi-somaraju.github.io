# Cloud Telemetry ETL Data Pipeline

This project deploys a telemetry collection pipeline that consumes sensor events, transforms values, and loads analytics-ready rows into an **Azure SQL Database**.

## ☁️ Architecture
1.  **Extract**: Python requests queries industrial sensor endpoints.
2.  **Transform**: Pandas reformats metrics, parses datetimes, and flags thermal threshold alerts.
3.  **Load**: Simulates load into cloud DB instances.
