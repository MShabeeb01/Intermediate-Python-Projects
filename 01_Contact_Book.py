#Contact book project
#Step-1: Initialize an empty contact book
contacts = {}

#Step-2: Display the menu
def show_menu():
    print("\n---Contact book menu---")
    print("1.Add contact")
    print("2.View contacts")
    print("3.Search contact")
    print("4.Edit contact")
    print("5.Delete contact")
    print("6.Exit")

#Step-3 Add a contact
def add_contact():
    name = input("Enter contact name:")
    phone = input("Enter contact number:")
    email = input("Enter contact email:")
    contacts[name] = {"phone": phone,"email" : email}    
    #This saves the input in the dictionary
    print(f"Contact {name} has been added to your contact book successfully.")

#Step-4: View all contacts
def view_contact():
    if contacts: #If there is any contact in the dictionary.
        print("\n---Contact list---")
        for name, details in contacts.items():
            print(f"Name : {name}")
            print(f"Phone : {details['phone']}")
            print(f"Email : {details['email']}")
    else :
        print("Your contact book is empty.")

#Step-5: Search a contact
def search_contact():
    name = input("Enter the name of the contact you want to search:")
    if name in contacts:
        print(f"\n---Contact details for {name}---")
        print(f"Name: {name}")
        print(f"Contact : {contacts[name]['phone']}")
        print(f"Email : {contacts[name]['email']}")
    else:
        print(f"{name} not found in your contact book.")                     

#Step-6: Edit a contact 
def edit_contacts():
    name = input("Enter the name of the contact that you want to edit:")
    if name in contacts:
        phone = input("Enter new phone number:")
        email = input("Enter new email:")
        contacts[name] = {"Phone": phone , "Email" : email} #To assign new values to the dictionaries.
    else:
        print(f"{name} not found in your contact book.")

#Step-7: Delete a contact
def delete_contact():
    name = input("Enter the name of contact you want to delete:")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted from your contact book.") 
    else :
        print(f"{name} not found in your contact book.")

 #Step-8: Main program loop

while True:
    show_menu()
    choice = input("Enter your choice (1-6):"
    )

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using the contact book.Goodbye!.")
        break
    else:
        print("Invalid choice.Please select a valid option.(1-6).")                                            
