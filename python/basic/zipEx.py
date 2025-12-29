name = ["M", "N", "S", "A"]
no = [4, 1, 3, 2]
numName = zip(name, no)
print(set(numName))

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

for x, y, z in zip(list1, list2, list3):
    print(f"sum: {x + y + z}")