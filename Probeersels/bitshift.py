# getal1 = 1

# print(f"{getal1:b}")

# getal1 = getal1 << 2

# print(f"{getal1:b}")




# getal2 = 17

# print(f"{getal2:b}")

# getal2 = getal2 >> 2

# print(f"{getal2:b}")



def set_bit(value, bit):
    print(f"value = {value:b}")
    print(f"bit = {bit:b}")

    mask = 1<<bit

    print(f"mask = {mask:b}")

    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def is_set(value, bit):
    return value & (1 << bit) != 0


getal1 = 0

getal1 = set_bit(getal1, 2)
print(getal1)