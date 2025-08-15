# Note Taking App

# Step-1: Define file name
file_name = "MyNotes.txt"

#Step-2: Display menu options

def show_menu():
    print("\n---Note Taking App Menu---") 
    print("1.Add a new note") 
    print("2.View all notes")
    print("3.Delete all notes")
    print("4.Exit")

#Step-3: Add a new note
def add_note():
    note = input("Enter your note :")
    with open("MyNotes.txt","a") as file:
        file.write(note + "\n")
        print("Note added successfully!.")

#Step-4: View all notes
def view_notes():
    try :
        with open("MyNotes.txt","r") as file:
            content = file.read()
            if content:
                print("\n---Your Notes---")
                print(content)
            else:
                print("\n---Your notes is empty---")
    except FileNotFoundError:
        print("No Notes found.")

#Step-5: Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/No)")                                        
    if confirm.lower() == "yes":
        with open("MyNotes.txt","w") as file:
            pass #(This is write an empty space and all the notes will be deleted as it uses w write and not a append)
        print("All notes have been deleted.")
    else:
        print("Deletion Cancelled")

#Step-6: Main Program loop

while True:
    show_menu()
    choice = input("Enter your choice (1-4) :")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes() 
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Exiting note taking app.Goodbye!")
        break
    else:
        print("Invalid choice.Please enter a valid number.")                       
