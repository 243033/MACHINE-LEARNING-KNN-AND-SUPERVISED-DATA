import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_excel('A:/DATASET/data_harga_rumah_mentah.xlsx', sheet_name='data_mentah')

# Ambil hanya kolom angka
num_data = data.select_dtypes(include='number')
num_vars = num_data.shape[1]

# Grid subplot
n_cols = 4
n_rows = -(-num_vars // n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 4))
axes = axes.flatten()

# Plot setiap kolom angka
for i, column in enumerate(num_data.columns):
    num_data[column].hist(ax=axes[i], bins=20, edgecolor='black')
    axes[i].set_title(column)
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Frequency')

# Hapus kotak kosong
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()