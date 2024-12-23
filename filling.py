import matplotlib.pyplot as plt
import numpy as np

def fill_polygon(vertices):
    # Sozdaniye pustogo polya
    x_min, x_max = min(vertices[:, 0]), max(vertices[:, 0])
    y_min, y_max = min(vertices[:, 1]), max(vertices[:, 1])
    
    # Spisok 4 zapolneniya
    fill_points = []
    
    # Prohod po gorizontal lines
    for y in range(int(y_min), int(y_max) + 1):
        intersections = []
        
        # Nahodim peresecheniya s ryobrami
        for i in range(len(vertices)):
            v1, v2 = vertices[i], vertices[(i + 1) % len(vertices)]
            if (v1[1] > y) != (v2[1] > y):
                x = (v2[0] - v1[0]) * (y - v1[1]) / (v2[1] - v1[1]) + v1[0]
                intersections.append(x)
        
        # Sortirue, peresecheniya
        intersections.sort()
        
        # Zapolnyaem Oblast'
        for i in range(0, len(intersections), 2):
            fill_points.append((intersections[i], y))
            fill_points.append((intersections[i + 1], y))
    
    return fill_points

# Vershini
vertices = np.array([(1, 1), (5, 0.5), (4, 4), (2, 3), (1, 4)])
fill_points = fill_polygon(vertices)

# Visualizatsia
plt.fill(vertices[:, 0], vertices[:, 1], 'lightgrey')
plt.xlim(0, 6)
plt.ylim(0, 5)
plt.show()