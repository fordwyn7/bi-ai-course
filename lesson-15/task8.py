import matplotlib.pyplot as plt
import numpy as np

tp = ['T1', 'T2', 'T3', 'T4']
category_a = [30, 25, 35, 20]
category_b = [20, 15, 25, 30]
category_c = [10, 20, 15, 25]
x = np.arange(len(tp))

plt.figure(figsize=(8, 6))
plt.bar(x, category_a, label='Category A', color='skyblue')
plt.bar(x, category_b, bottom=category_a, label='Category B', color='salmon')

bottom_c = np.array(category_a) + np.array(category_b)
plt.bar(x, category_c, bottom=bottom_c, label='Category C', color='limegreen')

plt.title('Stacked Bar Chart of Category Contributions Over Time')
plt.xlabel('Time Period')
plt.ylabel('Values')
plt.xticks(x, tp)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
