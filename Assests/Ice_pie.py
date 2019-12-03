from matplotlib import pyplot as plt

Medals = "Gold", "Silver", "Bronze"
average_medal_ratio = [510, 514,512]
explode = (0,0.1,0)           # it "explode" the first part

fig1, ax1 = plt.subplots()
ax1.pie(average_medal_ratio, explode=explode, labels=Medals, autopct='%1.1f%%',
		shadow=True, startangle=90)
ax1.axis('equal')
ax1.set_title("Canada Won maximum no. of medals as compare to others in Ice hockey\n(Using %, Medal Category)")  #Equal sapect ratio ensure that pie is drawn as a circle
ax1.legend(
			title="Countries",
			loc="lower right",
			bbox_to_anchor=(1, 0, 0.1, 1))

plt.show()