import os
import cv2
import numpy as np

def add_shadow(img, shadow_color=(0, 0, 0, 127)):
    h, w = img.shape[:2]
    shadow = np.zeros((h + h // 10, w + w // 10), dtype=np.uint8)
    shadow[h // 20:-h // 20, w // 20:-w // 20] = 255
    shadow = cv2.GaussianBlur(shadow, (0, 0), w // 20)
    shadow_color = np.array(shadow_color, dtype=np.uint8)
    shadow = cv2.addWeighted(shadow, 0.5, shadow_color, 0.5, 0)
    x, y = (w - shadow.shape[1]) // 2, (h - shadow.shape[0]) // 2
    img = cv2.copyMakeBorder(img, y, y, x, x, cv2.BORDER_CONSTANT, value=shadow_color)
    return cv2.addWeighted(img, 1, shadow, 0.5, 0)

def add_rounded_corners(img, radius=30):
    h, w = img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (w // 2, h // 2), radius, (255, 255, 255), -1)
    masked = cv2.bitwise_and(img, img, mask=mask)
    return masked

def process_image(img_path):
    img = cv2.imread(img_path)
    shadowed = add_shadow(img)
    rounded = add_rounded_corners(shadowed)
    cv2.imwrite(img_path, rounded)

def process_images_in_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                img_path = os.path.join(root, file)
                process_image(img_path)

folder = "/Users/eyresimpson/截图"
process_images_in_folder(folder)
