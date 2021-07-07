import matplotlib.pyplot as plt

years = [1970,1975,1980,1985,1990,1995,2000,2005,2010]
Ice_hockey_records = [56, 54, 58, 60, 66, 69, 68, 128, 129]
Skating_records = [36, 45, 46, 45, 48, 79, 89, 84, 94]

plt.plot(years, Ice_hockey_records,)
plt.plot(years, Skating_records)
plt.xlabel('years')
plt.ylabel('Ice_hockey_records')
plt.title('Ice hockey VS Skating')

Sports = 'Ice_hockey', 'Skating'

plt.legend(Sports,
			title="Sports",
			loc="bottomright")

plt.show()			
