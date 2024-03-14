import numpy as np
import matplotlib.pyplot as plt

# Ukuran gambar
rowmax = 300
colmax = 300

# Membuat gambar kosong
gambar = np.zeros(shape=(rowmax, colmax, 3), dtype=np.uint8)

# Loop untuk mengisi warna berdasarkan pola tertentu
for i in range(rowmax):
    for j in range(colmax):
        if (i < rowmax/2) and (j < colmax/2):
            gambar[i, j] = [255, 0, 0]  # Merah
        elif (i < rowmax/2) and (j >= colmax/2):
            gambar[i, j] = [0, 255, 0]  # Hijau
        elif (i >= rowmax/2) and (j < colmax/2):
            gambar[i, j] = [0, 0, 255]  # Biru
        else:
            gambar[i, j] = [255, 255, 0]  # Kuning

# Menampilkan gambar
plt.imshow(gambar)
plt.axis('off')  # Menghilangkan sumbu
plt.show()
