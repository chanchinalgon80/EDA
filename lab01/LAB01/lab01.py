import matplotlib.pyplot as plt
from timeit import default_timer as timer

# Algoritmo 1
def function1(n):
    i = s = 1
    while s < n:
        i = i + 1
        s = s + i

# Algoritmo 2
def function2(n):
    count = 0
    for i in range(n // 2, n):
        j = 1
        while j + n // 2 <= n:
            k = 1
            while k < n:
                count += 1
                k = k * 2
            j = j + 1

# Algoritmo 3
def function3(n):
    count = 0
    for i in range(int(n / 2), n):
        j = 1
        while j + n / 2 <= n:
            if j > n:
                break
            j = j + 2
    print(count)

# Valores de n para cada algoritmo
n_values1 = [1, 10, 100, 1000, 10000]
n_values2 = [1, 10, 100, 1000]
n_values3 = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

# Función para medir tiempos y graficar
def measure_and_plot(func, n_values, title):
    times = []
    for n in n_values:
        start = timer()
        func(n)
        end = timer()
        times.append(end - start)
        print(f"{title} - n: {n}, Time: {end - start:.6f} seconds")

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', linestyle='-', label=title)
    plt.xlabel("n")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.title(title)
    plt.show()

# Ejecutar y graficar cada algoritmo
measure_and_plot(function1, n_values1, "Algoritmo 1")
measure_and_plot(function2, n_values2, "Algoritmo 2")
measure_and_plot(function3, n_values3, "Algoritmo 3")
