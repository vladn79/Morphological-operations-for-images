import cv2
import numpy as np

def custom_dilation_cross(image, n, m):
    image_height, image_width = image.shape
    result = np.zeros((image_height, image_width), dtype=np.uint8)

    for i in range(n//2, image_height - n//2):
        for j in range(m//2, image_width - m//2):
            roi = image[i - n//2: i + n//2 + 1, j - m//2: j + m//2 + 1]
            if np.any(roi[n//2, :] == 255) or np.any(roi[:, m//2] == 255):
                result[i, j] = 255

    return result

def custom_dilation_rectangle(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    border_height = kernel_height // 2
    border_width = kernel_width // 2

    result = np.zeros((image_height, image_width), dtype=np.uint8)

    for i in range(border_height, image_height - border_height):
        for j in range(border_width, image_width - border_width):
            roi = image[i - border_height: i + border_height + 1, j - border_width: j + border_width + 1]

            result[i, j] = np.max(roi * kernel)

    return result

def custom_dilation_circular(image, radius):
    image_height, image_width = image.shape
    result = np.zeros((image_height, image_width), dtype=np.uint8)

    custom_radius = radius - 3  

    kernel = np.zeros((2*custom_radius+1, 2*custom_radius+1), dtype=np.uint8)
    cv2.circle(kernel, (custom_radius, custom_radius), custom_radius, 1, -1)

    for i in range(custom_radius, image_height - custom_radius):
        for j in range(custom_radius, image_width - custom_radius):
            roi = image[i - custom_radius: i + custom_radius + 1, j - custom_radius: j + custom_radius + 1]

            if np.any(cv2.bitwise_and(roi, kernel) != 0): 
                result[i, j] = 255

    return result


image = cv2.imread('1241241241412343.bmp', cv2.IMREAD_GRAYSCALE)
rectangle_kernel = np.ones((7, 3), dtype=np.uint8)
custom_dilated_rectangle = custom_dilation_rectangle(image, rectangle_kernel)
cv2_dilated_rectangle = cv2.dilate(image, rectangle_kernel)

custom_dilated_cross = custom_dilation_cross(image, 7, 5)
opencv_dilated_cross = cv2.dilate(image, cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 5)), iterations=1)

custom_dilated_circular = custom_dilation_circular(image, 5)
opencv_dilated_circular = cv2.dilate(image, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=1)
cv2.imshow('Custom Dilation Rectangle Kernel', custom_dilated_rectangle)
cv2.imshow('OpenCV Dilation Rectangle Kernel', cv2_dilated_rectangle)

cv2.imshow('Custom Dilation Cross Kernel', custom_dilated_cross)
cv2.imshow('OpenCV Dilation Cross Kernel', opencv_dilated_cross)

cv2.imshow('Custom Dilation Circular Kernel', custom_dilated_circular)
cv2.imshow('OpenCV Dilation Circular Kernel', opencv_dilated_circular)

cv2.waitKey(0)
cv2.destroyAllWindows()
