# List-Based Tasks

# Print all elements of a list using a while loop
a = [1.2,1,3,4,True, False, "hello", "bye", 3.14]
i = 0
print("The elements of a list are:")
while(i<len(a)):
    print(a[i])
    i = i+1

print("____"*15)

# Find the sum of all elements in a list
a = [1,2,3,4,5,6,7,8,9,10]
i = 0
sum = 0
print("The sum of all elements in a list: ")
while(i<len(a)):
    sum = sum + a[i]
    i = i+1

print(sum)

print("____"*15)

# Find the largest number in a list
a = [1,2,3,4,5,6,7,8,9,10]
i = 0
max = a[0]
while(i<len(a)):
    if(max < a[i]):
        max = a[i]
    i = i+1
print("The largest number in a list: ", max)

print("____"*15)

# Count how many times a specific number appears in a list
a = [1,2,1,4,4,6,7,8,9,9,10]
num = 10
# num = int(input("Enter the number: "))
i = 0
count_num = 0
while(i<len(a)):
    if num == a[i]:
        count_num = count_num + 1
    i = i+1
print(f"Number: {num} repeated {count_num} times")