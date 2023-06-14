def square_digits(num):
    num_list = list(str(num)) 
    dig_list = list(map(lambda x: str(int(x)**2),num_list))
    return int("".join(dig_list))
num = int(input())

print(square_digits(num))