age = int(input("Ваш возраст: "))
payday = int(input("Ваш доход: "))
bank = str(input("Есть ли банквоский счет? (Да/нет) "))
credit = int(input("Сумма кредита: "))
k = (credit*20)/100
if age >= 18 and payday>=k and bank == "Да":
    print("Succes")
else:
    print("No")