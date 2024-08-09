import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import folium
from folium.plugins import HeatMap

# Memuat data
data = pd.read_csv('dashboard/main_data.csv')

# Mengatur palet warna
sns.set_palette("Set2")

# Visualisasi Box Plot untuk Dampak Cuaca
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=data)
plt.title('Distribusi Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.xticks([0, 1, 2], ['Cerah', 'Mendung', 'Hujan'])
plt.show()

# Visualisasi Bar Chart untuk Dampak Cuaca
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=data, estimator=lambda x: sum(x)/len(x))
plt.title('Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xticks([0, 1, 2], ['Cerah', 'Mendung', 'Hujan'])
plt.show()

# Visualisasi Bar Chart untuk Hari Kerja vs Akhir Pekan
plt.figure(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=data, estimator=lambda x: sum(x)/len(x))
plt.title('Rata-rata Jumlah Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan')
plt.xlabel('Hari Kerja (0 = Tidak, 1 = Ya)')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xticks([0, 1], ['Akhir Pekan', 'Hari Kerja'])
plt.show()

# RFM Analysis
rfm_data = data.groupby('dteday').agg({
    'cnt': ['sum', 'count', 'mean']
}).reset_index()
rfm_data.columns = ['dteday', 'Total_Spend', 'Frequency', 'Average_Spend']

# Visualisasi RFM Analysis
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.hist(rfm_data['Total_Spend'], bins=20, color='skyblue')
plt.title('Distribusi Total Belanja')
plt.xlabel('Total Belanja')
plt.ylabel('Frekuensi')

plt.subplot(1, 3, 2)
plt.hist(rfm_data['Frequency'], bins=20, color='salmon')
plt.title('Distribusi Frekuensi')
plt.xlabel('Frekuensi')
plt.ylabel('Frekuensi')

plt.subplot(1, 3, 3)
plt.hist(rfm_data['Average_Spend'], bins=20, color='lightgreen')
plt.title('Distribusi Pengeluaran Rata-rata')
plt.xlabel('Pengeluaran Rata-rata')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Clustering
features = data[['temp', 'hum', 'windspeed']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)  # Menambahkan random_state untuk konsistensi
data['cluster'] = kmeans.fit_predict(features_scaled)

# Visualisasi Hasil Clustering
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['temp'], data['hum'], c=data['cluster'], cmap='viridis')
plt.colorbar(scatter, label='Cluster')
plt.title('Clustering Penyewaan Sepeda berdasarkan Suhu dan Kelembapan')
plt.xlabel('Suhu')
plt.ylabel('Kelembapan')
plt.show()

# Geoanalysis (contoh jika data koordinat tersedia)
# Membuat peta dengan heatmap
m = folium.Map(location=[45.5236, -122.6750], zoom_start=12)  # Lokasi awal peta (latitude, longitude)
heat_data = [[45.5236, -122.6750], [45.5289, -122.6740]]  # Contoh data lokasi (latitude, longitude)
HeatMap(heat_data).add_to(m)

# Menyimpan peta
m.save('heatmap.html')
print("Peta panas telah disimpan sebagai 'heatmap.html'")
