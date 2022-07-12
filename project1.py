from database import Simpledb
import sys


print("T E L E P H O N E  D I R E C T O R Y")
print()

while True:
    user_command = input("Do you want to Add(a), Find(f), Delete(d), Update(u), or Quit(q)? ").lower()
    if user_command not in 'afduq':
        print("Please enter a valid command")
        continue
    if user_command == "a":
        name = input("Enter name: ")
        if ' ' in name:
            name = name.split(' ', 1)[0]
        phone_number = input("Enter their number (without hyphens): ")
        Simpledb.insert('telephone.txt', name, phone_number)
        print("Their name has been added!")
        print()
        continue
    elif user_command == "f":
        name = input("Enter the name you would like to find: ")
        if Simpledb.select_one('telephone.txt', name) is None:
            print(name + " is not in this database")
            continue
        print("Their number is: " + Simpledb.select_one('telephone.txt', name))
        print()
        continue
    elif user_command == "d":
        name = input("Enter the name you would like to delete: ")
        Simpledb.delete('telephone.txt', name)
        print(name + " has been deleted from the database")
        print()
        continue
    elif user_command == "u":
        name = input("Enter the name you would like to update: ")
        if not Simpledb.update('telephone.txt', name):
            phone_number = input("Enter their new number (without hyphens): ")
            Simpledb.update('telephone.txt', name, phone_number)
            print("Their number has been updated")
            print()
            continue
        print()
    else:
        sys.exit()

