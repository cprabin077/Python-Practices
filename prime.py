num = int(input("Enter the number: "))
flag = False

if num < 2:
    print(num, " is neither prime nor composite")
else:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if flag:
        print(num, "is composite")
    else:
        print(num, "is prime")