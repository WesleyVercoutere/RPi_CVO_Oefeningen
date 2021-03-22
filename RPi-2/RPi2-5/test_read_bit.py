def is_set(x):

    for i in range(4):
        if (x & (1<<i)):
            print("true")
        else:
            print("false")


x = 0
print(x)
is_set(x)

print("***************************")

x = 2
print(x)
is_set(x)

print("***************************")

x = 3
print(x)
is_set(x)

print("***************************")

x = 7
print(x)
is_set(x)

print("***************************")

x = 8
print(x)
is_set(x)


# if (x & (1<<n)) 
  ## n-th bit is set (1)


# else 
  ## n-th bit is not set (0)