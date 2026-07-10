import pandas as pd
import sqlite3
import requests
import json

def fetch_data_from_api(endpoint):
    print(f"Connecting to data api endpoint: {endpoint}")
    # Simulating API response
    response_data = [
        {"sensor_id": "SN-001", "timestamp": "2026-07-13T12:00:00Z", "temperature": 23.5, "humidity": 45.2},
        {"sensor_id": "SN-002", "timestamp": "2026-07-13T12:00:00Z", "temperature": 21.8, "humidity": 50.1},
        {"sensor_id": "SN-001", "timestamp": "2026-07-13T12:05:00Z", "temperature": 24.1, "humidity": 44.8}
    ]
    return pd.DataFrame(response_data)

def transform_telemetry(df):
    print("Applying data transformations...")
    # Convert timestamps and flag outliers
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["temp_f"] = ((df["temperature"] * 9/5) + 32).round(1)
    df["is_alert"] = df["temperature"] > 24.0
    return df

def load_to_azure_simulated(df):
    print("Loading data into Azure SQL Storage container...")
    # Loading to local sqlite to simulate Azure SQL target
    conn = sqlite3.connect("azure_telemetry_reporting.db")
    df.to_sql("device_telemetry", conn, if_exists="append", index=False)
    conn.close()
    print("  Load completed successfully.")

if __name__ == "__main__":
    df_raw = fetch_data_from_api("https://api.factory-sensors.com/v1/telemetry")
    df_clean = transform_telemetry(df_raw)
    load_to_azure_simulated(df_clean)
