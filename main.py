import addContact, removeContact, updateContact, viewContacts, searchContact
print("Welcome to contact management.")

while True:
    print("\n1. Add contact")
    print("2. Remove contact")
    print("3. Update contact")
    print("4. Viw all contacts")
    print("5. Search contact")
    print("0. Exit")


    try:
        option = int(input("Select an option : "))

        if option == 1:
            addContact.addContactFunction()

        elif option == 2:
            removeContact.removeContactFunction()

        elif option == 3:
            updateContact.updateContactFunction()

        elif option == 4:
            viewContacts.viewContactFunction()

        elif option == 5:
            searchContact.searchContactFunction()

        elif option == 0:
            print("Thank you.")
            break

        else:
            print("Invalid option.")
    except:
        print("Invalid input. Please enter a number.")