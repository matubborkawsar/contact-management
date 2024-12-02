def updateContactFunction():
    savedContact = False

    try:
        with open("contactList.csv", "r") as contactListFile:
            contactList = contactListFile.readlines()
            if contactList:
                for index, contact in enumerate(contactList):
                    print(f"{index + 1}. {contact.strip()}")
                updateContact = int(input("Select a contact to update : "))
                if 0 < updateContact <= len(contactList):
                    singleContact = contactList[updateContact - 1].split(",")

                    print("1. Update contact name")
                    print("2. Update contact number")
                    print("3. Update contact email")

                    updateOption = int(input("Choose an option to update : "))

                    if updateOption == 1:
                        singleContact[0] = input("Enter new name: ")
                    elif updateOption == 2:
                        singleContact[1] = input("Enter new number: ")
                        for contact in contactList:
                            savedContactInfo = contact.split(",")
                            if singleContact[1] == savedContactInfo[1].strip():
                                savedContact = True
                                print("This number already exists.")
                    elif updateOption == 3:
                        singleContact[2] = input("Enter new email: ")
                        singleContact[2] = f"{singleContact[2]}\n"
                    else:
                        print("Invalid option.")

                    contactList[updateContact - 1] = f"{singleContact[0]}, {singleContact[1]}, {singleContact[2]}"

                    if not savedContact:
                        with open("contactList.csv", "w") as contactListFile:
                            contactListFile.writelines(contactList)
                        print("Contact updated successfully.")
                else:
                    print("Invalid option.")
            else:
                print("There are no contact.")
    except:
        open("contactList.csv", "w").close()
        print("There are no contact.")