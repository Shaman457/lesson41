import math
x = int(input("X: "))
y = int(input("Y: "))
def sqrt(a,b):
    z = math.sqrt(a * b)
    print(z)
def log(a,b):
    z = math.log(a + b)
    print(z)



if x > y:
    sqrt(x,y)
else:
    log(x,y)