def add(x: float, y: float) -> float:
    return x + y

def multiply(x:float, y:float) -> float:
    return x * y

def square(x:float) -> float:
    return multiply(x, x)

def add_squares(x:float, y:float) -> float:
    return add(square(x), square(y))

print(add(1, 2)) # Expected output: 3
print(multiply(2, 3)) # Expected output: 6
print(square(4)) # Expected output: 16
print(add_squares(2, 3)) # Expected output: 13
