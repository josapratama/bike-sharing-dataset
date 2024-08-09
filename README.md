# Proyek Analisis Penyewaan Sepeda

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset yang mencakup informasi per jam dan per hari. Analisis meliputi dampak cuaca terhadap penyewaan sepeda, perbedaan penggunaan sepeda antara hari kerja dan akhir pekan, serta eksplorasi tambahan seperti analisis RFM dan clustering.

## Struktur Direktori

- `dashboard/`
  - `main_data.csv` : Data gabungan dari per jam dan per hari.
  - `dashboard.py` : Skrip Streamlit yang menyediakan dashboard interaktif untuk visualisasi dampak cuaca terhadap penyewaan sepeda dan perbedaan antara hari kerja dan akhir pekan.
  - `analysis.py` : Skrip untuk analisis tambahan termasuk visualisasi box plot, bar chart, analisis RFM, clustering, dan geoanalysis.
- `data/`
  - `hour.csv` : Data penyewaan sepeda per jam.
  - `day.csv` : Data penyewaan sepeda per hari.
- `make_main_data.py` : Skrip untuk menggabungkan data per jam dan per hari menjadi satu file CSV (main_data.csv) yang digunakan untuk analisis dan visualisasi.
- `notebook.ipynb`: Notebook Jupyter untuk dokumentasi dan analisis tambahan.
- `README.md`: Dokumentasi proyek ini.
- `requirements.txt`: Daftar dependensi Python.
- `url.txt`: URL atau informasi terkait lainnya

## Cara Menjalankan Dashboard

1. **Instalasi Dependensi**

   Pastikan Anda telah menginstal semua dependensi yang diperlukan. Gunakan `requirements.txt` untuk menginstal paket-paket yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan Skrip Dashboard**
   Setelah semua dependensi terinstal, jalankan dashboard.py menggunakan Streamlit untuk melihat visualisasi interaktif:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

   Ini akan membuka aplikasi Streamlit di browser Anda, memungkinkan Anda untuk memilih jenis visualisasi dan melihat data secara interaktif.

## Cara Menjalankan Analisis

1. **Instalasi Dependensi**

   Sama seperti langkah di atas, pastikan semua dependensi yang diperlukan sudah terinstal.

2. **Jalankan Skrip Analisis**

   Jalankan analysis.py untuk melakukan analisis tambahan dan visualisasi data:

   ```bash
   python dashboard/analysis.py
   ```

   Hasil visualisasi akan ditampilkan langsung di jendela terminal atau disimpan sebagai file, seperti heatmap.html untuk analisis geo.

## Catatan

- Pastikan Anda berada di direktori utama proyek (bike-sharing-dataset) saat menjalankan perintah di atas.
- Sesuaikan path atau konfigurasi jika Anda menggunakan lingkungan virtual atau struktur folder yang berbeda.
