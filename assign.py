"""This is a test program."""

import numpy as np
import matplotlib.pyplot as plt


class Image:
    def __init__(self):
        self.img = np.zeros((300, 300))
        self.x, self.y = 225, 225
        self.chainCode = ''
        with open('flower_chain_code.txt', encoding='utf-8') as f:
            for line in f:
                self.chainCode = line
        self.chainCode = list(self.chainCode)
        self.area = 0

    def chain_code(self):
        self.img[self.y][self.x] = 255
        for d in self.chainCode:
            if d == '0':
                self.x = self.x - 1
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '1':
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '2':
                self.x = self.x + 1
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '3':
                self.x = self.x + 1
                self.img[self.y][self.x] = 255
            elif d == '4':
                self.x = self.x + 1
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
            elif d == '5':
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
            elif d == '6':
                self.x = self.x - 1
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
            elif d == '7':
                self.x = self.x - 1
                self.img[self.y][self.x] = 255

    def show(self):
        print(self.area)
        plt.imshow(self.img, 'gray')

    def calculate_area(self):
        for y in range(self.img.shape[0]):
            pos = []
            for x in range(self.img.shape[1]):
                if self.img[y][x] == 255:
                    pos.append((x, y))
            if len(pos) == 1:
                self.area += 1
            elif len(pos) == 2:
                self.area += pos[1][0] - pos[0][0]
            print(len(pos))


img = Image()
img.chain_code()
img.calculate_area()
img.show()

plt.show()
