import numpy as np
import matplotlib.pyplot as plt


def f1(x):
    if x!=0:
        y =  np.sin(x)/np.log(x)
        return y
    else:
        return 0


def f2(x):
    return x**3+2*(x**2)+x

#Sin/ln
def PochSinLn(arrX, krok):
    y1 = []
    y2 = []
    for x in arrX:
        fy = (x+krok)
        fx = (x-krok)
        deltaF = (f1(fy)-f1(fx))/(2*krok)
        y1.append(float(deltaF))
        y2.append(float(f1(x)))
    return [y1,y2]

#x^3+2x^2+x
def PochY(arrX, krok):
    y1 = []
    y2 = []
    for x in arrX:
        fy = (x+krok)
        fx = (x-krok)
        deltaF = (f2(fy)-f2(fx))/(2*krok)
        y1.append(float(deltaF))
        y2.append(float(f2(x)))
    return [y1,y2]

#Sin/ln
x1 =np.linspace(0,10,10)
x1 = x1.tolist()
x1.remove(0)
y1p,y1 = PochSinLn(x1, 10/10)


#x^3+2x^2+x
x2 =np.linspace(-10,10,2000)
y2p,y2 = PochY(x2, 10/1000)

plt.plot(x1, y1,label = "f(x)", color = "blue",marker='o', linestyle='-', markersize=2)
plt.plot(x1, y1p,label = "f '(x)", color = "orange", marker='o', linestyle='-', markersize=2)
plt.xlabel('X')
plt.ylabel('f(x)')
plt.title("f(x) = sin(x)/ln(x)")
plt.ylim(-10,10)
plt.grid(True)
plt.legend()
plt.savefig("sinln0.png")
plt.show()



plt.plot(x2, y2,label = "f(x)", color = "blue",marker='o', linestyle='-', markersize=2)
plt.plot(x2, y2p,label = "f '(x)", color = "orange", marker='o', linestyle='-', markersize=2)
plt.xlabel('Współrzędna X')
plt.ylabel('Współrzędna Y')
plt.title("f(x) = x^3+2x^2+x")
plt.grid(True)
plt.legend()
plt.savefig("xpot2.png")
plt.show()

