import time
from threading import Thread
from multiprocessing import Pool

contador = 500000


def contage_regressiva(n):
    while n > 0:
        n -= 1


# mesmo utilizando multi threading devido ao GIL ele é executado em single - threading
t1 = Thread(target=contage_regressiva, args=(contador//2,))
t2 = Thread(target=contage_regressiva, args=(contador//2,))
inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()
print(f"Thread executadas em: {fim - inicio}")


def contage_regressiva_2(n):
    while n > 0:
        n -= 1


pool = Pool(processes=2)
inicio = time.time()
r1 = pool.apply_async(contage_regressiva_2, [contador//2])
r2 = pool.apply_async(contage_regressiva_2, [contador//2])
pool.close()
pool.join()
fim = time.time()
print(f"Process executadas em: {fim - inicio}")
