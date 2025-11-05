import requests
import pandas as pd

url = "https://api.openaq.org/v3/locations"
headers = {"X-API-Key": "API key"}

params = {
    "limit": 500,        # fetch more data for EDA
    "sort": "desc"
}

response = requests.get(url, headers=headers, params=params)
print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data["results"])
    print("DATA FETCHED!")
    print("Shape:", df.shape)
    print(df.columns.tolist())
    df.to_csv("global_aqi_locations.csv", index=False)
    print("Saved as global_aqi_locations.csv")
else:
    print("Error:", response.text)

