#     project 2
contacts = {}

# ADD CONTACT

def add_contact():
    name = input('Enter your name : ')
    phone = int(input('Enter your phone no : '))
    contacts[name] = phone
    print("Contacts Add Sucessfully!")

# Search Contact 

def search_contact():
    if not contacts:
        print("No contacts available!")
        return
    name = input('Enter the name : ')
    if name in contacts:
        print(contacts[name])
    else:
        print('Contact not found!')

# Display Contact 

def display_contacts():
    if not contacts:
        print("No contacts available!")
        return
    
    print("\n-------Contact List-------\n")

    for name, phone in contacts.items():
        print(f'Name     : {name}')
        print(f'Phone no : {phone}')

# Delete Contact 

def delete_contact():
    if not contacts:
        print("No contacts available!")
        return
     
    name = input('Enter the name : ')

    if name in contacts:
        del contacts[name]
        print('Contact delete sucessfully!')
    else:
        print('Contact not found!')

# Menu 
# Main program
while True:
    print(f'1.Add Contact')
    print(f'2.Search Contact')
    print(f'3.Display Contact')
    print(f'4.Delete Contact')
    print(f'5.Exit')

    choice = int(input('Enter your Choice : '))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        display_contacts()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        print('Thanks for using Contact book!')
        break
    else:
        print('Invalid choice!')