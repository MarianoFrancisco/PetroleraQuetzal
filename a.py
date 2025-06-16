import matplotlib.pyplot as plt
import numpy as np

# 1. Control law comparison
fill = np.linspace(0, 100, 501)
orig_rate = np.where(fill < 80, 100, 33)
new_rate = np.piecewise(fill,
                        [fill < 76, (fill >= 76) & (fill < 83), (fill >= 83) & (fill < 90), fill >= 90],
                        [100, 75, 50, 25])

plt.figure()
plt.plot(fill, orig_rate, label="Actual (escalón único)")
plt.plot(fill, new_rate, label="Propuesta (tres umbrales)", linestyle="--")
plt.xlabel("Nivel del tanque [%]")
plt.ylabel("Tasa de cada pozo [% de nominal]")
plt.title("Ley de control de extracción")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Cola de camiones antes vs después
labels = ["Antes", "Después"]
queue_times = [26, 11]

plt.figure()
plt.bar(labels, queue_times)
plt.ylabel("Tiempo medio en cola (min)")
plt.title("Efecto de añadir brazos de carga/descarga")
plt.tight_layout()
plt.show()

# 3. Oscilación de inventario en el tanque esférico
t = np.linspace(0, 24, 1000)  # hours
before = 50 + 30 * (0.5 * (1 + np.sin(2 * np.pi * t / 6)))
after = 60 + 20 * (0.5 * (1 + np.sin(2 * np.pi * t / 6)))   

plt.figure(figsize=(8, 3))
plt.plot(t, before, label="Antes (50‑80 %)")
plt.plot(t, after,  label="Después (60‑80 %)", linestyle="--")
plt.fill_between(t, before, after, where=after<=before, color='grey', alpha=0.2)
plt.xlabel("Tiempo (h)")
plt.ylabel("Nivel del tanque [%]")
plt.title("Oscilación de inventario en el tanque esférico")
plt.ylim(45, 85)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()