import pandas as pd
# https://www.kaggle.com/datasets/piterfm/massive-missile-attacks-on-ukraine?resource=download
# Load the dataset
OSINT_df = pd.read_csv('Data/missile_attacks_daily.csv')  # Source: https://www.kaggle.com/datasets/piterfm/massive-missile-attacks-on-ukraine?resource=download

# Clean blanks and NaNs
OSINT_df['time_start'] = OSINT_df['time_start'].astype(str).str.strip()
OSINT_df['time_end'] = OSINT_df['time_end'].astype(str).str.strip()

# Filter: Keep rows where both 'time_start' and 'time_end' include time info and are not empty
OSINT_df = OSINT_df[(OSINT_df['time_start'].str.len() > 10) & (OSINT_df['time_end'].str.len() > 10)]
OSINT_df.dropna(subset=['time_start', 'time_end', 'target'], inplace=True)

# Convert to datetime safely
OSINT_df['time_start'] = pd.to_datetime(OSINT_df['time_start'], errors='coerce')
OSINT_df['time_end'] = pd.to_datetime(OSINT_df['time_end'], errors='coerce')

# Drop rows where datetime conversion failed
OSINT_df.dropna(subset=['time_start', 'time_end'], inplace=True)

# Define March boundaries
march_start = pd.Timestamp('2025-03-01 00:00')
march_end = pd.Timestamp('2025-03-31 23:59')

# Filter within March boundaries
df_filtered = OSINT_df[(OSINT_df['time_start'] >= march_start) & (OSINT_df['time_end'] <= march_end)]

# Save the filtered DataFrame
OSINT_df[['time_start', 'time_end', 'target']].to_csv('OSINT.csv', index=False)

print("Filtered dataset saved to 'Data/OSINT.csv'")
