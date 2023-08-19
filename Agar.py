import matplotlib.pyplot as plt

# Ваши координаты
coordinates = [
    5, 5, 5, 0, 1, 0, 1, 2, 2, 3, 3, 3, 4, 3, 5, 3, 5, 0, 10, 0, 8, 1, 8,
    3, 10, 4, 12, 3, 12, 1, 10, 0, 10, 2, 10, 0, 15, 0, 15, 5, 15, 4, 14, 4,
    16, 4, 15, 4, 15, -1, 17, -2, 15, -1, 15, 0, 20, 0, 19, 1, 20, 0, 21, 1,
    20, 2, 19, 3, 20, 4, 21, 3, 20, 4, 19, 3, 21, 1, 20, 0, 30, 0, 30, 4, 31,
    5, 30, 4, 29, 4, 31, 4, 30, 4, 30, 0, 35, 0, 33, 1, 33, 3, 35, 4, 37, 3,
    37, 1, 35, 0, 40, 0, 40, 4, 41, 5, 40, 4, 40, 0, 50, 0, 48, 2, 50, 0, 52,
    2, 50, 0, 50, -1, 50, -2, 49, -3, 50, -2, 50, 0, 57, 0, 55, 1, 55, 3, 57,
    4, 59, 3, 59, 1, 57, 0, 57, 2, 57, 0, 65, 0, 65, 4, 65, 0, 64, 0, 63, 1, 63, 2, 63, 3
]

# Разделение координат на пары (x, y)
x_coords = coordinates[::2]
y_coords = coordinates[1::2]

# Создание графика
plt.plot(x_coords, y_coords, marker='o')
plt.title("График по заданным координатам")
plt.xlabel("X координата")
plt.ylabel("Y координата")
plt.grid(True)
plt.show()