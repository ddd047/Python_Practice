def PhoneBook():
    phonebook = {"AMIT": "9876543210", "RIYA": "9123456780"}

    while True:
        print("\n--------PHONEBOOK--------")
        print("--CHOOSE THE OPERATION--")
        print("1. ADD CONTACT")
        print("2. DELETE CONTACT")
        print("3. UPDATE CONTACT")
        print("4. VIEW ALL CONTACT")
        print("5. EXIT")

        choise = input("\nENTER YOUR CHOICE (1-5): ")

        if choise == "1":
            name = input("ENTER THE NAME: ").upper()
            if name in phonebook:
                print("CONTACT ALREADY EXISTS.")
            else:
                phone = input("ENTER THE PHONE NUMBER: ")
                phonebook[name] = phone
                print("CONTACT ADDED SUCCESSFULLY.")

        elif choise == "2":
            name = input("Enter The Name You Want to DELETE: ").upper()
            if name in phonebook:
                del phonebook[name]
                print("CONTACT DELETED SUCCESSFULLY.")
            else:
                print("CONTACT NOT FOUND.")

        elif choise == "3":
            name = input("Enter The Name You Want to UPDATE: ").upper()
            if name in phonebook:
                phone = input("ENTER THE NEW PHONE NUMBER: ")
                phonebook[name] = phone
                print("CONTACT UPDATED SUCCESSFULLY.")
            else:
                print("CONTACT NOT FOUND.")

        elif choise == "4":
            for name, phone in phonebook.items():
                print(f"{name} : {phone}")

        elif choise == "5":
            print("\nTHANK YOU FOR USING THE PHONEBOOK.")
            break

        else:
            print("\nINVALID CHOICE. PLEASE TRY AGAIN.")


if __name__ == "__main__":
    PhoneBook()
