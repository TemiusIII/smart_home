n = int(input())
counter = 0
list = []
while counter < n:
    list.append(int(input()))
    counter += 1

counter = {}

for elem in list:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)