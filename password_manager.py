import csv
import random 

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*"

password_characters = alphabet_upper + alphabet_lower + numbers + symbols

passwords = []

def show_menu():
    print("PASSWORD MANAGER")
    print("")
    print("1. Add password")
    print("")
    print("2. View password")
    print("")
    print("3. Remove password")
    print("")
    print("4. Save to CSV")
    print("")
    print("5. Generate strong password")
    print("")
    print("6. Exit")
    print("")

def add_password():
    website = input("Enter website: ")
    password = input("Enter password: ")
    if website == "" or password == "":
        print("Website and password cannot be empty!")
    else:
        passwords.append({"website": website, "password": password})
        print("Password saved!")

def view_password():
    if not passwords:
        print("No passwords yet.")
    else:
        for password in passwords:
            print(password["website"].upper(), "|", password["password"])

def remove_password():
    view_password()
    website_to_remove = input("Enter website to remove: ")
    for password in passwords:
        if password["website"] == website_to_remove:
            passwords.remove(password)
            print("Password removed!")
            break
    else:
        print("Website not found!")

def save_to_csv():
    if not passwords:
        print("No passwords to save!")
    else:
        with open("password.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["website", "password"])
            for password in passwords:
                writer.writerow([password["website"], password["password"]])
        print("Saved to password.csv!")

def generate_password():
    length = int(input("Enter password length: "))
    password = ""
    for i in range(length):
        password += random.choice(password_characters)
    print("Your generated password is:", password)
    save = input("Save this password? (yes/no): ").lower()
    if save == "yes":
        website = input("Enter website: ")
        passwords.append({"website": website, "password": password})
        print("Password saved!")
        
while True:
    show_menu()
    choice = input("Select an option: ")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        remove_password()
    elif choice == "4":
        save_to_csv()
    elif choice == "5":
        generate_password()
    elif choice == "6":
        break
    else:
        print("Invalid option")