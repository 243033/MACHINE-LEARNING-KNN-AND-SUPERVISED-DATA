import pandas as pd

# membuat variable supaya data dibaca dalam variable untuk data loading
train = pd.read_excel('A:/DATASET/data_harga_rumah_mentah.xlsx', sheet_name='data_mentah')

# 1. mengenali data
train.info()
train.describe(include="all")

# 2. kemudian data hitung mising value
missing_values = train.isnull().sum()
missing_values[missing_values > 0]

# 3. data memisahkan kolom berdasarkan banyaknya data missing value
less = missing_values[missing_values < 20].index
over = missing_values[missing_values >= 20].index   

# 4. disini data isi kolom angka dengan median(nilai dari tengah setelah data diurutkan dari yang terkecil ke terbesar)
numeric_features = train[less].select_dtypes(include=['number']).columns
train[numeric_features] = train[numeric_features].fillna(train[numeric_features].median())

# 5. mengisi kolom kategori dengan modulo
kategorical_features = train[less].select_dtypes(include=['object']).columns
for column in kategorical_features:
    train[column] = train[column].fillna(train[column].mode()[0])