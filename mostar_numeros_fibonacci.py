### MOSTRAR PRIMEROS 10 NUMEROS FIBONACCI ###

def fibonacci(n):
 fib_sequence = []
 a, b = 0, 1
 for _ in range(n):
  fib_sequence.append(a)
  a, b = b, a + b
 return fib_sequence
primeros_diez_fibonacci = fibonacci(10)
print(primeros_diez_fibonacci)
