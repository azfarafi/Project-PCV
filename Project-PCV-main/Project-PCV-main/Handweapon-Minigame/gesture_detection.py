import cv2
import config

def detect_blue_object(mask, frame):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > config.AREA_THRESHOLD:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            cx, cy = x + w//2, y + h//2
            cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)
            return (cx, cy)
    return None


