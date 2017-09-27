# EG12-07 Pickling people

import pickle

class LanguageMethods(object): 

    def hello_french(self): 
        print('Bonjour')

    def hello_german(self): 
        print('Hallo')

    def hello_english(self): 
        print('Hello')

class Person: 
    pass

langauges = LanguageMethods() 

ellie = Person() 
ellie.hello = langauges.hello_french 
ellie.hello() 

with open('people.pickle','wb') as out_file:
    pickle.dump(ellie,out_file)

with open('people.pickle','rb') as in_file:
    loaded_ellie = pickle.load(in_file)

loaded_ellie.hello()
