python
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load Public Transport Usage Data
transport_data = pd.read_csv('Public_Transport_Usage_Statistics_Abu_Dhabi.csv')

# Load Air Quality Index Data
with open('Air_Quality_Index_Data_Abu_Dhabi.json') as f:
    air_quality_data = json.load(f)

# Preprocessing and merging datasets
transport_df = pd.DataFrame(transport_data)
air_quality_df = pd.DataFrame(air_quality_data)

# Example: Analyzing peak usage times and corresponding AQI levels
peak_times = transport_df.groupby('peak_usage')['passenger_count'].sum()

# For simplicity, assume AQI data is averaged over the same time intervals
average_aqi = air_quality_df.groupby('time')['AQI'].mean()

# Merge the dataframes on time indices
merged_df = pd.merge(peak_times, average_aqi, left_index=True, right_index=True)

# Plotting the merged data
plt.figure(figsize=(10, 5))
plt.plot(merged_df.index, merged_df['passenger_count'], label='Passenger Count')
plt.plot(merged_df.index, merged_df['AQI'], label='Average AQI', color='red')
plt.xlabel('Time')
plt.ylabel('Count / AQI')
plt.title('Public Transport Usage and Air Quality Index Over Time')
plt.legend()
plt.show()
