# EG12-04 Methods in classes


class LanguageMethods(object):

    def hello_french(self):
        print('Bonjour')

    def hello_german(self):
        print('Hallo')

    def hello_english(self):
        print('Hello')

class Person(object):
    pass

langauges = LanguageMethods()

ellie = Person()
ellie.hello = langauges.hello_french
ellie.hello()

gustav = Person()
gustav.hello = langauges.hello_german
gustav.hello()

langauges.hello_french = langauges.hello_german
ellie.hello()
rob = Person()
rob.hello = langauges.hello_english
rob.hello()

