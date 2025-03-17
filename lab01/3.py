from timeit import default_timer as timer
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

