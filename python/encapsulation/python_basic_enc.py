class Phone:
    username = 'Kate'               # public variable
    __how_many_times_turn_on = 0    # private variable

    def call(self):                 # public method
        print('Ring-ring!')

    def __turn_on(self):            # private method
        self.__how_many_times_turn_on += 1
        print('Time was turned on:', self.__how_many_times_turn_on)


my_phone = Phone()

my_phone.call()
print('The username is', my_phone.username)
