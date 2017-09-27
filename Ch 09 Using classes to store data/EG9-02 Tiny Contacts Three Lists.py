# EG9-02 Tiny Contacts Three Lists

from BTCInput import *

# Create the lists to store contact information
names=[]
addresses=[]
telephones=[]

def new_contact():
    '''
    Reads in a new contact and stores it
    '''
    print('Create new contact')
    names.append(read_text('Enter the contact name: '))
    addresses.append(read_text('Enter the contact address: '))
    telephones.append(read_text('Enter the contact phone: '))

def find_contact():
    '''
    Reads in a name to search for and then displays
    the content information for that name or a
    message indicating that the name was not found
    '''
    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    # remove any whitespace from around the search name
    search_name = search_name.strip()
    # convert the search name to lower case
    search_name = search_name.lower()
    # Counter for the name position
    name_position=0
    for name in names:
        # remove any ny whitespace from around the name
        name=name.strip()
        # convert the name to lower case
        name = name.lower()
        # see if the names match
        if name==search_name:
            # if the names match, end the loop
            break
        # move the position down to the next name
        name_position=name_position+1

    if name_position < len(names):
        # Found a name
        print('Name: ',names[name_position])
        print('Address: ',addresses[name_position])
        print('Telephone: ',telephones[name_position])
    else:              
        print('This name was not found.')

menu='''Tiny Contacts

1. New Contact
2. Find Contact
3. Exit program

Enter your command: '''
while True:
    command=read_int_ranged(prompt=menu,min_value=1,max_value=3)
    if command==1:
        new_contact()
    elif command==2:
        find_contact()
    elif command==3:
        break
