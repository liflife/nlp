import matplotlib.pyplot as plt
from wordcloud import WordCloud
import PIL.Image as Image
import os
import numpy as np

import jieba
import math
arr1 = np.array([[0,3], [0, 4]]) # type:np.ndarray
arr2 = np.array([[1, 1], [2, 2]])
print(type(arr1))

print(arr1)
print(arr2)
print('dot:',arr1.dot(arr2))

arr3 = np.arange(0,10,2)  # type:np.ndarray
print('arrs3',arr3)

my_array = np.array([1, 2, 3, 4, 5])
print (my_array.shape)

# x是一个数组
x = np.arange(0, np.pi / 2, 0.1)
y = np.sin(x)

print("narray:", x, y)

# animals = ['cat','dog','monkey']
animals = ['cat','cat','dog','monkey']
for idx,animal in enumerate(animals):
    print('%d,%s' %(idx,animal))

# import matplotlib.pyplot as plt
#
# a = np.linspace(0, 2 * np.pi, 50)
# b = np.sin(a)
# plt.plot(a,b)
# mask = b >= 0
# plt.plot(a[mask], b[mask], 'bo')
# mask = (b >= 0) & (a <= np.pi / 2)
# plt.plot(a[mask], b[mask], 'go')
# plt.show()

# x=np.arange(0,2*np.pi,0.01)
# x=np.arange(0,180*3,1)
# x1=[math.radians(i) for i in x ]
# y=np.sin(x1)
# y1=np.sin(x1)*3
# y3=np.sin(x1)*-3
# y2=np.sin(x1)*-1
# y=np.sin(x)
# print(x)
# print(y)
# # print('a:%s' % math.radians(1))
# plt.plot(x,y)
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.plot(x,y3)
# plt.show()


array = np.asarray(allBigPng, dtype=np.uint8)
image = Image.fromarray(array, 'RGBA')
image.save(outputImgPath + pollutionName + '.png')
