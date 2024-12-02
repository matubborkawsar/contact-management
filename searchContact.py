def searchContactFunction():
    try:
        contactSearch = input("Search : ")

        found = False

        with open("contactList.csv", "r") as contactListFile:
            contactList = contactListFile.readlines()
            searchResultList = []
            if contactList:
                for contact in contactList:
                    savedContactInfo = contact.strip().split(",")
                    for savedContactInfoItem in savedContactInfo:
                        if contactSearch.lower() == savedContactInfoItem.lower():
                            found = True
                            searchResultList.append(contact)

            for index, contact in enumerate(searchResultList):
                print(f"{index + 1}. {contact.strip()}")

        if not found:
            print("There are no contact for", contactSearch)
    except:
        open("contactList.csv", "w").close()
        print("There are no contact.")