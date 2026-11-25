
import numpy as np
import matplotlib.pyplot as plt

# Створення масиву значень x
x = np.linspace(0.3, 12.3, 100)

# Обчислення значень функції
y = np.log(x) + 0.7 * x**2

# Побудова графіка
plt.plot(x, y, 'c--', label='y = ln(x) + 0.7x^2')

# Оформлення графіка
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції')
plt.grid(True)
plt.legend()

# Збереження графіка
plt.savefig('myplot.jpg', dpi=400)

# Відображення графіка
plt.show()
