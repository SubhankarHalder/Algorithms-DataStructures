def rev(name):
    if len(name) == 1:
        return name
    else:
        return rev(name[1:]) + name[0]
    

print(rev("algorithm"))
print(rev("kayak"))