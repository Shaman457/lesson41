import time
import random
def cond(a):
    if a>=20:
        print("on")
    else:
        print("off")
    print(f"{a} \n//////////////")
while True:
    time.sleep(10)
    a = random.randint(0,40)
    cond(a)