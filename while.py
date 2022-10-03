n = 0

while n < 5:
    print(n)
    n = n + 1

n = 5

while n != 0:
    print(n)
    n = n - 1

user_input = -1

while user_input != 0:
    user_input = (int(input("Enter a number")))
    if user_input == 0:
        print("exiting")
        break
    if user_input == 40:
       print("You entered 40")
       break
    
