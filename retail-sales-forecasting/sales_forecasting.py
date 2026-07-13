import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

def generate_mock_sales_data(days=365):
    """Generates synthetic daily sales transaction data with weekly seasonality and upward trend."""
    np.random.seed(42)
    date_range = pd.date_range(start="2025-01-01", periods=days, freq="D")
    
    # Components: Trend, Seasonality, Noise
    trend = 0.5 * np.arange(days) + 100
    weekly_seasonality = 20 * np.sin(2 * np.pi * date_range.dayofweek / 7)
    noise = np.random.normal(scale=10, size=days)
    
    sales = trend + weekly_seasonality + noise
    df = pd.DataFrame({"date": date_range, "sales": sales})
    return df

def engineer_time_series_features(df):
    """Engineers lag features and rolling stats for forecasting demand."""
    df = df.copy()
    
    # Date parts
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Lag features
    df['sales_lag_1'] = df['sales'].shift(1)
    df['sales_lag_7'] = df['sales'].shift(7)
    df['sales_lag_30'] = df['sales'].shift(30)
    
    # Rolling averages
    df['sales_roll_mean_7'] = df['sales'].shift(1).rolling(window=7).mean()
    df['sales_roll_std_7'] = df['sales'].shift(1).rolling(window=7).std()
    
    # Drop rows with NaN (due to shifts/rolling)
    df = df.dropna().reset_index(drop=True)
    return df

def train_forecaster():
    print("Initializing Time Series Demand Forecaster...")
    
    # 1. Generate & Load Data
    raw_df = generate_mock_sales_data(days=365)
    processed_df = engineer_time_series_features(raw_df)
    
    # 2. Split into Train & Test (80% train, 20% test chronologically)
    split_idx = int(len(processed_df) * 0.8)
    train_df = processed_df.iloc[:split_idx]
    test_df = processed_df.iloc[split_idx:]
    
    # Features & Targets
    features = ['day_of_week', 'month', 'is_weekend', 'sales_lag_1', 'sales_lag_7', 'sales_roll_mean_7']
    target = 'sales'
    
    X_train, y_train = train_df[features], train_df[target]
    X_test, y_test = test_df[features], test_df[target]
    
    # 3. Model Training
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. Forecast & Evaluation
    predictions = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    mae = mean_absolute_error(y_test, predictions)
    
    print("\n==========================================")
    print("           MODEL PERFORMANCE METRICS")
    print("==========================================")
    print(f"Target Variable: Daily Sales Units")
    print(f"Features Used: {', '.join(features)}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print("==========================================\n")
    
    # Save predictions
    results_df = test_df[['date', 'sales']].copy()
    results_df['forecasted_sales'] = predictions
    results_df.to_csv("sales_forecast_results.csv", index=False)
    print("Forecast completed. Saved outputs to sales_forecast_results.csv")

if __name__ == "__main__":
    train_forecaster()
