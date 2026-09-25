amount_due=50

while amount_due>0:
    coin=int(input("Insert Coin: "))

    if coin==25:
        amount_due=amount_due-25
    elif coin==10:
        amount_due=amount_due-10
    elif coin==5:
        amount_due=amount_due-5

    if amount_due>0:
        print(f'Amount Due: {amount_due}')

if amount_due<0:
    print(f'Change Owed: {-amount_due}')

else:
    print('Change Owed: 0')
