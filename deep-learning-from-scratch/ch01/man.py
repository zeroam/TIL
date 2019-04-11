class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

    def __call__(self):
        print("I'm called")

m = Man("David")
m.hello()
m.goodbye()
m()