def is_point_in_ring(x, y, R1, R2):
    distance_squared = x**2 + y**2
    return R1**2 <= distance_squared <= R2**2

x, y = map(float, input("Введіть координати точки (x, y): ").split())
R1 = float(input("Введіть внутрішній радіус R1: "))
R2 = float(input("Введіть зовнішній радіус R2: "))

if is_point_in_ring(x, y, R1, R2):
    print(f"Точка ({x}, {y}) належить кільцю.")
else:
    print(f"Точка ({x}, {y}) не належить кільцю.")
