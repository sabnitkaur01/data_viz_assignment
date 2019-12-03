from matplotlib import pyplot as plt

Country = "USA", "RUS", "GBR", "FRG", "CAN"
average_medal_ratio = [269, 46, 24, 18,351]
explode = (0,0.1,0,0.1,0) # it "explode" the first part

fig1, ax1 = plt.subplots()
ax1.pie(average_medal_ratio, explode=explode, labels=Country, autopct='%1.1f%%',
		shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Canada Won Maximum No. of Medals\n(Using %, Medal Category)")  #Equal sapect ratio ensure that pie is drawn as a circle
ax1.legend(
			title="Countries",
			loc="upper right",
			bbox_to_anchor=(1, 0, 0.1, 1))

plt.show()