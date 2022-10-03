data = 'some data to save'


def write():
    with open('data.txt', 'w') as file:
        file.write(data + '\n')
        file.close()
    menu()

def append():
    with open('data.txt', 'a') as file:
        file.write(data + '\n')
        file.close()
    menu()

def read():
    with open('data.txt', 'r') as file:
        print(data)
        menu()
    
    
def menu():
    print("1 - Read")
    print("2 - Write")
    print("3 - Append")
    print("4 - Exit")
    global userChoice
    userChoice= input("What option would you like to choose? ")

    if userChoice == "1":
        read()
    elif userChoice == "2":
        write()
    elif userChoice == "3":
        append()
    elif userChoice == "4":
        exit()
    else:
        print("Please enter a number between 1 and 4 ")
        menu()
        
menu()


