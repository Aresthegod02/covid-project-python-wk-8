import pandas as pd

# Load the data
df = pd.read_csv("owid-covid-data.csv")

# Quick overview
print(df.shape)
print(df.columns)
df.head()

# Check missing values
df.isnull().sum()

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Check data types
df.dtypes
# Check for duplicates
df.duplicated().sum()

countries = ['Nigeria', 'United States', 'India', 'United Kingdom']
df = df[df['location'].isin(countries)]

# Drop rows with missing critical values
df.dropna(subset=['date', 'total_cases'], inplace=True)

# Fill other missing numeric values
df.fillna(0, inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Plot total cases over time
plt.figure(figsize=(14, 6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

# Death rate analysis
df['death_rate'] = df['total_deaths'] / df['total_cases']

# Vaccination progress
plt.figure(figsize=(14, 6))
for country in countries:
    temp = df[df['location'] == country]
    plt.plot(temp['date'], temp['total_vaccinations'], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.show()

# Keep only numeric columns for correlation
numeric_df = df.select_dtypes(include='number')
correlation_matrix = numeric_df.corr()


import plotly.express as px

# Latest date's data
latest = df[df['date'] == df['date'].max()]

fig = px.choropleth(latest,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Viridis",
                    title="COVID-19 Total Cases by Country")
fig.show()

