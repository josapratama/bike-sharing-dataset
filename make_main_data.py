import pandas as pd

# Path ke data
hour_data_path = 'data/hour.csv'
day_data_path = 'data/day.csv'

# Memuat dataset
hour_data = pd.read_csv(hour_data_path)
day_data = pd.read_csv(day_data_path)

# Menambahkan kolom sumber
hour_data['source'] = 'hourly'
day_data['source'] = 'daily'

# Memilih kolom yang diperlukan dan menamai ulang untuk konsistensi
hour_data = hour_data[['dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt', 'source']]
day_data = day_data[['dteday', 'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt', 'source']]

# Menggabungkan data per jam dan per hari
combined_data = pd.concat([hour_data, day_data], ignore_index=True)

# Menyimpan ke CSV
combined_data.to_csv('dashboard/main_data.csv', index=False)
