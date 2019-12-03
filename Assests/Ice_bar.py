import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Sports = ('Biathlon', 'Bobsleign','curling', 'Ice hockey', 'luge','skating')
y_pos = np.arange(len(Sports))
Number_of_Medals = [140, 144, 58, 510, 62, 412]

plt.bar(y_pos, Number_of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, Sports)
plt.ylabel('Number_of_Medals')
plt.xlabel('Sports')
plt.title('Number of Gold Medals Won')

plt.legend(
	title="Sports",
	loc="upper right",
	bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()
