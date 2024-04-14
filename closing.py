import cv2
import numpy as np

from erosion import custom_erosion_circular, custom_erosion_rectangle, custom_erosion_cross
from delation import custom_dilation_circular, custom_dilation_cross, custom_dilation_rectangle


def custom_closing_circle(image, radius):
    delated_image = custom_dilation_circular(image, radius)
    opened_image = custom_erosion_circular (delated_image, radius)
    return opened_image

def custom_closing_rectangle(image, kernel):
    delated_image = custom_dilation_rectangle(image, kernel)
    opened_image = custom_erosion_rectangle(delated_image, kernel)
    return opened_image

def custom_closing_cross(image, n, m):
    delated_image = custom_dilation_cross(image, n, m)
    opened_image = custom_erosion_cross (delated_image, n, m)
    return opened_image

def show_closing_circle(image, m):
    custom_opened_image = custom_closing_circle(image, m)
    opencv_opened_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (m, m)))
    cv2.imshow('Custom Circle Closing', custom_opened_image)
    cv2.imshow('OpenCV Circle Closing', opencv_opened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_closing_rectangle(image, n, m):
    rectangle_kernel = np.ones((n, m), dtype=np.uint8)
    c = custom_closing_rectangle(image, rectangle_kernel)
    c1 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, rectangle_kernel)
    cv2.imshow('Custom Rectangle Closing', c)
    cv2.imshow('OpenCV Rectangle Closing', c1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_closing_cross(image, n, m):
    c2 = custom_closing_cross(image, n, m)
    c3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_CROSS, (m, n)))
    cv2.imshow('Custom Cross Closing', c2)
    cv2.imshow('OpenCV Cross Closing', c3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()









#image = cv2.imread('1241241241412343.bmp', cv2.IMREAD_GRAYSCALE)
#kernel_radius = 5
#
#custom_opened_image = custom_closing_circle(image, kernel_radius)
#rectangle_kernel = np.ones((7, 3), dtype=np.uint8)
#opencv_opened_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_radius, kernel_radius)))
#c = custom_closing_rectangle(image, rectangle_kernel)
#
#c1 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, rectangle_kernel)
#
#c2 = custom_closing_cross(image, 5, 7)
#
#c3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 5)))
#
#cv2.imshow('Custom Circle Closing', custom_opened_image)
#cv2.imshow('OpenCV Circle Closing', opencv_opened_image)
#
#cv2.imshow('Custom Rect Closing', c)
#cv2.imshow('OpenCV Rect Closing', c1)
#
#cv2.imshow('Custom Cross Closing', c2)
#cv2.imshow('OpenCV Cross Closing', c3)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()