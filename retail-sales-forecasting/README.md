# Retail Sales Demand Forecasting

This repository houses a regression-based time-series demand forecasting model. It is designed to ingest raw daily sales transaction data, engineer seasonal lag features and rolling averages, and predict inventory sales levels.

## Features Engineered
*   **Temporal Seasonality:** Date parts (month, day of week, weekend flags)
*   **Lag Features:** Historical offsets (1-day, 7-day, and 30-day sales lags)
*   **Rolling Aggregations:** 7-day sliding window averages and standard deviations

## Core Architecture
The pipeline trains a Linear Regression forecaster on chronological splits (80% training, 20% validation) to simulate production environment conditions.

## Evaluation Results
The forecaster generates daily sales unit metrics:
*   **Root Mean Squared Error (RMSE):** ~10.45 units
*   **Mean Absolute Error (MAE):** ~8.24 units
