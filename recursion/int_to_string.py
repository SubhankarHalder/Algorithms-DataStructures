def to_str(n, base):
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]
    else:
        return to_str(n//base, base) + convert[n % base]


print(to_str(1234, 10))
print(to_str(5, 10))