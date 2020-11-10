

class Person:    
    def __init__(self, name):
        self.name = name
        
    def say_name(self):
        return self.name

def create(name):
    person = Person(name)
    return person.say_name()
    
    