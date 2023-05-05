# PREPROCESSING IMAGES 

import numpy as np
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
from IPython.display import Image, display


def resizing_image(img, argument):
    '''
    1: Shrink
    2: Enlarge Cubic
    3: Enlager Linear
    '''
    switcher = {
        1: cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA),
        2: cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC),
        3: cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    }
    return switcher.get(argument, "Invalid method")


def threshold_image(img, argument):
    '''
    # 1. Binary-Otsu w/ Gaussian Blur (kernel size = 9)                               #
    # 2. Binary-Otsu w/ Gaussian Blur (kernel size = 7)                               #
    # 3. Binary-Otsu w/ Gaussian Blur (kernel size = 5)                               #
    # 4. Binary-Otsu w/ Median Blur (kernel size = 5)                                 #
    # 5. Binary-Otsu w/ Median Blur (kernel size = 3)                                 #
    # 6. Adaptive Gaussian Threshold (31,2) w/ Gaussian Blur (kernel size = 5)        #
    # 7. Adaptive Gaussian Threshold (31,2) w/ Median Blur (kernel size = 5)
    '''

    switcher = {
        1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        4: cv2.threshold(cv2.medianBlur(img, 5), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        5: cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        6: cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 31, 2),
        7: cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2),
    }
    return switcher.get(argument, "Invalid method")


def crop_image(img, start_x, start_y, end_x, end_y):
    cropped = img[start_y:end_y, start_x:end_x]
    return cropped


def preprocess_image(img, dict_preprocessing):
    img = np.array(img)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    if dict_preprocessing['cropping_image'] is True:
        # Crop the areas where provision number is more likely present
        img = crop_image(img, dict_preprocessing['pnr_area'][0], dict_preprocessing['pnr_area'][1],
                         dict_preprocessing['pnr_area'][2], dict_preprocessing['pnr_area'][3])
        img_show = Image.fromarray(img, 'RGB')
        display(img_show)

    # Rescale the image, if needed.
    if dict_preprocessing['resizing_image'] is True:
        img = resizing_image(img, dict_preprocessing['resizing_method'])
        img_show = Image.fromarray(img, 'RGB')
        display(img_show)

    # Apply blurring and thresholding
    if dict_preprocessing['thresholding_image']  is True:
        img = threshold_image(img, dict_preprocessing['thresholding_method'])
        img_show = Image.fromarray(img, 'RGB')
        display(img_show)

    return img
