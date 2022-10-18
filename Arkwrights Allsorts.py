import csv

def search():
    global tsv_file
    tsv_file = open("example.tsv")
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    for row in read_tsv:
        print(row)
    tsv_file.close()
    menu()

def add():
    global name
    global location
    global department
    global quantity
    name = input("What is the name of the item? ")
    location = input("Where is the item located? ")
    department = input("What department is the item stored in? ")
    quantity = input("How many of this item are in stock? ")
    pri_in_VAT = int(input("What is the price of this item with VAT? "))
    pri_ex_VAT = pri_in_VAT - (pri_in_VAT * 20 / 100)
    print("Entering "+ "Name: " + name + " Location: " + location + " Department: " + department + " Quantity: " + quantity)
    with open('example.tsv', 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([name, location, department, quantity, pri_in_VAT, pri_ex_VAT ])
    menu()



def menu():
    print("1) Search")
    print("2) Add")
    global userChoice
    userChoice = int(input("What option would you like to do? "))

    if userChoice == 1:
        search()
    elif userChoice == 2:
        add()
    else:
        print("Please select a number between 1 and 2")
        


menu()
