import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Attempt import of matplotlib, install if missing
try:
    import matplotlib.pyplot as plt
except ImportError:
    import subprocess
    subprocess.run(["pip", "install", "matplotlib"], check=True)
    import matplotlib.pyplot as plt

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
    
    # Generate Visual Plot Chart
    plt.figure(figsize=(10, 5))
    plt.plot(test_df['date'], test_df['sales'], label='Actual Sales Demand', color='#1e293b', linewidth=2)
    plt.plot(test_df['date'], predictions, label='Forecasted Demand (Linear Regression)', color='#3b82f6', linestyle='--', linewidth=2)
    plt.title('Retail Sales Forecast vs Actual Demand Model', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Date Range', fontsize=12)
    plt.ylabel('Daily Units Sold', fontsize=12)
    plt.legend(loc='upper left')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    
    # Save plot file
    plot_filename = "sales_forecast_plot.png"
    plt.savefig(plot_filename, dpi=300)
    plt.close()
    print(f"Saved forecasting visualization plot to {plot_filename}")

if __name__ == "__main__":
    train_forecaster()
