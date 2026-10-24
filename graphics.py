#используем numpy - для вычислений, matplotlib - для рисования графиков
import numpy as np
import matplotlib.pyplot as plt

#много значений x для гладких линий (от 0.1, потому что ln(0) не существует)
x = np.linspace(0.1, 5, 200)

#целые значения x: 1, 2, 3, 4, 5 (для отметки точек)
xi = np.array([1, 2, 3, 4, 5])

#рисуем линии функций, у каждой свой цвет
plt.plot(x, x ** 2, color="blue", label="x^2")
plt.plot(x, np.exp(x), color="red", label="e^x")
plt.plot(x, np.log(x), color="green", label="ln(x)")
plt.plot(x, x ** 3, color="orange", label="x^3")

#отмечаем точки при целых x, у каждой функции свой значок
plt.plot(xi, xi ** 2, "o", color="blue")        # точки
plt.plot(xi, np.exp(xi), "x", color="red")      # кресты
plt.plot(xi, np.log(xi), "s", color="green")    # квадраты
plt.plot(xi, xi ** 3, "^", color="orange")      # треугольники

#ограничиваем ось y, иначе e^x делает остальные графики плоскими
plt.ylim(-2, 60)

#подписи, сетка и легенда
plt.title("Графики функций")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

#показываем график
plt.show()