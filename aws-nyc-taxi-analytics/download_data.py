"""
Downloads the latest available month of NYC TLC yellow taxi trip data
(real public dataset, verified reachable at the URL below) and uploads
it to your own S3 bucket so Glue/Athena can actually crawl and query it
(the public nyc-tlc bucket itself denies s3:ListBucket, even to
authenticated AWS accounts).
"""

import os
import boto3
import requests

PROFILE_NAME = "preethi-portfolio"
BUCKET_NAME = "CHANGE-ME-to-your-bucket-name"  # must be globally unique
REGION = "us-east-2"

LATEST_MONTH = "2026-05"  # update this as newer months become available
SOURCE_URL = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{LATEST_MONTH}.parquet"
LOCAL_FILE = f"yellow_tripdata_{LATEST_MONTH}.parquet"
S3_KEY = f"trip-data/{LOCAL_FILE}"


def download_latest_month():
    print(f"Downloading {SOURCE_URL} ...")
    response = requests.get(SOURCE_URL, stream=True)
    response.raise_for_status()
    with open(LOCAL_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Saved locally as {LOCAL_FILE} ({os.path.getsize(LOCAL_FILE) / 1e6:.1f} MB)")


def upload_to_s3():
    session = boto3.Session(profile_name=PROFILE_NAME, region_name=REGION)
    s3 = session.client("s3")
    print(f"Uploading to s3://{BUCKET_NAME}/{S3_KEY} ...")
    s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
    print("Upload complete.")


if __name__ == "__main__":
    if BUCKET_NAME.startswith("CHANGE-ME"):
        raise SystemExit("Set BUCKET_NAME to your actual S3 bucket name before running.")
    download_latest_month()
    upload_to_s3()
