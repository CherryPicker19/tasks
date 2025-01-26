import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x) * np.cos(x ** 2 + 5)

dif1 = np.diff(y)
dif2 = np.diff(dif1)

plt.figure()

max_value = np.max(y)
min_value = np.min(y)
max_index = np.argmax(y)
min_index = np.argmin(y)
plt.subplot(3, 1, 1)
plt.plot(x, y, label='Function')

plt.plot([x[max_index]], [max_value], 'o', color='b', label='MAX')
plt.plot([x[min_index]], [min_value], 'o', color='r', label='MIN')

x0 = x[max_index]
y0 = np.sin(x0) * np.cos(x0 ** 2 + 5)

tangent_eq = lambda x: y0 * (x - x0) + max_value
normal_eq = lambda x: -1/y0 * (x - x0) + max_value
plt.plot(x, y, label='f(x)')
plt.plot([x0], [max_value], 'o', color='b', label='Максимум')
plt.plot(x, tangent_eq(x), '--', color='orange', label='Касательная')
plt.plot(x, normal_eq(x), '--', color='green', label='Нормаль')
plt.grid()
plt.legend()


plt.subplot(3, 1, 2)
x = np.linspace(0, 10, 49)
plt.plot(x, dif1, label='dif1')
plt.grid()
plt.legend()

plt.subplot(3, 1, 3)
x = np.linspace(0, 10, 48)
plt.plot(x, dif2, label='dif2')
plt.grid()
plt.legend()

plt.figure(figsize=(8, 6))
x = np.linspace(0, 10, 50)
for xi in np.linspace(0, 5, 10):
    y0 = np.sin(x0) * np.cos(x0 ** 2 + 5)
    fxi = np.sin(xi) * np.cos(xi ** 2 + 5)
    plt.plot(x, fxi + y0 * (x - xi), '--', color='gray', alpha=0.5)
plt.plot(x, y, label='f(x)')
plt.title('Касательное расслоение')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

plt.show()
