import pandas as pd

# Load the saved file
df = pd.read_csv("global_aqi_locations.csv")

print("Shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# Checking missing values
print("\nMissing values:\n", df.isnull().sum())

# Drop rows with no country or name (no use)
df = df.dropna(subset=["country.name", "name"])

# Drop duplicates if any present in data
df = df.drop_duplicates(subset=["id"])

print("\nAfter cleaning:", df.shape)

# Number of stations per country
country_counts = df["country.name"].value_counts().head(10)
print("\nTop 10 countries by station count:\n", country_counts)

# checking longitude and latitude as per global data
print("\nLatitude range:", (df["coordinates.latitude"].min(), df["coordinates.latitude"].max()))
print("Longitude range:", (df["coordinates.longitude"].min(), df["coordinates.longitude"].max()))

# owner of station/ service provider
print("\nTop data providers:\n", df["provider.name"].value_counts().head(10))

#plotting
############
import plotly.express as px

# Load your existing cleaned data
df = pd.read_csv("global_aqi_locations.csv")

# Drop rows missing coordinates (just in case)
df = df.dropna(subset=["coordinates.latitude", "coordinates.longitude"])

# Create the map
fig = px.scatter_geo(
    df,
    lat="coordinates.latitude",
    lon="coordinates.longitude",
    color="country.name",               # color by country
    hover_name="name",                  # show station name on hover
    hover_data={
        "country.name": True,
        "provider.name": True,
        "coordinates.latitude": False,
        "coordinates.longitude": False
    },
    title="Global Air Quality Stations as per (OpenAQ)",
    projection="natural earth"
)

fig.update_layout(
    geo=dict(showland=True, landcolor="Black", showocean=True, oceancolor="lightblue"),
    legend_title_text="Country"
)

fig.show()

