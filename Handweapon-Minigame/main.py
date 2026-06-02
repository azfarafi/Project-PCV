import cv2
import numpy as np
import os
import winsound
import threading
import time
from utils import get_blue_mask, apply_morphology
from gesture_detection import detect_blue_object
import config
from asset.target import Target, overlay_sprite
from asset.effect import show_destroy_effect, draw_destroy_text

base_path = os.path.dirname(__file__)

# Load sprites
sprite_alive = cv2.imread(os.path.join(base_path, "asset/sprites/target.png"), cv2.IMREAD_UNCHANGED)
sprite_destroyed = cv2.imread(os.path.join(base_path, "asset/sprites/destroy.png"), cv2.IMREAD_UNCHANGED)
hand_sprite = cv2.imread(os.path.join(base_path, "asset/sprites/knife.png"), cv2.IMREAD_UNCHANGED)

# Load background animasi
backgrounds = []
for i in range(1, 6):
    bg = cv2.imread(os.path.join(base_path, f"asset/sprites/bg{i}.png"))
    if bg is not None:
        backgrounds.append(cv2.resize(bg, (640,480)))

# --- Fungsi untuk loop backsound ---
def play_background():
    winsound.PlaySound(os.path.join(base_path, "asset/sound/backsound.wav"),
                       winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

# --- Fungsi utama game ---
def play_game():
    threading.Thread(target=play_background, daemon=True).start()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    score = 0
    target = Target(sprite_alive=sprite_alive, sprite_destroyed=sprite_destroyed,
                    size=128, destroyed_size=200)

    prev_pos = None
    frame_count = 0
    start_time = time.time()
    GAME_DURATION = 15
    WIN_THRESHOLD = 5  

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)

        blue_mask = get_blue_mask(frame)
        blue_mask = apply_morphology(blue_mask)
        pos = detect_blue_object(blue_mask, frame)

        # background
        if backgrounds:
            bg_index = (frame_count // 20) % len(backgrounds)
            game_frame = backgrounds[bg_index].copy()
        else:
            game_frame = np.zeros((480,640,3), dtype=np.uint8)

        target.update()
        target.draw(game_frame)

        if pos:
            cx, cy = pos
            if prev_pos:
                dx = cx - prev_pos[0]
                dy = cy - prev_pos[1]
                speed = (dx**2 + dy**2)**0.5
                if target.check_hit(pos, speed, config.HIT_SPEED_THRESHOLD):
                    score += 1
                    show_destroy_effect(game_frame, target.pos)
                    # Tidak ada suara pisau, hanya efek visual
            prev_pos = (cx, cy)
            if hand_sprite is not None:
                overlay_sprite(game_frame, hand_sprite, pos, size=200)

        # tampilkan efek destroyed
        draw_destroy_text(game_frame, target.pos)

        # tampilkan skor & timer
        elapsed = int(time.time() - start_time)
        remaining = GAME_DURATION - elapsed
        cv2.putText(game_frame, f"Score: {score}", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(game_frame, f"Time: {remaining}s", (20,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.imshow("Game Window", game_frame)
        cv2.imshow("Detection Window", frame)   # kamera dengan kotak biru
        cv2.imshow("Blue Mask", blue_mask)      # hasil masking biru

        frame_count += 1

        if remaining <= 0:
            break
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    winsound.PlaySound(None, winsound.SND_PURGE)

    # tampilkan hasil
    if score >= WIN_THRESHOLD:
        result_img = cv2.imread(os.path.join(base_path, "asset/sprites/menang.png"))
    else:
        result_img = cv2.imread(os.path.join(base_path, "asset/sprites/kalah.png"))

    if result_img is not None:
        result_img = cv2.resize(result_img, (640,480))
        cv2.imshow("Game Window", result_img)

        # tunggu input spasi atau ESC
        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == 32:  # spasi
                cv2.destroyAllWindows()
                play_game()   # main lagi
                break
            elif key == 27:  # ESC
                cv2.destroyAllWindows()
                break

# --- Jalankan game pertama kali ---
play_game()



