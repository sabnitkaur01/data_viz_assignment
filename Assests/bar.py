import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Gender = ('Men', 'Women')
y_pos = np.arange(len(Gender))
Number_of_Medals = [1231, 305]

plt.bar(y_pos, Number_of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, Gender)
plt.ylabel('Number_of_Medals')
plt.xlabel('Gender')
plt.title('Number of Medals Won by Men and Women in ice hockey')

plt.legend(
	title="Gender",
	loc="upper right",
	bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()
