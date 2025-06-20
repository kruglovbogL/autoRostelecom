import cv2
import numpy as np
from tempfile import TemporaryFile









# Загрузка изображения
image_path = 'target.png'
image = cv2.imread(image_path)

# Проверка, загрузилось ли изображение
if image is None:
    raise ValueError("Не удалось загрузить изображение. Проверьте путь.")

# Получаем размеры изображения
height, width, _ = image.shape

# Определяем размеры фрагмента (например, 100x100 пикселей)
fragment_size = 125

# Вычисляем координаты центрального фрагмента
start_x = (width - fragment_size) // 2 - 72
start_y = (height - fragment_size) // 2 + 230

# Вырезаем фрагмент изображения
fragment = image[start_y:start_y + fragment_size, start_x:start_x + fragment_size]

# Преобразуем его в массив NumPy
fragment_array = np.array(fragment)
np.save('test3.npy',fragment_array)    # .npy extension is added if not given
d = np.load('test3.npy')
print(d)
# print(fragment_array == d)
# array([ True,  True,  True,  True], dtype=bool)



print(len(fragment_array))



# with open('file.txt','a')as f:
#     print(fragment_array, file=f)

# if fragment_array == enemy:
#     pass
# Отображаем фрагмент
cv2.imshow('Fragment', fragment)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Выводим массив NumPy
print(fragment_array)
