def viewContactFunction():
    try:
        with open("contactList.csv", "r") as contactListFile:
            contactList = contactListFile.readlines()
            if contactList:
                for index, contact in enumerate(contactList):
                    print(f"{index + 1}. {contact.strip()}")
            else:
                print("There are no contact.")
    except:
        open("contactList.csv", "w").close()
        print("There are no contact.")