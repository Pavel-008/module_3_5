



def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) < 2:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


num = input('Введите число: ')
print(get_multiplied_digits(num))




