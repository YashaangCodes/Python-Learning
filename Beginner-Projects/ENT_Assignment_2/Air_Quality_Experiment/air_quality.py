import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# 1. LOAD THE DATASET
# ---------------------------------------------

df = pd.read_csv("city_day.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ---------------------------------------------
# 2. CHECK DATA
# ---------------------------------------------

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------------
# 3. CONVERT DATE COLUMN
# ---------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# Sort data according to date
df = df.sort_values("Date")


# ---------------------------------------------
# 4. SELECT ONE CITY
# ---------------------------------------------

city = "Mumbai"

mumbai = df[df["City"] == city].copy()

print("\nMumbai Data:")
print(mumbai.head())


# ---------------------------------------------
# 5. MONTHLY AVERAGE PM2.5
# ---------------------------------------------

monthly_pm25 = mumbai.set_index("Date")["PM2.5"].resample("ME").mean()

plt.figure(figsize=(12, 5))

plt.plot(monthly_pm25.index, monthly_pm25.values)

plt.xlabel("Date")
plt.ylabel("PM2.5 (µg/m³)")
plt.title("Monthly Average PM2.5 in Mumbai")

plt.grid()
plt.tight_layout()
plt.show()


# ---------------------------------------------
# 6. COMPARE POLLUTANTS
# ---------------------------------------------

pollutants = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]

average_pollution = mumbai[pollutants].mean()

print("\nAverage Pollutant Concentrations in Mumbai:")
print(average_pollution)


plt.figure(figsize=(10, 5))

average_pollution.plot(kind="bar")

plt.xlabel("Pollutant")
plt.ylabel("Average Concentration")
plt.title("Average Pollutant Concentration in Mumbai")

plt.xticks(rotation=0)
plt.grid(axis="y")

plt.tight_layout()
plt.show()


# ---------------------------------------------
# 7. AQI TREND
# ---------------------------------------------

monthly_aqi = mumbai.set_index("Date")["AQI"].resample("ME").mean()

plt.figure(figsize=(12, 5))

plt.plot(monthly_aqi.index, monthly_aqi.values)

plt.xlabel("Date")
plt.ylabel("AQI")
plt.title("Monthly Average AQI in Mumbai")

plt.grid()
plt.tight_layout()
plt.show()


# ---------------------------------------------
# 8. PM2.5 VS PM10
# ---------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    mumbai["PM2.5"],
    mumbai["PM10"],
    alpha=0.5
)

plt.xlabel("PM2.5 (µg/m³)")
plt.ylabel("PM10 (µg/m³)")
plt.title("Relationship Between PM2.5 and PM10")

plt.grid()
plt.tight_layout()
plt.show()


# ---------------------------------------------
# 9. CORRELATION MATRIX
# ---------------------------------------------

correlation = mumbai[pollutants + ["AQI"]].corr()

print("\nCorrelation Matrix:")
print(correlation)


# ---------------------------------------------
# 10. CITY-WISE AQI COMPARISON
# ---------------------------------------------

city_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)

print("\nAverage AQI of Cities:")
print(city_aqi)


plt.figure(figsize=(12, 6))

city_aqi.plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Average AQI")
plt.title("Average AQI Comparison Across Indian Cities")

plt.xticks(rotation=90)
plt.grid(axis="y")

plt.tight_layout()
plt.show()