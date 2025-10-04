import os

doc_path = os.path.expanduser('~/Documents')

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def student():
    student_no = input("Enter Student No.: ")
    name = input("Enter Name (Last Name, First Name, Middle Initial): ")
    program = input("Enter Program: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    birthdate = input("Enter Birthdate (MM/DD/YYYY): ")
    contact_no = input("Enter Contact No.: ")
   
    filename = os.path.join(doc_path, f"{student_no}.txt")
    with open(filename, 'w') as file:
        file.write(f"Student No.: {student_no}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Program: {program}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}")
        file.write(f"Birthdate: {birthdate}\n")
        file.write(f"Contact No.: {contact_no}\n")

    print(f"Student information saved to {filename}")

# LOOP FOR MENU
while True:
    print("\n===Menu===")
    print("[1] Register Student")
    print("[2] Open Student Record")
    print("[3] Exit")
    choice = input("Choose an option (1-3): ")
    if choice == '1':
        student()
    elif choice == '2':
        student_id = input("Enter Student No. to view info: ")
        viewinfo(student_id)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
