
n = int(input("Introduce el número de términos: "))

a, b = 0, 1

print("Serie de Fibonacci:")
for _ in range(n):
    print(a)
    a, b = b, a + b
