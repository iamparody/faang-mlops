import pandas as pd
import os

# Paths
data_dir = os.path.dirname(__file__)
input_file = os.path.join(data_dir, "Apple_Historical_StockPrice2.csv")
reference_file = os.path.join(data_dir, "reference.csv")
current_file = os.path.join(data_dir, "current.csv")

# Load dataset
df = pd.read_csv(input_file)

# Basic cleanup: fix column casing
df.columns = [col.strip().capitalize() for col in df.columns]

# Ensure 'Date' exists and is datetime
if "Date" not in df.columns:
    raise ValueError("Expected a 'Date' column in the dataset")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])
df = df.sort_values("Date")

# --- Create required columns ---
if "Close" not in df.columns:
    raise ValueError("Expected a 'Close' column in the dataset")

df["target"] = df["Close"]

# Simulate predictions (1% shift)
df["prediction"] = df["target"] * 1.01

# Keep only what we need
df = df[["Date", "target", "prediction"]]

# Split
split_point = -30 if len(df) >= 30 else -int(len(df) / 5)
reference = df[:split_point]
current = df[split_point:]

# Save
reference.to_csv(reference_file, index=False)
current.to_csv(current_file, index=False)

print(f"✅ Split complete:")
print(f"  • reference.csv → {len(reference)} rows")
print(f"  • current.csv   → {len(current)} rows")
