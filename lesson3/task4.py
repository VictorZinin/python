# Нашему заказчику нужно, чтобы фраза «Я — программист!» выводилась на экран столько раз, сколько он сам этого захочет.
# Напишите программу, которая запрашивает число — количество строчек с фразой «Я — программист!» — и столько же раз выводит на экран эту фразу. 
# Для решения задачи используйте переменную-счётчик, которая увеличивается на единицу до тех пор, пока не будет введено нужное количество строчек.

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
number = int(input("Введите количество строк: "))
i = 0
while i < number:
    print("Я — программист!")
    i += 1