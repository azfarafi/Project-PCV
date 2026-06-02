import cv2
import numpy as np
import config

def get_blue_mask(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(config.LOWER_BLUE, dtype=np.uint8)
    upper_blue = np.array(config.UPPER_BLUE, dtype=np.uint8)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask_blue

def apply_morphology(mask):
    kernel = np.ones(config.KERNEL_SIZE, np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)
    return mask
