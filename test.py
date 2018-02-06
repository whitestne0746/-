import numpy as np
import matplotlib.pyplot as plt

Ref_CIX = np.array([[1, 1, 0, -1, -1, -1, 0, 1]])
Ref_CIY = np.array([[0, 1, 1, 1, 0, -1, -1, -1]])

# CI = np.array([[2, 2, 1, 7, 6, 6, 4, 4]])
CI = np.array([[2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 0, 0, 0, 0]])

size = np.shape(CI)

CIX = np.zeros(size)
CIY = np.zeros(size)
YI = np.zeros(size)
A = np.zeros(size)
# print(Ref_CIX[0])

img = np.zeros((7, 7))

for i in range(size[1]):
    CIX[0][i] = Ref_CIX[0][CI[0][i]]
    CIY[0][i] = Ref_CIY[0][CI[0][i]]


xx, yy = 5, 1
for i in range(len(CIX[0])):
    img[yy][xx] = 255
    xx += int(CIX[0][i])
    yy += int(CIY[0][i])

'''
for i in range(size[1]):
    if i != 0:
        YI[0][i] = YI[0][i - 1] + CIY[0][i]
        A[0][i] = CIX[0][i] * (YI[0][i - 1] + CIY[0][i] / 2)
    else:
        YI[0][i] = 0 + CIY[0][i]
        A[0][i] = CIX[0][i] * (0 + CIY[0][i] / 2)
'''
for i in range(size[1] - 1):
    A[0][i] = CIX[0][i] * CIY[0][i + 1] - CIX[0][i + 1] * CIY[0][i]

print(CIX)
print(CIY)
print(A)
print(abs(sum(A[0])))

plt.imshow(img, 'gray')
plt.show()
