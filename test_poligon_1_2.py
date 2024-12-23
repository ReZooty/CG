import matplotlib.pyplot as plt
import time
import random

###############################COD1#################################

def clip_line(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    if (x1 < xmin and x2 < xmin) or (x1 > xmax and x2 > xmax) or (y1 < ymin and y2 < ymin) or (y1 > ymax and y2 > ymax):
        return None
    clipped_points = [[x1, y1], [x2, y2]]
    for i in range(2):
        x, y = clipped_points[i]
        if x < xmin:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin
        elif x > xmax:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        if y < ymin:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif y > ymax:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        clipped_points[i] = [x, y]
    if (clipped_points[0][0] < xmin and clipped_points[1][0] < xmin) or (clipped_points[0][0] > xmax and clipped_points[1][0] > xmax):
        return None
    return clipped_points[0][0], clipped_points[0][1], clipped_points[1][0], clipped_points[1][1]


def test_cod1(lines, xmin, ymin, xmax, ymax):
    start = time.perf_counter()
    clipped_lines = []
    for line in lines:
        result = clip_line(*line, xmin, ymin, xmax, ymax)
        if result:
            clipped_lines.append(result)
    finish = time.perf_counter()
    return finish - start, len(clipped_lines)

###############################COD2#################################

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8
def region_code(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    if x < x_min: code |= LEFT
    elif x > x_max: code |= RIGHT
    if y < y_min: code |= BOTTOM
    elif y > y_max: code |= TOP
    return code

def sutherland_cohen(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = region_code(x1, y1, x_min, y_min, x_max, y_max)
    code2 = region_code(x2, y2, x_min, y_min, x_max, y_max)
    while True:
        if code1 == 0 and code2 == 0:
            return x1, y1, x2, y2
        elif code1 & code2 != 0:
            return None
        else:
            if code1 != 0: code_out = code1
            else: code_out = code2
            if code_out & TOP: x, y = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1), y_max
            elif code_out & BOTTOM: x, y = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1), y_min
            elif code_out & RIGHT: x, y = x_max, y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            elif code_out & LEFT: x, y = x_min, y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
            if code_out == code1: x1, y1, code1 = x, y, region_code(x, y, x_min, y_min, x_max, y_max)
            else: x2, y2, code2 = x, y, region_code(x, y, x_min, y_min, x_max, y_max)


def test_cod2(lines, x_min, y_min, x_max, y_max):
    start = time.perf_counter()
    clipped_lines = []
    for line in lines:
        result = sutherland_cohen(*line, x_min, y_min, x_max, y_max)
        if result:
            clipped_lines.append(result)
    finish = time.perf_counter()
    return finish - start, len(clipped_lines)


def generate_lines(num_lines, xmin, ymin, xmax, ymax):
    lines = []
    for _ in range(num_lines):
        x1, y1 = random.randint(xmin - 50, xmax + 50), random.randint(ymin - 50, ymax + 50)
        x2, y2 = random.randint(xmin - 50, xmax + 50), random.randint(ymin - 50, ymax + 50)
        lines.append((x1, y1, x2, y2))
    return lines


xmin, ymin, xmax, ymax = 50, 10, 150, 100
num_lines = 10000000 


lines = generate_lines(num_lines, xmin, ymin, xmax, ymax)


time_cod1, clipped_cod1 = test_cod1(lines, xmin, ymin, xmax, ymax)
print(f"Время работы cod1: {time_cod1:.4f} секунд, Отсеченные линии: {clipped_cod1}")

time_cod2, clipped_cod2 = test_cod2(lines, xmin, ymin, xmax, ymax)
print(f"Время работы cod2: {time_cod2:.4f} секунд, Отсеченные линии: {clipped_cod2}")
