#Import libaries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import time

#creating our time funciton
start = time.time()
#initlizes our start values
x = 1.0
y = 2.0
h = 0.05

#the 1st kutta method defaniton
def k1st (x0, y0):
    k1 = model(x0, y0)
    return k1
#the 2nd kutta method defination
def k2nd (x0, y0, h , k1):
    x = x0 + (h / 2)
    y = y0 + ((h / 2) * k1)

    k2 = model(x, y)

    return k2
#the 3rd kutta method defination
def k3rd (x0, y0, h, k2):
    x = x0 + (h / 2)
    y = y0 + ((h / 2) * k2)

    k3 = model(x, y)

    return k3
#the 4th kutta method defination
def k4th (x0, y0 , h, k3):
    x = x0 + h
    y = y0 + (h * k3)

    k4 = model(x, y)

    return k4

#the model defination
def model (x, y):
    ans = y * math.exp(-x) - math.exp(-x)

    return ans

#the actualy kutta method that calls all the other method
def rungeKutta (x0, y0, h):
    ans1 = k1st(x0, y0)

    print ("k1st = " +str(ans1))

    ans2 = k2nd(x0, y0, h, ans1)

    print("k2nd = " + str(ans2))

    ans3 = k3rd(x0, y0, h, ans2)

    print("k3st = " + str(ans3))

    ans4 = k4th(x0, y0, h, ans3)

    print("k4th = " + str(ans4))

    ans = y0 + ((h / 6) * (ans1 + (2 * ans2) + (2 * ans3) + ans4))

    return ans

#taking the user input of iteration
iteration = input("Enter the amount of iteration: ")
#creating the fist and second iteration storage
iter = []

iter1 = []

plt.figure()

end = time.time()
print("\n It took: ")
print(end - start)
print("\n")

#using the input for an amout of iterations
for i in range(0, int(iteration)):
    y = rungeKutta(x, y, h)
    x = x + h
    iter.append(x)
    iter1.append(y)




    #run1 = odeint()
    plt.plot(iter, iter1)
plt.show()

for i in range(len(iter1)):
    print("\ny" + str(i + 1) + "= ")
    print(iter1[i])

end = time.time()
print("It took: ")
print(end - start)

