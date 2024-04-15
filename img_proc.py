import cv2

# Завантаження зображення
image = cv2.imread('original-zhivotnye_5.jpg')


# Перетворення зображення в чорно-білий з використанням порогу
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Збереження чорно-білого зображення у форматі BMP
cv2.imwrite('output_image.bmp', binary_image)

