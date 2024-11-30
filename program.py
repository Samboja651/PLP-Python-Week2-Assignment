# question 1
my_list = []

# question 2
items = (10, 20, 30, 40)
for item in items:
    my_list.append(item)

# question 3
my_list.insert(1, 15)

# question 4
my_list.extend([50, 60, 70])

# question 5
my_list.pop()

# question 6
my_list.sort()

# question 7
my_list.index(30)
# or
index_of_30 = 0
for item in my_list: 
    if item == 30:
        break
    index_of_30 += 1
print(index_of_30)