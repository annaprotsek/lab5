import math

def calculate_function(x):
    if x >= 0:
        return x + 2 * x**4 - math.sqrt(3)
    elif -7.7 < x < 0:
        return math.sin(2 * x) + math.log10(abs(x))
    elif x <= -7.7:
        return math.cos(3 * x) - 1 / x
    else:
        return None

x_values = [0, -3, -7.7, -8]  
for x in x_values:
    print(f"f({x}) = {calculate_function(x):.4f}")
