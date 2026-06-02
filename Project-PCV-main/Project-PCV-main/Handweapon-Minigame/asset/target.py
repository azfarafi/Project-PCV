import cv2
import numpy as np

def overlay_sprite(frame, sprite, pos, size):
    sprite_resized = cv2.resize(sprite, (size, size))
    h, w = sprite_resized.shape[:2]
    x, y = pos

    roi = frame[y-h//2:y+h//2, x-w//2:x+w//2]
    if roi.shape[0] != h or roi.shape[1] != w:
        return

    if sprite_resized.shape[2] == 4:  # ada alpha channel
        b,g,r,a = cv2.split(sprite_resized)
        fg = cv2.merge((b,g,r))
        mask = cv2.merge((a,a,a))
        fg_masked = cv2.bitwise_and(fg, mask)
        bg_masked = cv2.bitwise_and(roi, cv2.bitwise_not(mask))
        combined = cv2.add(fg_masked, bg_masked)
        frame[y-h//2:y+h//2, x-w//2:x+w//2] = combined
    else:
        frame[y-h//2:y+h//2, x-w//2:x+w//2] = sprite_resized

class Target:
    def __init__(self, pos=(320,480), size=128, destroyed_size=200,
                 sprite_alive=None, sprite_destroyed=None):
        self.pos = list(pos)
        self.size = size
        self.destroyed_size = destroyed_size
        self.destroyed = False
        self.sprite_alive = sprite_alive
        self.sprite_destroyed = sprite_destroyed
        self.velocity_y = -np.random.randint(15,25)
        self.gravity = 1
        self.destroy_timer = 0

    def update(self, width=640, height=480):
        if self.destroyed:
            if self.destroy_timer > 0:
                self.destroy_timer -= 1
            else:
                self.pos = [np.random.randint(100, width-100), height]
                self.velocity_y = -np.random.randint(15,25)
                self.destroyed = False
        else:
            self.pos[1] += self.velocity_y
            self.velocity_y += self.gravity
            if self.pos[1] > height + self.size//2:
                self.pos = [np.random.randint(100, width-100), height]
                self.velocity_y = -np.random.randint(15,25)

    def draw(self, frame):
        if self.destroyed and self.sprite_destroyed is not None:
            overlay_sprite(frame, self.sprite_destroyed, self.pos, self.destroyed_size)
        elif self.sprite_alive is not None:
            overlay_sprite(frame, self.sprite_alive, self.pos, self.size)

    def check_hit(self, hand_pos, speed, threshold=20):
        if hand_pos and not self.destroyed:
            cx, cy = hand_pos
            dist = ((cx - self.pos[0])**2 + (cy - self.pos[1])**2)**0.5
            if dist < self.size//2 + 30 and speed > threshold:
                self.destroyed = True
                self.destroy_timer = 15
                return True
        return False
