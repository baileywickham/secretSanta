import random

names = ["andy", "jack", "christian", "ben", "ian", "bailey"]
numbers =  ["5033329523", "5037060383", "5034844734", "5038940386", "5037079976", "5039892243"]

for idx, number in enumerate(numbers):
	i = random.randrange(len(names))
	print('origonal ', i)
	while i == idx:
		i = random.randrange(len(names))
		print("they are equal, new i, idx ", i, idx)
	n = names[i]
	del names[i]

	print("{0} would buy for {1}".format(number, n))