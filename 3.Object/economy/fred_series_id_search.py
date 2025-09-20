import requests
import urllib3
urllib3.disable_warnings()

# FRED API URL
API_KEY = "1c8585ebaf71fa0b53c64d2bc14e8d6a"
SEARCH_KEYWORD = 'Employment+Cost+Index'  # Example: Average Hourly Earnings
URL = f"https://api.stlouisfed.org/fred/series/search?search_text={SEARCH_KEYWORD}&api_key={API_KEY}&file_type=json" \
      f"&search_type=full_text"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    series = data.get("seriess", [])
    for s in series:
        print(f"ID: {s['id']} - Title: {s['title']}")
else:
    print("Failed to fetch series IDs.")
