import time
import random
import numpy as np
import matplotlib.pyplot as plt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Функция для генерации случайного многоугольника
def generate_random_polygon(num_vertices):
    angles = np.sort(np.random.rand(num_vertices) * 2 * np.pi)  # Углы для вершин
    radius = 0.5  # Радиус многоугольника
    vertices = [(radius * np.cos(angle) + 0.5, radius * np.sin(angle) + 0.5) for angle in angles]
    return vertices

# Алгоритм заполнения многоугольника по граничным точкам
def fill_polygon(vertices):
    # Создание пустого поля
    x_min, x_max = min(vertices[:, 0]), max(vertices[:, 0])
    y_min, y_max = min(vertices[:, 1]), max(vertices[:, 1])

    # Список для заполнения
    fill_points = []

    # Проход по горизонтальным линиям
    for y in range(int(y_min * 500), int(y_max * 500) + 1):
        intersections = []

        # Находим пересечения с рёбрами
        for i in range(len(vertices)):
            v1, v2 = vertices[i], vertices[(i + 1) % len(vertices)]
            if (v1[1] > y / 500) != (v2[1] > y / 500):
                x = (v2[0] - v1[0]) * (y / 500 - v1[1]) / (v2[1] - v1[1]) + v1[0]
                intersections.append(x)

        # Сортируем пересечения
        intersections.sort()

        # Заполняем область
        for i in range(0, len(intersections), 2):
            fill_points.append((intersections[i], y / 500))
            fill_points.append((intersections[i + 1], y / 500))

    return fill_points

# Функция для инициализации окна OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Устанавливаем цвет фона
    glMatrixMode(GL_PROJECTION)  # Переходим в режим проекции
    glLoadIdentity()  # Сбрасываем матрицу проекции
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)  # Устанавливаем ортографическую проекцию

# Функция для рисования
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Очищаем буфер цвета
    glColor3f(1.0, 0.0, 0.0)  # Устанавливаем цвет рисования
    start_time = time.time()
    # Используем OpenGL для рисования многоугольника
    glBegin(GL_POLYGON)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()
    end_time = time.time()
    time_pyopengl = end_time - start_time
    print(f"Время выполнения метода из PyOpenGL: {time_pyopengl:.4f} секунд")
    glFlush()  # Обновляем буфер

def close_window():
    glutLeaveMainLoop()  # Завершает основной цикл GLUT

def keyboard(key, x, y):
    print(key)
    if key == b'\x1b':  # ESC key
        glutLeaveMainLoop()  # Завершает основной цикл GLUT

# Основная функция
if __name__ == "__main__":
    # Генерируем случайный многоугольник
    num_vertices = 10000  # Количество вершин многоугольника
    points = generate_random_polygon(num_vertices)

    # Преобразуем точки в массив NumPy
    vertices = np.array(points)

    # Измеряем время выполнения алгоритма заполнения многоугольника
    start_time = time.time()
    fill_points = fill_polygon(vertices)
    end_time = time.time()
    time_algorithm = end_time - start_time
    print(f"Время выполнения алгоритма заполнения многоугольника: {time_algorithm:.4f} секунд")

    # Визуализация заполнения многоугольника с помощью matplotlib
    plt.fill(vertices[:, 0], vertices[:, 1], 'lightgrey')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title("Заполнение многоугольника (matplotlib)")
    plt.show()

    # Инициализируем окно OpenGL
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'py')
    init()
    glutDisplayFunc(display)  # Устанавливаем функцию отрисовки
    glutKeyboardFunc(keyboard)
    glutCloseFunc(close_window)

    # Измеряем время выполнения метода из PyOpenGL
    glutMainLoop()  # Запускаем цикл отрисовки
