def removeContactFunction():
    try:
        with open("contactList.csv", "r") as contactListFile:
            contactList = contactListFile.readlines()
            if contactList:
                for index, contact in enumerate(contactList):
                    print(f"{index + 1}. {contact.strip()}")
                removeContact = int(input("Select a contact to remove : "))
                if 0 < removeContact <= len(contactList):
                    contactList.pop(removeContact - 1)
                    with open("contactList.csv", "w") as contactListFile:
                        contactListFile.writelines(contactList)
                    print("Contact removed successfully.")
                else:
                    print("Invalid option.")
            else:
                print("There are no contact.")
    except:
        open("contactList.csv", "w").close()
        print("There are no contact.")