import pandas as pd

# Load data
df = pd.read_csv("data/raw/faang_stocks.csv")

# Drop columns with 0 non-null values
df.drop(columns=[
    'Revenue', 'Gross Profit', 'Operating Income', 'Cash Ratio',
    'Total Assets', 'Total Equity',
    'Trailing Twelve Months (TTM) Revenue',
    'Trailing Twelve Months (TTM) EBITDA',
    'Trailing Twelve Months (TTM) Earnings'
], inplace=True)

# Drop rows with missing target value (Close)
df.dropna(subset=['Close'], inplace=True)

# Optional: fill Beta values
df['Beta'] = df['Beta'].fillna(df['Beta'].mean())
df['Beta (5Y)'] = df['Beta (5Y)'].fillna(df['Beta (5Y)'].mean())

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date (per ticker)
df.sort_values(['Ticker', 'Date'], inplace=True)

# Save cleaned version
df.to_csv("data/clean/faang_clean.csv", index=False)

print(" Cleaned dataset saved to data/clean/faang_clean.csv")
