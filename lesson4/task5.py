words = input().split() # вводим два слова и разделяем их по пробелам
word1 = words[0] # первое слово
word2 = words[1] # второе слово

result1 = word1 in word2 # проверяем вхождение первого слова во второе
result2 = word1 == word2 # проверяем равенство слов
result3 = word1 > word2 # проверяем, больше ли первое слово второго
result4 = word1 < word2 # проверяем, меньше ли первое слово второго

print(result1, result2, result3, result4) # выводим результаты
