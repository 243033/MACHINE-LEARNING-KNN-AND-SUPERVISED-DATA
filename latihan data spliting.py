import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_excel('A:/DATASET/data_harga_rumah_mentah.xlsx', sheet_name='data_mentah')

# Persiapan minimal sebelum split
data = data.drop_duplicates()                                       
data['harga_rp'] = pd.to_numeric(data['harga_rp'], errors='coerce')
data = data.dropna(subset=['harga_rp'])                             

# Pisahkan fitur dan target
x = data.drop(columns=['harga_rp'])
y = data['harga_rp']

# Bagi data 80% latih, 20% uji
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print("Jumlah data: ", len(x))
print("Jumlah data latih: ", len(x_train))
print("Jumlah data test: ", len(x_test))