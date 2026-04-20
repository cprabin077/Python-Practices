# 🔹 Basic Tasks

# Print numbers from 1 to 10 using a while loop
num = 1
while(num<=10):
    print(num)
    num = num + 1 

print("____"*10)  

# Print even numbers from 1 to 20
num = 1
print("The even numbers are: ")
while(num <=20):
    if(num%2 == 0):
        print(f"{num}")
    num = num + 1
        
print("____"*10) 

# Print odd numbers from 1 to 15
num = 1
print("The odd numbers are: ")
while(num <=15):
    if(num%2 != 0):
        print(f"{num}")
    num = num + 1

print("____"*10)  

# Print numbers in reverse (10 to 1)
num = 10
print("The reverse numbers are: ")
while(num>0):
    print(num)
    num = num-1



