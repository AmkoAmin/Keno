import numpy as np
import matplotlib.pyplot as plt

Vmax = 200
f1, f2 = 100, 25
t = np.linspace(0, 0.04, 2000)

f_t = Vmax * np.sin(2*np.pi*f1*t)
g_t = Vmax * np.sin(2*np.pi*f2*t)

fig, ax = plt.subplots(figsize=(9.5, 3.2))
ax.plot(t*1000, f_t, label=r"$f(t)=200\,\sin(2\pi\cdot100\,t)$")
ax.plot(t*1000, g_t, label=r"$g(t)=200\,\sin(2\pi\cdot25\,t)$")
ax.set_title("Voltage Waveforms")
ax.set_xlabel("Time (ms)")
ax.set_ylabel("Voltage (V)")
ax.grid(True)
ax.legend()

fig.savefig("kenoplot.png", dpi=300, bbox_inches="tight")  # <-- vor show()
plt.show()
plt.close(fig)
