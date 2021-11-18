import math

def sqr(a):
    return a * a

a = float(input("Enter the side length that is opposite of the angle you want: "))
b = float(input("Enter one of the other sides. It does not matter which: "))
c = float(input("Enter one of the other sides. It does not matter which: "))

top = (sqr(a))-(sqr(b))-(sqr(c))
bottom = ((-2.0)*(b)*(c))

print (math.degrees((math.acos(top/bottom))))