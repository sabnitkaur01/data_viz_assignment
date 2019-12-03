import matplotlib.pyplot as plt

years = [1975,1980,1985,1990,1995,2000,2005,2010,2015,2020]
MEN = [18, 19, 20, 22, 23, 22, 22, 24, 23, 25]
WOMEN = [0, 0, 0, 0, 0, 20, 20, 19, 21, 21]

plt.plot(years, MEN)
plt.plot(years, WOMEN)
plt.xlabel('Years')
plt.ylabel('Gender')
plt.title('MEN VS WOMEN')

Gender = 'MEN', 'WOMEN'
plt.legend(Gender,
		   title="Gender",
		   loc="upper left")

plt.show()