

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def is_set(value, bit):
    return value & 1 << bit != 0


getal1 = 12
getal2 = 15

print(f"bits from {getal1}")
for i in range(8):
    print(is_set(getal1, i))

print()
print(f"bits from {getal2}")
for i in range(8):
    print(is_set(getal2, i))

getal1 = set_bit(getal1, 0)
print()
print(f"bits from {getal1}")
for i in range(8):
    print(is_set(getal1, i))

getal1 = clear_bit(getal1, 0)
print()
print(f"bits from {getal1}")
for i in range(8):
    print(is_set(getal1, i))