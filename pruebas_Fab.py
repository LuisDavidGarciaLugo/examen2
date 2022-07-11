from Fab import F_Recursiva, F_Cola, F_Iter

#requiere la libreria matplotlib, ejecutar:
#   pip install matplotlib
import matplotlib.pyplot as plt
import time

funciones = [
   [F_Recursiva, []],
    [F_Cola, []],
    [F_Iter, []]
]

x = [i for i in range(1,201)]

for f in funciones:
    for i in x:
        ti = time.time()
        f[0](i)
        f[1].append((time.time() - ti)/1000)

    plt.plot(x, f[1], label = f[0].__name__)


plt.legend()
plt.show()