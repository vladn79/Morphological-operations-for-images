import cv2
import numpy as np




def custom_erosion_cross(image, n, m):
    image_height, image_width = image.shape
    result = np.zeros((image_height, image_width), dtype=np.uint8)

    for i in range(n//2, image_height - n//2):
        for j in range(m//2, image_width - m//2):
            roi = image[i - n//2: i + n//2 + 1, j - m//2: j + m//2 + 1]
            if np.all(roi[n//2, :] == 255) and np.all(roi[:, m//2] == 255):
                result[i, j] = 255

    return result

def custom_erosion_rectangle(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    border_height = kernel_height // 2
    border_width = kernel_width // 2

    result = np.zeros((image_height, image_width), dtype=np.uint8)

    for i in range(border_height, image_height - border_height):
        for j in range(border_width, image_width - border_width):
            roi = image[i - border_height: i + border_height + 1, j - border_width: j + border_width + 1]

            result[i, j] = np.min(roi * kernel)

    return result

def custom_erosion_circular(image, radius):
    image_height, image_width = image.shape
    result = np.zeros((image_height, image_width), dtype=np.uint8)

    custom_radius = int(radius / 1.2)

    kernel = np.zeros((2*custom_radius+1, 2*custom_radius+1), dtype=np.uint8)
    cv2.circle(kernel, (custom_radius, custom_radius), custom_radius, 1, -1)

    for i in range(custom_radius, image_height - custom_radius):
        for j in range(custom_radius, image_width - custom_radius):
            roi = image[i - custom_radius: i + custom_radius + 1, j - custom_radius: j + custom_radius + 1]

            if np.sum(cv2.bitwise_and(roi, kernel)) == np.sum(kernel):
                result[i, j] = 255

    return result

def show_erosion_circle(image, m):
      custom_eroded_circular = custom_erosion_circular(image, m)
      opencv_eroded_circular = cv2.erode(image, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (m, m)), iterations=1)
      cv2.imshow('Custom Erosion Circular Kernel', custom_eroded_circular)
      cv2.imshow('OpenCV Erosion Circular Kernel', opencv_eroded_circular)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

def show_erosion_rectangle(image, n, m):
      rectangle_kernel = np.ones((n, m), dtype=np.uint8)
      custom_eroded_rectangle = custom_erosion_rectangle(image, rectangle_kernel)
      cv2_eroded_rectangle = cv2.erode(image, rectangle_kernel)
      cv2.imshow('Custom Erosion Rectangle Kernel', custom_eroded_rectangle)
      cv2.imshow('OpenCV Erosion Rectangle Kernel', cv2_eroded_rectangle)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

def show_erosion_cross(image, n, m):
    custom_eroded_cross = custom_erosion_cross(image, m, n)
    opencv_eroded_cross = cv2.erode(image, cv2.getStructuringElement(cv2.MORPH_CROSS, (n, m)), iterations=1)
    cv2.imshow('Custom Erosion Cross Kernel', custom_eroded_cross)
    cv2.imshow('OpenCV Erosion Cross Kernel', opencv_eroded_cross)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#