# EG12-06 Adding a function as a class attribute

def hello_spanish(self):
    print('Hola')

class Person(object):
    pass

jose = Person()
jose.hello = hello_spanish
jose.hello()
