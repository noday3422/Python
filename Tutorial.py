import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

class Man:
    def __init__(self, name):
        self.name=name
        print("Initialized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye "+ self.name + "!")

    def studyArray(self):
        x = np.array([1.0, 2.0, 3.0])
        y = np.array([2.0, 4.0, 6.0])
        print(len(x))
        print(x+y)
        print(x-y)
        print(x*y)
        print(x/y)
        print(x/2.0)

    def studyNArray(self):
        A = np.array([[1,2],[3,4]])
        print(A)
        print(A.shape)
        print(A.dtype)
        B = np.array([[3,0],[0,6]])
        print(A+B)
        print(A*B)
        print(A*10)

    def studyBasicMatrix(self):
        A = np.array([[1,2],[3,4]])
        B = np.array([10,20])
        C = np.array([[10],[20]])
        print(A)
        print(B)
        X = A*B
        print(X)
        for row in X:
            print(row)
        X = X.flatten()
        print(X)
        print(X>15)
        print(X[X>15])

    def studyPlot(self):
        #データ作成
        x = np.arange(0, 6, 0.1) #0から6まで0.1刻みで配列生成
        #print(x)
        y1 = np.sin(x)
        y2 = np.cos(x)
        plt.plot(x, y1, label = "sin")
        plt.plot(x, y2, linestyle="--", label="cos")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("sin & cos")
        plt.legend()
        plt.show()

    def studyPlotImage(self):
        #これだけちゃんと動いてくんない。
        img = imread('./IMG_0794.JPG')
        plt.imshow(img)

m = Man("Daisuke")
m.hello()
#m.studyArray()
#m.studyNArray()
#m.studyBasicMatrix()
#m.studyPlot()
m.studyPlotImage()
m.goodbye()