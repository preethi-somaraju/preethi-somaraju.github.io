import pandas as pd
import sqlite3
import numpy as np

def run_sales_etl():
    print("Initializing sales pipeline ETL...")
    # Load mock raw transactions data
    np.random.seed(42)
    dates = pd.date_range(start="2025-01-01", end="2025-06-30", freq="D")
    data = {
        "transaction_id": range(1001, 1001 + len(dates)),
        "date": dates,
        "customer_id": np.random.randint(5001, 5200, size=len(dates)),
        "product_category": np.random.choice(["Electronics", "Home Decor", "Apparel", "Office Supplies"], size=len(dates)),
        "quantity": np.random.randint(1, 5, size=len(dates)),
        "unit_price": np.random.uniform(10.0, 500.0, size=len(dates)).round(2)
    }
    df = pd.DataFrame(data)
    df["revenue"] = (df["quantity"] * df["unit_price"]).round(2)
    
    # Save clean dataset
    df.to_csv("clean_sales_data.csv", index=False)
    print("  Clean sales dataset outputted to 'clean_sales_data.csv'.")
    
    # Upload to local SQLite DB for business query demonstration
    conn = sqlite3.connect("sales_reporting.db")
    df.to_sql("sales_transactions", conn, if_exists="replace", index=False)
    conn.close()
    print("  Sales database loaded to SQLite successfully.")

if __name__ == "__main__":
    run_sales_etl()
