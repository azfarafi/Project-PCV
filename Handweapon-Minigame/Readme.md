# Handweapon Mini Game 

Mini game bertema **Fruit Ninja** sederhana menggunakan **deteksi tangan sebagai pisau**.  
Game dikembangkan hanya dengan **Python + OpenCV + NumPy**, tanpa framework atau game engine tambahan.

---

## Fitur Utama
- **Gesture Detection**: deteksi tangan berbasis warna.
- **Second Object (Target)**: sprite target muncul dan bisa dihancurkan.
- **Scoring System**: skor bertambah setiap kali target kena pukulan cepat.
- **Weapon Overlay**: sprite senjata/tangan ditempel di posisi tangan dengan alpha blending manual.
- **Gesture Recognition**: gerakan cepat (slash) → digunakan untuk menghancurkan target.
- **Game Timer**: durasi permainan 15 detik.
- **Game Result**: tampil gambar `menang.png` jika skor ≥ threshold, atau `kalah.png` jika skor < threshold.
- **Efek Destroyed**: tulisan "Memasak!" muncul selama beberapa detik saat target hancur.
- **Replay**: setelah game selesai, tekan **spasi** untuk main lagi atau **ESC** untuk keluar.

---

## Teknologi
- **Python**
- **OpenCV (cv2)** → kamera, manipulasi gambar, window game.
- **NumPy** → operasi array & manipulasi piksel.
- **OS, Time, Threading, Winsound** → modul bawaan Python untuk path, timer, thread, dan audio `.wav`.

---


---


## Cara Menjalankan
1. Clone repositori:
   ```bash
   git clone https://github.com/username/Handweapon-Minigame.git
   cd Handweapon-Minigame

2. Intall Library : 
pip install opencv-python numpy

3. Jalankan Game : 
python main.py

---
## Cara Memainkan 
1. **Deteksi tangan**
   - Arahkan tangan ke depan kamera.
   - Game akan mendeteksi area tangan berdasarkan warna (HSV mask).
   - Sprite senjata (`knife.png`) akan muncul mengikuti posisi tangan.

2. **Gerakan slash**
   - Lakukan gerakan cepat (mengayun/slash) dengan tangan.
   - Jika gerakan cukup cepat dan mengenai target, target akan hancur.
   - Skor bertambah setiap kali target kena.

3. **Timer permainan**
   - Game berlangsung selama **15 detik**.
   - Skor dan waktu tersisa ditampilkan di layar.

4. **Hasil akhir**
   - Jika skor ≥ threshold (misalnya 5) → muncul gambar **menang.png**.
   - Jika skor < threshold → muncul gambar **kalah.png**.

5. **Replay**
   - Setelah hasil muncul, tekan **spasi** untuk main lagi.
   - Tekan **ESC** untuk keluar dari game.

---
## Dokumentasi
- **Screenshot Game**: [Gameplay](docs/screenshoot1.png)
- **Screenshot Menang**: [Menang](docs/screenshoot2.png)
- **Screenshot Kalah**: [Kalah](docs/screenshoot3.png)
- **Video Demo**: [Tonton Video Demo](docs/demo.mp4)
