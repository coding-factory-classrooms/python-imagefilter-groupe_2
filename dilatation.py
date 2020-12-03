import cv2
import numpy as np
import os


def dilatation_pic(dossierE, dossierS):
    files = os.listdir(dossierE)
    kernel = np.ones((20, 20), np.uint8)

    for f in files:
        print(f)
        img = cv2.imread(f"{dossierE}/{f}")
        dilation = cv2.dilate(img, kernel, 20)
        cv2.imwrite(f"{dossierS}/{f}", dilation)
