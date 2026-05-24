import random
from scipy.integrate import quad

def fn(x):
    return x**2

def is_under(x, y):
    """Перевіряє, чи знаходиться точка (x, y) під кривою функції."""
    return y <= fn(x)

def monte_carlo_simulation(a, b, num_experiments=100, num_points=15000):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        under_points = [point for point in points if is_under(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(under_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area

# Розміри прямокутника
a = 2
b = fn(a)

# Кількість експериментів
num_experiments = 100
num_points_low = 15
num_points_mid = 150
num_points_high = 1500
num_points_highest = 15000

# Аналітична площа
S = quad(fn, 0, a)[0]
# Виконання симуляції
average_area_low = monte_carlo_simulation(a, b, num_experiments, num_points_low)
average_area_mid = monte_carlo_simulation(a, b, num_experiments, num_points_mid)
average_area_high = monte_carlo_simulation(a, b, num_experiments, num_points_high)
average_area_highest = monte_carlo_simulation(a, b, num_experiments, num_points_highest)
print(f"Аналітична площа: {S:.4f}")
print(f"Середня площа при {num_points_low} точках: {average_area_low:.4f}")
print(f"Середня площа при {num_points_mid} точках: {average_area_mid:.4f}")
print(f"Середня площа при {num_points_high} точках: {average_area_high:.4f}")
print(f"Середня площа при {num_points_highest} точках: {average_area_highest:.4f}")