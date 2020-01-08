# Find the least common multiplier of two numbers.

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

print(lcm(2, 14))
print(lcm(3, 14))
