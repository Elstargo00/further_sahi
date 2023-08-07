import cv2
import os
import numpy as np

def remove_white(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(dir_path, filename)
            image = cv2.imread(img_path)
            # If less than 95% of the pixels are white, move on to the next image
            if np.mean(image < 255) > 0.05:
                continue
            # If more than 95% of the pixels are white, remove the image
            os.remove(img_path)
            print(f"Removed: {img_path}")


def remove_black(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(dir_path, filename)
            image = cv2.imread(img_path)
            # If less than 95% of the pixels are white, move on to the next image
            if np.mean(image > 0) > 0.05:
                continue
            # If more than 95% of the pixels are white, remove the image
            os.remove(img_path)
            print(f"Removed: {img_path}")

def remove_twotone(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(dir_path, filename)
            image = cv2.imread(img_path)
            # If less than 95% of the pixels are white, move on to the next image
            if np.mean(image > 0) + np.mean(image < 255) > 0.05:
                continue
            # If more than 95% of the pixels are white, remove the image
            os.remove(img_path)
            print(f"Removed: {img_path}")  

