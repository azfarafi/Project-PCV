# Mini Project 1 Image Restoration

## Nama & NRP

**Nama:** Azfarafi Gustiar Jati
**NRP:** 5024241037

---

## Deskripsi Singkat

Project ini bertujuan untuk melakukan **restorasi citra** dari gambar yang telah mengalami noise (kerusakan), menggunakan pendekatan manual berbasis **NumPy** tanpa memanfaatkan fungsi processing dari OpenCV.

Citra yang digunakan adalah `lena_noisy.png`, dan hasil akhirnya disimpan sebagai `lena_restored.png`.

---

## Library yang Digunakan

* `numpy` → operasi pengolahan citra (filtering, histogram, transformasi)
* `cv2` → membaca dan menyimpan citra
* `matplotlib` → visualisasi histogram dan perbandingan gambar

---

## Pipeline Restorasi

### 1. Denoising (Median Filter)

* Menggunakan **median filter 5x5 manual**
* Dilakukan dengan padding `reflect`
* Setiap pixel diganti dengan nilai median dari tetangganya

**Tujuan:**
Menghilangkan noise terutama **salt-and-pepper noise**

---

### 2. Histogram Equalization (Manual)

* Menghitung histogram menggunakan `np.bincount`
* Menghitung CDF (Cumulative Distribution Function)
* Normalisasi ke range 0–255
* Membuat LUT (Look-Up Table)
* Mapping ulang nilai pixel

**Tujuan:**
Meningkatkan kontras citra

---

### 3. Sharpening (Kernel Manual)

* Menggunakan kernel:

```
[ 0 -1  0 ]
[-1  5 -1]
[ 0 -1  0 ]
```

* Dilakukan dengan konvolusi manual (loop + padding)

**Tujuan:**
Mempertajam detail yang sebelumnya blur akibat proses denoising

---

## Hasil Visualisasi

### Perbandingan Pipeline

Gambar berikut menunjukkan:

* Citra asli (noisy)
* Hasil median filter
* Hasil histogram equalization
* Hasil sharpening
* Histogram masing-masing tahap

![Pipeline Visualization](output/visualisasi_pipeline.png)

### Hasil Akhir

![Final Result](output/lena_restored.png)

---

## Analisis

Yang Berhasil

* Median filter efektif mengurangi noise
* Histogram equalization meningkatkan kontras (histogram lebih menyebar)
* Sharpening mengembalikan detail yang hilang

## Cara Menjalankan Program

1. Pastikan struktur folder:

```
mp1-image-restoration/
├── restoration.py
├── input/
│   └── lena_noisy.png
└── output/
```

2. Install library:

```bash
pip install numpy opencv-python matplotlib
```

3. Jalankan program:

```bash
python restoration.py
```

4. Output:

* `output/lena_restored.png`
* `output/visualisasi_pipeline.png`

---

## Kesimpulan

Pendekatan manual menggunakan NumPy berhasil melakukan restorasi citra dengan baik. Kombinasi median filter, histogram equalization, dan sharpening memberikan hasil yang lebih bersih dan tajam dibanding citra awal.

Namun, masih terdapat ruang untuk peningkatan seperti:

* Penggunaan Gaussian filter manual
* Adaptive histogram equalization
* Parameter tuning kernel sharpening

---

## Catatan

Semua operasi dilakukan secara manual sesuai ketentuan tugas tanpa menggunakan fungsi processing dari OpenCV.

---

