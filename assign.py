import numpy as np
import matplotlib.pyplot as plt

chain_code = ''
with open('flower_chain_code.txt', encoding='utf-8') as f:
    for line in f:
        chain_code = line

chain_code = list(chain_code)
img = np.zeros((500, 500))

x, y = 250, 250
for d in chain_code:
    if d == '0':
        x = x - 1
        y = y + 1
        img[y][x] = 255
    elif d == '1':
        y = y + 1
        img[y][x] = 255
    elif d == '2':
        x = x + 1
        y = y + 1
        img[y][x] = 255
    elif d == '3':
        x = x + 1
        img[y][x] = 255
    elif d == '4':
        x = x + 1
        y = y - 1
        img[y][x] = 255
    elif d == '5':
        y = y - 1
        img[y][x] = 255
    elif d == '6':
        x = x - 1
        y = y - 1
        img[y][x] = 255
    elif d == '7':
        x = x - 1
        img[y][x] = 255

plt.imshow(img)
plt.show()
