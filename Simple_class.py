class Person:
    def say(self, massage):
        print(massage)

    def say_hello(self):
        self.say("Hello")

tom = Person()
mot = Person()

tom.say_hello()
tom.say("allo")