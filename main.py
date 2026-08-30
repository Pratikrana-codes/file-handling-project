
from pathlib import Path

def create_file():
    name = input("Enter the file name: ")
    file = Path(name)

    if not file.exists():
        with open(file, "w") as f:
            data = input("What u want to enter in this file: ")
            f.write(data)
    else:
        print("File already exists")

    print("----FILE CREATED----")


def read_file():
    name = input("Enter the filename you want to read : ")
    file = Path(name)

    if file.exists():
        with open(file, "r") as f:
            content = f.read()
            print(content)
    else:
        print("The file u are searching doesn't exists")


def update_file():
    dic = {1: "Rename" , 2: 'Append' , 3:'Overwrite'}

    name = input("Enter the file name u want to update: \n")
    file = Path(name)

    if file.exists():
        print("Operations: ")
        for i in range(1,4):
                print(f"{i}. For {dic[i]} ")

        choice = int(input("Enter what u want to do with the file: "))

        if choice == 1:
                new_name = input("Enter the new file name: ")
                new_file = Path(new_name)

                if not new_file.exists():
                    file.rename(new_file)
                    print("----FILE RENAMED SUCCESSFULLY----")
                else:
                    print("File already exists try other name ")
        elif choice == 2:
            with open(file, "a") as f:
                data = input("Enter what u want to add: ")
                f.write(data)
            print("----ADDED----")
        elif choice == 3:
            with open(file, "w") as f:
                new_content = input("Enter the new content: ")
                f.write(new_content)
    else:
        print(" File doesn't exists ")

def delete_file():
    name = input("Enter the file name u want to delete: ")
    file = Path(name)

    if file.exists():
        file.unlink()
    else:
        print("File doesn't exists")

    print("----FILE DELETED----")


options = {1:"Creating", 2: "Reading" , 3: "Updating", 4:"Deleting", 5:"Exit"}


running = True

while running:

    for i in range(1,6):
        print(f"{i}. For {options[i]} the file.")
    

    try:
        choice = int(input("----WAITING FOR YOUR RESPONSE----\n"))

        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            update_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            running = False
        elif choice < 1 | choice > 5:
            print("Please enter a valid choice \n")
    except ValueError :
        print(f"Please enter a valid number")


    

