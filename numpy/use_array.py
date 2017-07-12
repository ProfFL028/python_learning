#数据
world_alcohol = [
        [1986, "Western Pacific", "Viet Name", "Wine", 0],
        [1985, "Americas", "Uruguay", "Other", 0.5],
        [1984, "Africa", "Cte d'Ivorie", "Wine", 1.62],
]

first_row = world_alcohol[0]
print (first_row)

#获取第五行的数据
liters_drank = []
for row in world_alcohol:
        liters = row[4]
        liters_drank.append(liters)
liters_drank = liters_drank[1:len(liters_drank)]

total = 0
for item in liters_drank:
        total = total + float(item)
average = total / len(liters_drank)
print (average)


