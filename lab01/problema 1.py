import matplotlib.pyplot as plt
from timeit import default_timer as timer

def logarithms(n):
    i = 1
    while i <= n:
        i = i * 2  # Multiplica i por 2 en cada iteración

# Lista de valores de n
n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
times = []

for n in n_values:
    start = timer()
    logarithms(n)
    end = timer()
    proc_time = end - start
    times.append(proc_time)

    print(f"n = {n}, Processing Time = {proc_time:.8f} segundos")

# Graficar los resultados
plt.figure(figsize=(8, 5))
plt.plot(n_values, times, marker="o", linestyle="-", color="b", label="Tiempo de procesamiento")
plt.xscale("log")  # Escala logarítmica en el eje X
plt.yscale("log")  # Escala logarítmica en el eje Y (opcional)
plt.xlabel("n (tamaño de entrada)")
plt.ylabel("Tiempo de procesamiento (segundos)")
plt.title("Tiempo de procesamiento vs. Tamaño de entrada")
plt.legend()
plt.grid(True)
plt.show()
