import cv2
import numpy as np


from erosion import custom_erosion_circular, custom_erosion_rectangle, custom_erosion_cross
from delation import custom_dilation_circular, custom_dilation_cross, custom_dilation_rectangle


def custom_opening_circle(image, radius):
    eroded_image = custom_erosion_circular(image, radius)
    opened_image = custom_dilation_circular(eroded_image, radius)
    return opened_image

def custom_opening_rectangle(image, kernel):
      eroded_image = custom_erosion_rectangle(image, kernel)
      opened_image = custom_dilation_rectangle(eroded_image, kernel)
      return opened_image

def custom_opening_cross(image, n, m):
      eroded_image = custom_erosion_cross(image, n, m)
      opened_image = custom_dilation_cross(eroded_image, n, m)
      return opened_image

def show_opening_circle(image, m):
      custom_opened_image = custom_opening_circle(image, m)
      opencv_opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (m, m)))
      cv2.imshow('Custom Circle Opening', custom_opened_image)
      cv2.imshow('OpenCV Circle Opening', opencv_opened_image)
      cv2.imshow('Custom Circle Opening', custom_opened_image)
      cv2.imshow('OpenCV Circle Opening', opencv_opened_image)

def show_opening_rectangle(image, n, m):
      rectangle_kernel = np.ones((n, m), dtype=np.uint8)
      c = custom_opening_rectangle(image, rectangle_kernel)
      c1 = cv2.morphologyEx(image, cv2.MORPH_OPEN, rectangle_kernel)
      cv2.imshow('Custom Rectangle Opening', c)
      cv2.imshow('OpenCV Rectangle Opening', c1)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

def show_opening_cross(image, n, m):
      c2 = custom_opening_cross(image, n, m)
      c3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_CROSS, (m, n)))
      cv2.imshow('Custom Cross Opening', c2)
      cv2.imshow('OpenCV Cross Opening', c3)
      cv2.waitKey(0)
      cv2.destroyAllWindows()






     
#kernel_radius = 5
#
#custom_opened_image = custom_opening_circle(image, kernel_radius)
#rectangle_kernel = np.ones((7, 3), dtype=np.uint8)
#opencv_opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_radius, kernel_radius)))
#c = custom_opening_rectangle(image, rectangle_kernel)
#
#c1 = cv2.morphologyEx(image, cv2.MORPH_OPEN, rectangle_kernel)
#
#c2 = custom_opening_cross(image, 5, 7)
#
#c3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 5)))
#
#cv2.imshow('Custom Circle Opening', custom_opened_image)
#cv2.imshow('OpenCV Circle Opening', opencv_opened_image)
#
#cv2.imshow('Custom Rect Opening', c)
#cv2.imshow('OpenCV Rect Opening', c1)
#
#cv2.imshow('Custom Cross Opening', c2)
#cv2.imshow('OpenCV Cross Opening', c3)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()