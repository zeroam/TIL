class Person():
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    def email(self):
        return f'{self.first}.{self.last}@email.com'


if __name__ == "__main__":
    person = Person('selva', 'prabhakaran')
    print(person.fullname)  #> selva prabhakaran
    print(person.first)  #> selva
    print(person.last)  #> prabhakaran

    # Setting fullname calls the setter method and updates person.first and person.last
    person.fullname = 'velu pillai'

    # Print the changed values of `first` and `last`
    print(person.fullname) #> velu pillai
    print(person.first)  #> pillai
    print(person.last)  #> pillai

    # fullname deleter 호출 self.first, self.last를 지움
    del person.fullname
    print(person.first) #> None
    print(person.last)  #> None
    
