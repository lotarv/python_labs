def is_prime(n):
    if n == 1:
        return True
    for i in range(2,n//2):
        if n % i == 0:
            return False
    return True

def max_prime_divisor(number):  #Метод 1 - Найти максимальный простой делитель числа
    max_divisor = 0
    for i in (2,number + 1):
        if (number % i == 0 and is_prime(i)):
            max_divisor = i
    return max_divisor


def mult_of_digits_not_divide_by_5(number): #Метод 2 - Найти произведение цифр числа, не делящихся на 5
    result = 1
    numberCpy = number
    while numberCpy > 0:
        digit = numberCpy % 10
        if (digit % 5 != 0):
            result *= digit
        numberCpy /= 10
    return result

def gdc_special(number): #Метод 3 - Найти НОД максимального нечетного непростого делителя числа и произведения цифр данного числа
    #Вычисляем максимальный нечетный непростой делитель
    max_odd_nonprime_divisor = 1
    for i in range(2,number):
        if i % 2 == 0:
            continue  # исключаем четные
        if (number % i != 0) :
            continue #исключаем не делители
        if (is_prime(i)) :
            continue #исключаем простые числа
        max_odd_nonprime_divisor = i
    
    
    #Вычисляем произведение чисел данного числа
    multiple_of_digits = 1

    while number > 0:
        multiple_of_digits *= number % 10
        number /= 10

    #Вычисляем НОД - наибольший общий делитель
    a = max_odd_nonprime_divisor
    b = multiple_of_digits

    while b != 0:
        a,b = b, a % b

    return a

print (gdc_special(150))
