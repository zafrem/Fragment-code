import requests
import pandas as pd
import matplotlib.pyplot as plt
import urllib3
urllib3.disable_warnings()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# FRED API configuration
API_KEY = "1c8585ebaf71fa0b53c64d2bc14e8d6a"  # Replace with your API key
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

# Fetch unemployment benefits data (Initial Claims)
def fetch_unemployment_data(series_id, api_key):
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

series_id = "IURSA"  # Insured Unemployment Rate
data = fetch_unemployment_data(series_id, API_KEY)

if data:
    # Convert the data to a DataFrame
    observations = data.get("observations", [])
    df = pd.DataFrame(observations)

    # Convert date and value columns to appropriate types
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")

    # Plot the unemployment claims
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["value"], label="Initial Claims (ICSA)", color="blue")
    plt.title("Insured Unemployment Rate")
    plt.xlabel("Year")
    plt.ylabel("Number of Claims")
    plt.grid(True)
    plt.legend()
    plt.show()
