import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define constants for repeated literals
WEATHER_IMPACT_TITLE = "Dampak Cuaca Terhadap Penyewaan Sepeda"
WEEKDAY_WEEKEND_DIFFERENCE_TITLE = "Perbedaan Penggunaan Sepeda antara Hari Kerja dan Akhir Pekan"

# Path ke data
file_path = 'dashboard/main_data.csv'

# Memuat dataset
data = pd.read_csv(file_path)

# Pilihan visualisasi
visualization_type = st.sidebar.selectbox(
    "Pilih jenis visualisasi:",
    [WEATHER_IMPACT_TITLE, WEEKDAY_WEEKEND_DIFFERENCE_TITLE]
)

if visualization_type == WEATHER_IMPACT_TITLE:
    if 'weathersit' in data.columns and 'cnt' in data.columns:
        # Agregasi data berdasarkan kondisi cuaca
        weather_data = data[['weathersit', 'cnt']].groupby('weathersit').sum().reset_index()
        
        # Membuat grafik
        st.write(WEATHER_IMPACT_TITLE)
        plt.figure(figsize=(10, 6))
        plt.bar(weather_data['weathersit'], weather_data['cnt'])
        plt.xlabel('Kondisi Cuaca')
        plt.ylabel('Jumlah Penyewaan')
        plt.title('Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
        st.pyplot(plt)
    else:
        st.write("Kolom 'weathersit' atau 'cnt' tidak ditemukan dalam dataset.")

elif visualization_type == WEEKDAY_WEEKEND_DIFFERENCE_TITLE:
    if 'workingday' in data.columns and 'cnt' in data.columns:
        # Agregasi data berdasarkan hari kerja
        usage_data = data[['workingday', 'cnt']].groupby('workingday').sum().reset_index()
        usage_data['workingday'] = usage_data['workingday'].map({0: 'Akhir Pekan', 1: 'Hari Kerja'})
        
        # Membuat grafik
        st.write(WEEKDAY_WEEKEND_DIFFERENCE_TITLE)
        plt.figure(figsize=(10, 6))
        plt.bar(usage_data['workingday'], usage_data['cnt'])
        plt.xlabel('Tipe Hari')
        plt.ylabel('Jumlah Penyewaan')
        plt.title('Jumlah Penyewaan Sepeda Berdasarkan Tipe Hari')
        st.pyplot(plt)
    else:
        st.write("Kolom 'workingday' atau 'cnt' tidak ditemukan dalam dataset.")
