import numpy as np
import matplotlib.pyplot as plt

def scalar_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def cyrus_beck(line_start, line_end, polygon):
    d = np.array(line_end) - np.array(line_start)  
    t_enter, t_exit = 0, 1  
    for i in range(len(polygon)):
        p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
        edge = np.array(p2) - np.array(p1)
        normal = np.array([-edge[1], edge[0]]) 
        w = np.array(line_start) - np.array(p1)  
        numerator = -scalar_product(w, normal)  
        denominator = scalar_product(d, normal)  
        
        if denominator != 0:
            t = numerator / denominator  
            if denominator > 0:
                t_enter = max(t_enter, t)  
            else:
                t_exit = min(t_exit, t)  
            
            if t_enter > t_exit:
                return None  
    if t_enter <= t_exit:
        return line_start + t_enter * d, line_start + t_exit * d
    return None

def plot_clip(lines, polygon):
    fig, ax = plt.subplots()
    polygon.append(polygon[0])  
    polygon = np.array(polygon)
    ax.plot(polygon[:, 0], polygon[:, 1], 'k-', lw=2)  

    for line in lines:
        start, end = line
        ax.plot([start[0], end[0]], [start[1], end[1]], 'r--')

    for line in lines:
        result = cyrus_beck(np.array(line[0]), np.array(line[1]), polygon[:-1].tolist())
        if result:
            clipped_start, clipped_end = result
            ax.plot([clipped_start[0], clipped_end[0]], [clipped_start[1], clipped_end[1]], 'g-', lw=2)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Cyrus-Beck Clipping')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    polygon = [[10, 10], [100, 30], [90, 100], [30, 90]]  
    lines = [([0, 0], [50, 50]), ([20, 80], [80, 20]), ([60, 60], [120, 120]), ([0, 100], [100, 0]), ([70, 10], [70, 120])]  # Отрезки
    plot_clip(lines, polygon)
