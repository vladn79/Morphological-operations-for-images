import cv2
import numpy as np

def custom_erosion(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    border_height = kernel_height // 2
    border_width = kernel_width // 2

    result = np.zeros((image_height, image_width), dtype=np.uint8)

    # Проводимо ерозію
    for i in range(border_height, image_height - border_height):
        for j in range(border_width, image_width - border_width):
            roi = image[i - border_height: i + border_height + 1, j - border_width: j + border_width + 1]

            result[i, j] = np.min(roi * kernel)

    return result
image = cv2.imread('1241241241412343.bmp', cv2.IMREAD_GRAYSCALE)

rectangle_kernel = np.ones((7, 3), dtype=np.uint8)

custom_eroded_rectangle = custom_erosion(image, rectangle_kernel)

cv2_eroded_rectangle = cv2.erode(image, rectangle_kernel)

# Відображення результатів порівняння
cv2.imshow('Custom Erosion Rectangle Kernel', custom_eroded_rectangle)
cv2.imshow('OpenCV Erosion Rectangle Kernel', cv2_eroded_rectangle)

cv2.waitKey(0)
cv2.destroyAllWindows()
