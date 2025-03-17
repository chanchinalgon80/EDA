from timeit import default_timer as timer
import matplotlib.pyplot as plt

valores = [1, 10, 100, 1000, 10000, 100000]
tiempos = []

for n in valores:
    start = timer()
    for i in range(n):
        pass  
    end = timer()
    proc_time = end - start
    tiempos.append(proc_time)
    print(f"Processing time for n={n} -> {proc_time:.6f} seconds")

plt.figure(figsize=(8, 5))
plt.plot(valores, tiempos, marker='o', linestyle='-', color='b', label='Tiempo de procesamiento')
plt.title("Tiempo de procesamiento en función de n")
plt.xlabel("Número de iteraciones (n)")
plt.ylabel("Tiempo de procesamiento (segundos)")
plt.xscale("log")  # Escala logarítmica para n
plt.yscale("log")  # Escala logarítmica para el tiempo
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
