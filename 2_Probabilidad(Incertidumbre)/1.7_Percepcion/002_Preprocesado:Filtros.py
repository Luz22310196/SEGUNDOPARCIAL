import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Señal ruidosa
t = np.linspace(0, 1, 500)
signal = np.sin(2*np.pi*5*t) + 0.5*np.random.randn(500)

# Diseño filtro pasa bajas
b, a = butter(4, 0.1, btype='low')
filtered_signal = filtfilt(b, a, signal)

# Graficar
plt.plot(t, signal, label="Señal original")
plt.plot(t, filtered_signal, label="Señal filtrada")
plt.title("Preprocesado: filtro pasa bajas")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.legend()
plt.show()