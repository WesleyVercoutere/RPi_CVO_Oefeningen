# These work for integers of any size, even greater than 32 bit:

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

# If you like things short, you can just use:

val = 0b111
val |= (1<<3)

'{:b}'.format(val)
'1111'
>>> val &=~ (1<<1)
'1101'