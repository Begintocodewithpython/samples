# EG12-05 Test contact generator

class Contact:
    
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self._hours_worked=0

    @staticmethod
    def create_test_contacts():
        phone_number = 1000000
        hours_worked = 1
        for first_name in ('Rob', 'Mary', 'Jenny', 'David', 'Chris', 'Imogen'):
            for second_name in ('Miles', 'Brown'):
                full_name = first_name + ' ' + second_name
                address = full_name + "'s house"
                telephone = str(phone_number)
                phone_number = phone_number + 1
                contact = Contact(full_name, address, telephone)
                contact._hours_worked = hours_worked
                hours_worked = hours_worked + 1
                yield contact

for contact in Contact.create_test_contacts():
    print(contact.name)
    print(contact.address)
    print(contact.telephone)
