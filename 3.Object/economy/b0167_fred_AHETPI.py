import requests
import pandas as pd
import matplotlib.pyplot as plt
import urllib3
urllib3.disable_warnings()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# FRED API configuration
API_KEY = "1c8585ebaf71fa0b53c64d2bc14e8d6a"  # Replace with your actual FRED API key
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

# Wage growth data series ID (example: 'AHETPI' for Average Hourly Earnings)
SERIES_ID = "AHETPI"

def fetch_wage_data(series_id, api_key):
    # API parameters
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json"
    }

    # Fetch data from FRED API
    response = requests.get(FRED_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        return None

# Fetch data
data = fetch_wage_data(SERIES_ID, API_KEY)

if data:
    # Convert the data to a DataFrame
    observations = data.get("observations", [])
    df = pd.DataFrame(observations)

    # Convert date and value columns to appropriate types
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Plot the wage growth rate
    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["value"], label="Average Hourly Earnings", color="blue")
    plt.title("U.S. Wage Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Average Hourly Earnings (Index)")
    plt.grid(True)
    plt.legend()
    plt.show()
