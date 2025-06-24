import matplotlib.pyplot as plt


products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['skyblue', 'salmon', 'limegreen', 'orange', 'mediumpurple']

plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=colors)
plt.title('Sales Data for Products')
plt.xlabel('Products')
plt.ylabel('Sales Units')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
