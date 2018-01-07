import numpy as np

class perceptron:
    def AND(x1,x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1

    def NAND(x1,x2):
        w1, w2, theta = -0.5, -0.5, -0.7
        tmp = x1 * w1 + x2 * w2
        print('%s*%s+%s*%s<=%s->0' % (x1, w1, x2, w2, theta))
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1

    def OR(x1,x2):
        w1, w2, theta = 0.5, 0.5, 0.4
        tmp = x1 * w1 + x2 * w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1

p = perceptron
#print("----AND----")
#print(p.AND(0, 0))
#print(p.AND(0, 1))
#print(p.AND(1, 0))
#print(p.AND(1, 1))
#print("----NAND----")
#print(p.NAND(0, 0))
#print(p.NAND(0, 1))
#print(p.NAND(1, 0))
#print(p.NAND(1, 1))
print("----OR----")
print(p.OR(0, 0))
print(p.OR(0, 1))
print(p.OR(1, 0))
print(p.OR(1, 1))
