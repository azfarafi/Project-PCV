import cv2
import time

# Simpan waktu terakhir efek muncul
last_destroy_time = 0
DESTROY_DURATION = 0.5  # detik

def show_destroy_effect(frame, pos):
    """Dipanggil saat target kena pukulan"""
    global last_destroy_time
    last_destroy_time = time.time()
    cx, cy = pos
    cv2.putText(frame, "Memasak!", (cx-50, cy-50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

def draw_destroy_text(frame, pos):
    """Dipanggil setiap frame untuk menampilkan tulisan selama durasi"""
    if time.time() - last_destroy_time < DESTROY_DURATION:
        cx, cy = pos
        cv2.putText(frame, "Memasak!", (cx-50, cy-50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
