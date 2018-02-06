"""This is a test program."""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
from PIL import Image
from PIL import ImageDraw


class Chain:
    def __init__(self):
        self.count = 0
        self.img = np.zeros((256, 256))
        self.x, self.y = 120, 220
        self.chainCode = ''
        with open('flower_chain_code.txt', encoding='utf-8') as f:
            for line in f:
                self.chainCode = line
        self.chainCode = list(self.chainCode)
        # self.chainCode = ['0', '0', '0', '2', '2', '2', '4', '4', '4', '6', '6', '6']
        self.area = 0
        self.Ref_CIX = np.array([[1, 1, 0, -1, -1, -1, 0, 1]])
        self.Ref_CIY = np.array([[0, 1, 1, 1, 0, -1, -1, -1]])

    def chain_code(self):
        self.img[self.y][self.x] = 255
        for d in self.chainCode:
            if d == '0':
                self.x = self.x + 1
                self.img[self.y][self.x] = 255
            elif d == '1':
                self.x = self.x + 1
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '2':
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '3':
                self.x = self.x - 1
                self.y = self.y + 1
                self.img[self.y][self.x] = 255
            elif d == '4':
                self.x = self.x - 1
                self.img[self.y][self.x] = 255
            elif d == '5':
                self.x = self.x - 1
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
            elif d == '6':
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
            elif d == '7':
                self.x = self.x + 1
                self.y = self.y - 1
                self.img[self.y][self.x] = 255
        cv2.imwrite('img.png', self.img)

    def fill(self, x, y):
        '''
        self.img[y][x] = 150
        # self.count += 1
        # print('{}'.format(self.count))
        if self.img[y - 1][x] == 0:
            self.fill(x, y - 1)
        if self.img[y][x - 1] == 0:
            self.fill(x - 1, y)
        if self.img[y + 1][x] == 0:
            self.fill(x, y + 1)
        if self.img[y][x + 1] == 0:
            self.fill(x + 1, y)
        self.count += 1
        print('{}'.format(self.count))
        '''
        self.img = Image.open('./img.png')
        print(self.img)
        ImageDraw.floodfill(self.img, (x, y), (255, 0, 0), border=None)

    def show(self):
        print(self.img)
        plt.imshow(self.img, 'gray')
        plt.show()

    def calculate_area(self):
        size = (1, len(self.chainCode))
        CIX = np.zeros(size)
        CIY = np.zeros(size)
        YI = np.zeros(size)
        A = np.zeros(size)
        for i in range(size[1]):
            CIX[0][i] = self.Ref_CIX[0][int(self.chainCode[i])]
            CIY[0][i] = self.Ref_CIY[0][int(self.chainCode[i])]

        for i in range(size[1]):
            if i != 0:
                YI[0][i] = YI[0][i - 1] + CIY[0][i]
                A[0][i] = CIX[0][i] * (YI[0][i - 1] + CIY[0][i] / 2)
            else:
                YI[0][i] = 0 + CIY[0][i]
                A[0][i] = CIX[0][i] * (0 + CIY[0][i] / 2)

        print('chain code内の画素数: {}'.format(abs(sum(A[0]))))
        self.area = abs(sum(A[0])) + len(self.chainCode)
        print('chain codeも含めた画素数: {}'.format(self.area))


img = Chain()
img.chain_code()
img.fill(121, 44)
img.show()
# img.calculate_area()
