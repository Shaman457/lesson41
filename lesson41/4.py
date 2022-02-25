a = int(input("Оценка: "))
if a > 10 and a<=12:
    print("Отлично!")
elif a>=9 and a<=10:
    print("Хорошо!")
elif a>=6 and a<=8:
    print("Ты можешь лучше!")
elif a<=5 and a>=0:
    print("Ужасно!")
else:
    print("У нас 12-ти бальная система! А не 100 бальная!")