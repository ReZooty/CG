import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
import numpy as np

def draw_line(img, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        img.putpixel((x0, y0), color)
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def draw_grid(img, step, color):
    width, height = img.size
    
    for x in range(0, width, step):
        draw_line(img, x, 0, x, height-1, color)
    
    for y in range(0, height, step):
        draw_line(img, 0, y, width-1, y, color)

x0 = int(input("x0-coordinate: "))
y0 = int(input("y0-coordinate: "))
x1 = int(input("x1-coordinate: "))
y1 = int(input("y1-coordinate: "))
img = Image.new('RGB', (1000, 900), 'white')
draw_grid(img, 50, (200, 200, 200)) 
draw_line(img, x0, y0, x1, y1, (0, 0, 0))
imshow(np.asarray(img))
plt.show()
img.save('Linia.png')
