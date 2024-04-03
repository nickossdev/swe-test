def add_numbers(a, b):
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)
    return a + b

def multiply_numbers(a, b):
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)
    return a * b

a = 5
b = 10
c = "15"
d = 3

print(f"Adding {a} and {b}: {add_numbers(a, b)}")
print(f"Adding {a} and {c}: {add_numbers(a, c)}")
print(f"Multiplying {a} and {b}: {multiply_numbers(a, b)}")
print(f"Multiplying {c} and {d}: {multiply_numbers(c, d)}")
