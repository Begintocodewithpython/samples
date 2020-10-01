import contact
import addressBook
import re
from sys import exit
import random


__author__ = 'Muhammad Arslan <rslnkrmt2552@gmail.com>'

app = addressBook.addressBook(str(raw_input("Enter name of book  (Will be created if doesn't exist) \n> ")))
main_menu = '\n1. Show all contacts.\n2. Add contact.\n3. Search.\n4. Delete a contact.\n5.Update contact.\n6. Exit\n\n>'

def exitProg():
    exitMessages = ['You have my permission to die.']
    print random.choice(exitMessages)
    exit(0)

def getOption(prompt):
    inp = raw_input(prompt)
    try:
        inp = int(inp)
    except ValueError:
        print 'You should have selected a proper option.'
        return 13
    return inp


def showContacts():
    print 'show all'

def addContact():
    flag = 13
    while flag == 13:
        exp = map(lambda x: re.compile(x), [r'^([a-zA-Z]+)$', r'^(\+)?(\d)+$', r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"])

        fName = str(raw_input('Enter first name : ')).strip()
        while not exp[0].match(fName):
            fName = str(raw_input('\nWrong Input\nEnter (proper) first name : ')).strip()

        lName = str(raw_input('Enter last name : ')).strip()
        while not exp[0].match(lName):
            lName = str(raw_input('\nWrong Input\nEnter (proper) last name : ')).strip()

        pNum = str(raw_input('Enter phone number : ')).strip()
        while not exp[1].match(pNum):
            pNum = str(raw_input('\nWrong Input\nEnter (proper) number : ')).strip()

        email = str(raw_input('Enter email(Blank for none) : ')).strip()
        while not exp[2].match(email):
            if not email:
                break
            email = str(raw_input('\nWrong Input\nEnter (proper) email : ')).strip()

        print app.addEntry(contact.Contact(fName, lName, pNum, email))

        while (flag < 1) or (flag > 3):
            flag = getOption('\n1. Add another.\n2. Go to main menu\n3. Exit.\n\n> ')
        if flag == 2:
            break
        elif flag == 3:
            exitProg()
        else:
            flag = 13

def searchContact():
    print 'search'

def removeContact():
    name = str(raw_input('Enter first name of the contact: '))
    print app.removeEntry(name)

def updateContact():
    name = str(raw_input('Enter the first name of the contact: '))
    msg, cont = app.searchEntry(name)
    print msg



funcs = [showContacts, addContact, searchContact, removeContact, updateContact, exitProg]

while True:
    inp = getOption(main_menu)
    while inp < 1 or inp > 6:
        print 'Input a proper number, moron.'
        inp = getOption(main_menu)
    funcs[inp - 1]()
