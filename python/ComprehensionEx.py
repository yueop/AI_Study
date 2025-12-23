newlist = [x for x in range(1,11) if x % 2 == 0]
print(newlist)

country = ["Seoul", "New York", "London", "Shanghai", "paris", "Tokyo"]
newCountry = [x for x in country if x[0] == "S"]
print(newCountry)

newCountry1 = [x for x in country if "S" in x]
print(newCountry1)