#Import libaries
import numpy as np
from scipy import integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


#both equations below
print("Equation 1: y'' + 2y' + 2 = 2x; t >= 0; y(0) = y'(0) = 0 ")

print("Equation 2: y'' + y = 4; t >= 0; y(0) = y'(0) = 0 ")
print("")

#fucntion to figure out what case of the homogeneous
def Homogeneous(a, b, c):
    if(b * b - (4 * a * c)) > 0:
        ansX = -b + math.sqrt((b * b) - (4 * a * c))
        answerX = ansX / (2 * a)
        ansY = -b - math.sqrt((b * b) - (4 * a * c))
        answerY = ansY / (2 * a)
        print("Case 1: ")
        print("(", answerX, ",", answerY, ")")
        print(" y(x) = c1 e^", answerX, "x + ", "c2 e^", answerY, "x")
        return answerX, answerY
    elif(b * b - (4 * a * c)) == 0:
        ans = -b + math.sqrt((b * b) - (4 * a * c))
        answer = ans / (2 * a)
        print("Case 2: ")
        print("(", answer, ",", answer, ")")
        print(" y(x) = c1 e^", answer, "x + ", "c2 e^", answer, "x")
        return
    elif(b * b - (4 * a * c)) < 0:
        sqrtx = ((b * b) - (4 * a * c))
        ansXX = -b + (.5 * sqrtx)
        answerXX = ansXX / (2 * a)
        sqrty = ((b * b) - (4 * a * c))
        ansYY = -b - (.5 * sqrty)
        answerYY = ansYY / (2 * a)
        print("Case 3: ")
        print("(", answerXX, "i , ", answerYY, "i", ")")
        print(" y(x) = e**[c1 cos(", answerXX, "x) + ", "c2 sin(", answerYY, "x)]")
        print(" ")
        return



#Enter the two homogeneous solutions
print("Equation 1 solved: ")
print(Homogeneous(1, 2, 0))
print("")
print("Equation 2 solved: ")
print(Homogeneous(1, 0, 1))
print("")

#plotting equation 2 greens fucntion soltuion
x1Array = []
y1Array = []

for x in range(1, 5):
    for y in range(1, 5):
        equation = 4 + math.cos(y)
        x1Array.append(x)
        y1Array.append(equation)
plt.plot(x1Array, y1Array)
plt.title('Greens Function y(t) 2 ')

plt.show()
#plotting equation 1 greens fucntion soltuion

x2Array = []
y2Array = []

for x in range(1, 5):
    for y in range(1, 5):
        equ = 2 * x
        equation = .25 * (2 * (x * x) - (2 * x) - 1 - (math.e ** - equ))
        x2Array.append(x)
        y2Array.append(equation)
plt.plot(x2Array, y2Array)
plt.title('Greens Function y(t) 1 ')

plt.show()
