def addContactFunction():
    contactName = input("Enter name : ")
    contactNumber = input("Enter number : ")
    contactMail = input("Enter mail : ")

    savedContact = False

    try:
        with open("contactList.csv", "r") as contactListFile:
            contactList = contactListFile.readlines()
            if contactList:
                for contact in contactList:
                    savedContactInfo = contact.split(",")
                    if contactNumber == savedContactInfo[1].strip():
                        savedContact = True
                        print("This number already exists.")
    except:
        open("contactList.csv", "w").close()

    if not savedContact:
        with open("contactList.csv", "a") as contactListFile:
            contactListFile.writelines(f"{contactName}, {contactNumber}, {contactMail}\n")
        print("Contact added successfully.")