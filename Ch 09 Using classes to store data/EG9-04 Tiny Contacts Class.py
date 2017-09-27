# EG9-04 Tiny Contacts Class

from BTCInput import *

# Create the contact class

class Contact:
    pass

# Create the list to store contact information

contacts=[]

def new_contact():
    '''
    Reads in a new contact and stores it
    '''
    print('Create new contact')
    # create a new instance
    new_contact=Contact()
    # add the data attributes
    new_contact.name=read_text('Enter the contact name: ')
    new_contact.address=read_text('Enter the contact address: ')
    new_contact.telephone=read_text('Enter the contact phone: ')
    # add the new contact to the contact list
    contacts.append(new_contact)

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
    # Set the result to indicate nothing found
    result=None
    for contact in contacts:
        # get the name out of the contact
        name=contact.name
        # remove any whitespace from around the name
        name=name.strip()
        # convert the name to lower case
        name = name.lower()
        # see if the names match
        if name.startswith(search_name):
            # if the names match, set the contact
            result=contact
            # end the loop
            break

    if result!=None:
        # Found a name
        print('Name: ',result.name)
        print('Address: ',result.address)
        print('Telephone: ',result.telephone)
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
