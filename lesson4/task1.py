def square_digits(num):
    num_list = list(str(num)) 
    for item in range(len(num_list)):
        num_list[item] = str(int(num_list[item]) ** 2)
 
    return "".join(num_list)

num = int(input())

print(square_digits(num))