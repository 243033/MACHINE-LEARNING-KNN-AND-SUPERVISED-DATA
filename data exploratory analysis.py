import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_excel('A:/DATASET/data_harga_rumah_mentah.xlsx', sheet_name='data_mentah')

# Cleaning singkat supaya grafik tidak error
data['harga_rp'] = pd.to_numeric(data['harga_rp'], errors='coerce')
data['kota'] = data['kota'].str.strip().str.title()

num_columns = ['luas_tanah_m2', 'luas_bangunan_m2', 'usia_bangunan_tahun', 'jarak_ke_pusat_kota_km']
cat_columns = ['kota', 'kondisi']

plt.figure(figsize=(10, 7))

# Kolom angka: histogram + kurva KDE
for i, column in enumerate(num_columns, 1):
    plt.subplot(2, 3, i)
    sns.histplot(data[column], kde=True, bins=30)
    plt.title(f'Distribution of {column}')

# Kolom kategori: batang jumlah per kategori (tanpa KDE)
for i, column in enumerate(cat_columns, len(num_columns) + 1):
    plt.subplot(2, 3, i)
    sns.histplot(data[column], bins=30)
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()