import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), sharey=True)
fig.suptitle('Сходимость гистограммы к нормальному распределению', fontsize=18)

mu = 0
sigma = 1

x_values = np.linspace(-4, 4, 1000)

pdf_vals = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x_values - mu)**2) / (2 * sigma**2))


data1 = np.random.normal(mu, sigma, 100)
axes[0].hist(data1, bins=20, density=True, color='orange', alpha=0.7, label='n = 100')
axes[0].plot(x_values, pdf_vals, color='red', linewidth=2.5, label='Теоретическое N(0,1)')

axes[0].set_title('n = 100', fontsize=14)
axes[0].set_xlabel('Значение', fontsize=12)
axes[0].set_ylabel('Плотность вероятности', fontsize=12)
axes[0].set_xlim(-4, 4)
axes[0].set_ylim(0, 0.5)
axes[0].grid(True, alpha=0.3)
axes[0].legend(fontsize=12)

data2 = np.random.normal(mu, sigma, 1000)
axes[1].hist(data2, bins=30, density=True, color='black', alpha=0.7, label='n = 1000')
axes[1].plot(x_values, pdf_vals, color='red', linewidth=2.5, label='Теоретическое N(0,1)')

axes[1].set_title('n = 1000', fontsize=14)
axes[1].set_xlabel('Значение', fontsize=12)
axes[1].set_ylabel('Плотность вероятности', fontsize=12)
axes[1].set_xlim(-4, 4)
axes[1].set_ylim(0, 0.5)
axes[1].grid(True, alpha=0.3)
axes[1].legend(fontsize=12)

data3 = np.random.normal(mu, sigma, 10000)
axes[2].hist(data3, bins=50, density=True, color='plum', alpha=0.7, label='n = 10 000')
axes[2].plot(x_values, pdf_vals, color='red', linewidth=2.5, label='Теоретическое N(0,1)')

axes[2].set_title('n = 10 000', fontsize=14)
axes[2].set_xlabel('Значение', fontsize=12)
axes[2].set_ylabel('Плотность вероятности', fontsize=12)
axes[2].set_xlim(-4, 4)
axes[2].set_ylim(0, 0.5)
axes[2].grid(True, alpha=0.3)
axes[2].legend(fontsize=12)

plt.tight_layout() 
plt.subplots_adjust(top=0.85) 
plt.show()