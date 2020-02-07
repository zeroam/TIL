class Phone:
    def __init__(self, number):     # magic method / intializer
        print('The Phone object was created')
        self.number = number

    def __lt__(self, other):        # magic method / rich comparison
        return self.number < other.number


my_phone = Phone(20)
other_phone = Phone(30)

if my_phone < other_phone:
    print('Two instances of custom class were compared')
    print('"__lt__" was called implicitly')

if my_phone.__lt__(other_phone):
    print('New, "__lt__" was used explicitly')
