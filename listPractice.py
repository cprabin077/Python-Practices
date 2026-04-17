list1 = ["Paras","Sagar", "Abhisekh", "Chandra", "Dinesh", "Roshan", "Lokesh", "Bibek", "Hikmat", "Sagar", "Abhisekh"]
print(list1)

# Count total number of values
print(len(list1))

# Count the values
list2 = list1.count("Sagar") 
print(list2)

# Check if the last value is string or not
print(isinstance(list1[-1], str))

# Append -> add the values at the end of list
list1.append("Kiran")
print(list1)

# Insert -> add value to the specified position
# list1.insert(2, 3.14)
# print(list1)

# Extend -> Add value of another list
# list3 = [True, "Emma", 39]
# list3.extend(list1)
# print(list3)
# list1.extend(list3)
# print(list1)

# Concat -> Add two lists in another new list 
a = [1, 3,6,8,"Ram"]
b = [3.14, 9.86, "Gravity"]
list4 = a + b
print(list4)

# Delete -> delete the value at specified index
# del list1[1]
# print(list1)

# Clear -> removes entire value
# list1.clear()
# print(list1)

# remove -> removes the specified value 
# list1.remove("Sagar")
# print(list1)

# pop -> remove the element at specified position
# list1.pop(1)
# print(list1)
# list1.pop()
# print(list1)

# Reverse -> reverse order
# list1.reverse()
# print(list1)

# Sort -> sort  in ascending order
list1.sort()
print(list1)

list1.reverse()
print(list1)