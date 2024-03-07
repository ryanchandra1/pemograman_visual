print("\033c")

set_1 = {"Toyota", "Daihatsu", "Honda"}
set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data set_1 adalah ", type(set_1))
print("Tipe data set_2 adalah ", type(set_2))
print("data set_1: ", set_1)
print("data set_2: ", set_2)
print("--------------------------------------")

#print every item of set 1
for x in set_1:
    print(x)
print("--------------------------------------")

# check length of set
print(len(set_1))

# check if key exist
if "Daihatsu" in set_1:
    print("Yes, 'Daihatsu' is an item in set_1")
    

#add an item
set_1.add("Mitsubishi")
print(set_1)


#Add multiple items

set_1.update(["Suzuki", "Mazda", "Nissan"])
print(set_1)

print("================= PART 2 ===============")

# ========= Part 2 ==============

# Remove an item (method 1)
set_1.remove("Honda")
print(set_1)

# Remove an item (method 2)
set_1.discard("Mazda")
print(set_1)

# Delete (pop) the last inserted key
set_1.pop()
print(set_1)


# Create set_2
set_2 = {1, 2, 3}

# Union of set_1 and set_2
set_3 = set_1.union(set_2)
print(set_3)

# Clear the set_
set_1.clear()
print(set_1)

# Delete the set_
del set_1
print("--------------------------------------")



# Union of two set_s
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("--------------------------------------")


# set_ 1 takes copies of all items of set_ 2
set_1 = {"a", "b", "c"}
set_2 = {1, 2, 3}
set_1.update(set2)
print(set1)


