import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Accident_Sample.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# ---------------------------
# Missing Values
# ---------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing coordinates
df = df.dropna(subset=["Latitude", "Longitude"])

# ---------------------------
# 1. Accident Severity
# ---------------------------
plt.figure(figsize=(6, 4))
df["Accident_Severity"].value_counts().plot(kind="bar")
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("accident_severity.png")
plt.show()

# ---------------------------
# 2. Weather Conditions
# ---------------------------
plt.figure(figsize=(10, 5))
df["Weather_Conditions"].value_counts().head(10).plot(kind="bar")
plt.title("Top Weather Conditions During Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Accident Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.show()

# ---------------------------
# 3. Road Surface Conditions
# ---------------------------
plt.figure(figsize=(8, 5))
df["Road_Surface_Conditions"].value_counts().plot(kind="bar")
plt.title("Road Surface Conditions")
plt.xlabel("Road Surface")
plt.ylabel("Accident Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("road_surface_conditions.png")
plt.show()

# ---------------------------
# 4. Time of Day Analysis
# ---------------------------
df["Hour"] = pd.to_datetime(
    df["Time"],
    format="%H:%M",
    errors="coerce"
).dt.hour

plt.figure(figsize=(10, 5))
sns.histplot(df["Hour"].dropna(), bins=24)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.savefig("accidents_by_hour.png")
plt.show()

# ---------------------------
# 5. Urban vs Rural
# ---------------------------
plt.figure(figsize=(6, 4))
df["Urban_or_Rural_Area"].value_counts().plot(kind="bar")
plt.title("Urban vs Rural Accidents")
plt.xlabel("Area Type")
plt.ylabel("Accident Count")
plt.tight_layout()
plt.savefig("urban_vs_rural.png")
plt.show()

# ---------------------------
# 6. Accident Hotspots
# ---------------------------
plt.figure(figsize=(10, 6))

plt.scatter(
    df["Longitude"],
    df["Latitude"],
    alpha=0.5,
    s=10
)

plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.savefig("accident_hotspots.png")
plt.show()

print("\nTask 5 Completed Successfully!")