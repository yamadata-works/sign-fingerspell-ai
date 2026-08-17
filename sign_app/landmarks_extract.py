
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

def extract_landmarks_from_image(path):
    img = cv2.imread(path)
    if img is None:
        return None

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if not result.multi_hand_landmarks:
        return None

    data = []
    lm = result.multi_hand_landmarks[0]
    for p in lm.landmark:
        data.extend([p.x, p.y, p.z])

    return data
