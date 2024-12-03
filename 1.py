# read data.txt into memory
file = open("data.txt")
text = file.read()

# parse into lists
lines = text.split("\n")
tuples = [line.split() for line in lines]
list1, list2 = zip(*tuples)

# sort both lists
list1 = list(list1)
list1.sort()
list2 = list(list2)
list2.sort()

# calculate the difference
distances = [abs(int(left) - int(right)) for (left, right) in zip(list1, list2)]

total_distance = sum(distances)

print(total_distance)
