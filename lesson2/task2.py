price = int(input("введите сумму покупки \n"))
result = 0
while price != 0:
    result += price
    price = int(input("введите сумму следующей покупки \n"))
print (result)    
