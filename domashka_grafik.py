import matplotlib.pyplot as plt
import numpy as np
u = np.array([0, 0.5, 1.07, 1.54, 2.16, 2.62, 3.25])
i = np.array([0, 0.06, 0.19, 0.33, 0.42, 0.57, 0.69])
plt.figure(figsize=(8, 5), dpi=100)
plt.plot(i, u, label='ВАХ', color='red', linewidth=2)
plt.xlabel('Сила тока')
plt.ylabel('Напряжение')
plt.title('ВАХ')
plt.show()
