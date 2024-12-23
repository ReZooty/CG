import matplotlib.pyplot as plt
import numpy as np

def fill_area(vertices):
    x_min, x_max, y_min, y_max = min(vertices[:, 0]), max(vertices[:, 0]), min(vertices[:, 1]), max(vertices[:, 1])
    fill_points = []
    for y in range(int(y_min), int(y_max) + 1):
        intersections = []
        for i in range(len(vertices)):
            v1, v2 = vertices[i], vertices[(i + 1) % len(vertices)]
            if (v1[1] > y) != (v2[1] > y):
                x = (v2[0] - v1[0]) * (y - v1[1]) / (v2[1] - v1[1]) + v1[0]
                intersections.append(x)
        intersections.sort()
        for i in range(0, len(intersections), 2):
            fill_points.append((intersections[i], y))
            fill_points.append((intersections[i + 1], y))
    return fill_points

vertices = np.array([(1, 1), (5, 0.5), (4, 4), (2, 3), (1, 4)])
fill_points = fill_area(vertices)

plt.fill(vertices[:, 0], vertices[:, 1], 'lightgrey')
plt.xlim(0, 6); plt.ylim(0, 5)
plt.show()
