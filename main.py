import eel
import re
import cv2
from erosion import show_erosion_circle, show_erosion_rectangle, show_erosion_cross
from delation import show_dilation_circle, show_dilation_cross, show_dilation_rectangle
from closing import show_closing_circle, show_closing_cross, show_closing_rectangle
from opening import show_opening_circle, show_opening_cross, show_opening_rectangle

results_array = []


image_path = '1241241241412343.bmp'




image =cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)



@eel.expose
def add_result_to_array(shape, result, result1):
      numbers_in_brackets = re.findall(r'\(([\d,]+)\)', shape)
      if numbers_in_brackets:
            numbers = [int(num) for num in numbers_in_brackets[0].split(',')]
            results_array.extend(numbers)

            shape = re.sub(r'\(\d+,\s*\d+\)', '', shape)
            shape = re.sub(r'\(\d+\)', '', shape)
      results_array.append(result)
      results_array.append(shape)
      
      if ('Erosion' in results_array) and ('Circle' in results_array):
            show_erosion_circle(image, results_array[0])
            results_array.clear()
      if ('Erosion' in results_array) and ('Rectangle' in results_array):
            show_erosion_rectangle(image, results_array[0], results_array[1])
            results_array.clear()

      if ('Erosion' in results_array) and ('Cross' in results_array):
            show_erosion_cross(image, results_array[0], results_array[1])
            results_array.clear()


      if ('Dilation' in results_array) and ('Circle' in results_array):
            show_dilation_circle(image, results_array[0])
            results_array.clear()
      if ('Dilation' in results_array) and ('Rectangle' in results_array):
            show_dilation_rectangle(image, results_array[0], results_array[1])
            results_array.clear()
      if ('Dilation' in results_array) and ('Cross' in results_array):
            show_dilation_cross(image, results_array[0], results_array[1])
            results_array.clear()


      if ('Closing' in results_array) and ('Circle' in results_array):
            show_closing_circle(image, results_array[0])
            results_array.clear()

      if ('Closing' in results_array) and ('Rectangle' in results_array):
            show_closing_rectangle(image, results_array[0], results_array[1])
            results_array.clear()
      if ('Closing' in results_array) and ('Cross' in results_array):
            show_closing_cross(image, results_array[0], results_array[1])
            results_array.clear()


      if ('Opening' in results_array) and ('Circle' in results_array):
            show_opening_circle(image, results_array[0])
            results_array.clear()
      if ('Opening' in results_array) and ('Rectangle' in results_array):
            show_opening_rectangle(image, results_array[0], results_array[1])
            results_array.clear()
      if ('Opening' in results_array) and ('Cross' in results_array):
            show_opening_cross(image, results_array[0], results_array[1])
            results_array.clear()
      


      



      
      
      
      



      print(results_array)



# Функція для отримання масиву результатів
@eel.expose
def get_results_array():
    return results_array





    

eel.init('web')
eel.start('index.html', size=(800, 800))