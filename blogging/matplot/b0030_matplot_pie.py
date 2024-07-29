import matplotlib.pyplot as plt

labels = ['Aisa', 'Africa', 'Europe', 'Central and South America','North America','Oceania']
sizes = [59.5, 17.2, 9.6, 8.4, 4.7, 0.5]
colors = ['yellow', 'gray', 'lightskyblue', 'blue', 'red', 'green']
explode = (0.1, 0, 0, 0, 0 ,0)  # 두 번째 조각을 강조

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, explode=explode)

plt.title('Population Pie Chart')

plt.show()
