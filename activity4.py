import os

doc_path = os.path.expanduser('~/Documents')

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def student():
    student_no = input("Enter Student No.: ")
    lastName = input("Enter Last Name: ")  
    firstName = input("Enter First Name: ")
    middleInt = input("Enter Middle Initial: ")
    program = input("Enter Program: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    birthdate = input("Enter Birthdate (MM/DD/YYYY): ")
    contact_no = input("Enter Contact No.: ")

    data = [
        f"Student No.: {student_no}",
        f"Full Name: {lastName}, {firstName} {middleInt}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthdate}",
        f"Contact No.: {contact_no}"
    ]

    filename = os.path.join(doc_path, f"{student_no}.txt")
    with open(filename, 'w') as f:
        for info in data:
            f.write(info + "\n")

    print(f"Student information successfully saved to {filename}")

def search():
    while True:
        print("Select search method:")
        print("[1] Search by Student No.")
        print("[2] Search by Name")
        print("[3] Main Menu")
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            viewID()
        elif choice == '2':
            viewName()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

def viewID():
    student_id = input("Enter Student No. to view info: ")
    filename = os.path.join(doc_path, f"{student_id}.txt")
    try:
        with open(filename, 'r') as file:
            print("\n=== Student Information ===")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Student record not found. Please check the Student No. and try again. \n")

def viewName():
    name = input("Enter the name to search: ")
    found = False
    for file in os.listdir(doc_path):
        if file.endswith(".txt"):
            with open(os.path.join(doc_path, file), 'r') as f:
                content = f.read()
                if name in content:
                    print(f"Student {name} found in {file}:\n{content}\n")
                    found = True
                    break
    if not found:
        print(f"No records found with the name: {name}. \n")

def delInfo():
    while True:
        student_id = input("Enter Student No. to delete record: ")
        filename = os.path.join(doc_path, f"{student_id}.txt")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Student record {student_id} deleted.")
        else:
            print("Student record not found.")

while True:
    print("\n===Menu===")
    print("[1] Register Student")
    print("[2] Open Student Record")
    print("[3] Delete Student Record")
    print("[4] Exit")
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        student()
    elif choice == '2':
        search()
    elif choice == '3':
        delInfo()
    elif choice == '4':
        print("Thank you for using the program.")
        print("Exiting...")
        break
    elif choice == '5':
        updateInfo()
    else:
        print("Invalid choice. Please select a valid option.")
