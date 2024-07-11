import re

import pandas as pd

"""
load
"""

months = [10, 11, 12]
# expect certain data type, fast loading and detect change
taxi_dtypes = {
    "VendorID": pd.Int64Dtype(),
    "passenger_count": pd.Int64Dtype(),
    "trip_distance": float,
    "RatecodeID": pd.Int64Dtype(),
    "store_and_fwd_flag": str,
    "PULocationID": pd.Int64Dtype(),
    "DOLocationID": pd.Int64Dtype(),
    "payment_type": pd.Int64Dtype(),
    "fare_amount": float,
    "extra": float,
    "mta_tax": float,
    "tip_amount": float,
    "tolls_amount": float,
    "improvement_surcharge": float,
    "total_amount": float,
    "congestion_surcharge": float,
    "trip_type": int,
}


parse_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

df = pd.DataFrame()
for month in months:
    url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{str(month)}.csv.gz"
    data = pd.read_csv(
        url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates
    )
    if df.empty:
        df = data
    else:
        df = pd.concat([df, data])


start_date = pd.to_datetime("2020-10-01 00:00:00")
end_date = pd.to_datetime("2020-12-31 23:59:59")

mask = df["lpep_pickup_datetime"].between(start_date, end_date)
false_df = df[~mask]

assert (
    df["lpep_pickup_datetime"].between(start_date, end_date).all()
), "The df is not between October and December 2020"


"""
transform
"""
mask = (df["passenger_count"] > 0) & (df["trip_distance"] > 0)
df = df[mask]

df["lpep_pickup_date"] = df["lpep_pickup_datetime"].dt.date


def camel_to_snake(camel_str):
    # This regex handles consecutive uppercase letters properly
    snake_str = re.sub(
        r"([A-Z]+)([A-Z][a-z])", r"\1_\2", camel_str
    )  # Handles cases like HTTPRequest
    snake_str = re.sub(
        r"([a-z\d])([A-Z])", r"\1_\2", snake_str
    )  # Handles normal camel case
    return snake_str.lower()


columns = [
    "VendorID",
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "store_and_fwd_flag",
    "RatecodeID",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "fare_amount",
    "extra",
    "mta_tax",
    "tip_amount",
    "tolls_amount",
    "ehail_fee",
    "improvement_surcharge",
    "total_amount",
    "payment_type",
    "trip_type",
    "congestion_surcharge",
]

df.columns = [camel_to_snake(col) for col in columns]

"""
transform_test
"""
assert "vendor_id" in df.columns

assert (df["passenger_count"] > 0).all()

assert (df["trip_distance"] > 0).all()


# answer
"(266855, 20)"
"(139370, 20)"
"data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date"
"1 or 2"
"4"
"95"
