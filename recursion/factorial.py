def fact(number):
    if number < 2:
        return 1
    else:
        return number * fact(number-1)


print(fact(5))
print(fact(6))
print(fact(1))