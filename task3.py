# 🔹 User Input Tasks
# Take input from user until they enter 0, then print the sum

sum = 0
num = int(input("Enter the number: "))
while(num != 0):
    sum = sum + num
    num = int(input("Enter 0 to stop: "))
print(f"Sum={sum}")

print("___________"*10)

# Ask user to enter numbers and count how many are positive and negative
pos = 0
neg = 0
num = int(input("Enter the number: "))
while(num != 0):
    if num > 0:
        pos = pos + 1
    else:
        neg = neg + 1
    num = int(input("Enter 0 to stop: "))

print(f"Positive number: {pos}")
print(f"Negative number: {neg}")

print("___________"*10)

# Create a simple password checker (keep asking until correct password is entered)
correct_password = "password"
password = input("Enter the password: ")

while password != correct_password:
    print("Access denied, please try again")
    password = input("Enter the password: ")
print("Access Granted!")
