def ugly(num):
    start = 1
    counter = 1
    while counter != num:
        start += 1
        temp = start
        while (temp % 2 == 0):
            temp = temp / 2
        while (temp % 3 == 0):
            temp = temp/3
        while (temp % 5 == 0):
            temp = temp/5
        if temp == 1:
            counter += 1
    print(start)


def ugly2(num):
    start = 1
    counter = 1
    array_1 = []
    array_2 = []
    array_3 = []
    pointer_1 = 0
    pointer_2 = 0
    pointer_3 = 0
    while counter != num:
        array_1.append(start*2)
        array_2.append(start*3)
        array_3.append(start*5)
        start = min(array_1[pointer_1], array_2[pointer_2], array_3[pointer_3])
        if start == array_1[pointer_1]:
            pointer_1 += 1
        if start == array_2[pointer_2]:
            pointer_2 += 1
        if start == array_3[pointer_3]:
            pointer_3 += 1
        counter += 1
    
    print(start)


if __name__ == "__main__":
    ugly(7)
    ugly(10)
    ugly(15)
    ugly(150)
    ugly2(7)
    ugly2(10)
    ugly2(15)
    ugly2(150)
