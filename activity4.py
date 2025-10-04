import os

doc_path = os.path.expanduser('~/Documents')

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def search():
    print("Select search method:")
    print("[1] Search by Student No.")
    print("[2] Search by Name")
    choice = input("Choose an option (1-2): ")
    if choice == '1':
        viewinfo()
    elif choice == '2':
        searchname()
    else:
        print("Invalid choice. Please select 1 or 2.")

def student():
    student_no = input("Enter Student No.: ")
    firstName = input("Enter First Name: ")
    middleInt = input("Enter Middle Initial: ")
    lastName = input("Enter Last Name: ")  
    program = input("Enter Program: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    birthdate = input("Enter Birthdate (MM/DD/YYYY): ")
    contact_no = input("Enter Contact No.: ")
   
    filename = os.path.join(doc_path, f"{student_no}.txt")
    with open(filename, 'w') as file:
        file.write("data = [ \n}")
        file.write(f"Student No.: {student_no}\n")
        file.write(f"Full Name: {firstName} {middleInt} {lastName}\n")
        file.write(f"Program: {program}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Birthdate: {birthdate}\n")
        file.write(f"Contact No.: {contact_no}\n")

    print(f"Student information saved to {filename}")

def viewinfo():
    student_id = input("Enter Student No. to view info: ")
    filename = os.path.join(doc_path, f"{student_id}.txt")
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\n=== Student Information ===")
                print(content)
        except FileNotFoundError:
            print("❌ Student record not found.")

def delinfo():
    student_id = input("Enter Student No. to delete record: ")
    filename = os.path.join(doc_path, f"{student_id}.txt")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Student record {student_id} deleted.")
    else:
        print("❌ Student record not found.")

def searchname():
    name = input("Enter the name to search: ")
    found = False
    for file in os.listdir(doc_path):
        if file.endswith(".txt"):
            with open(os.path.join(doc_path, file), 'r') as f:
                content = f.read()
                if name in content:
                    print(f"Found in {file}:\n{content}\n")
                    found = True
    if not found:
        print("❌ No records found with that name.")

# LOOP FOR MENU
while True:
    print("\n===Menu===")
    print("[1] Register Student")
    print("[2] Open Student Record")
    print("[3] Delete Student Record")
    print("[4] Exit")
    choice = input("Choose an option (1-3): ")
    if choice == '1':
        student()
    elif choice == '2':
        search()
    elif choice == '3':
        delinfo()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
