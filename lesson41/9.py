x = int(input())
y = int(input())
if x>0 and y>0:
    print("Первая")
elif x<0 and y>0:
    print("Вторая")
elif x<0 and y<0:
    print("Третья")
elif x>0 and y<0:
    print("Четвертая")
else:
    print("Точка в центре")
print(x,y)