import numpy as np
import matplotlib.pyplot as plt


data       = np.loadtxt("Berlin_population.txt")
year       = data[:, 0]
population = data[:, 1]


plt.figure(figsize=(5.9, 3.8))
ax = plt.gca()
plt.subplots_adjust(top=0.98, bottom=0.19, left=0.30, right=0.98)
plt.rcParams.update({"font.size": 18})
plt.plot(year, population, color="black", linewidth="2.0")
ax.ticklabel_format(axis="y", style="plain")
plt.xlabel("year", labelpad=5.0)
plt.ylabel("population of Berlin", labelpad=5.0)
plt.xlim(1834, 1906)
plt.yticks([0, 500000, 1000000, 1500000, 2000000], ["0", "500.000", "1.000.000", "1.500.000", "2.000.000"])
plt.ylim(0, 2350000)
plt.grid(color="lightgray")
plt.show()
