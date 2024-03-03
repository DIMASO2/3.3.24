class Chel:
    def __init__(self, name):
        self.name = name
        self.weight = 70
    def set_weight(self, weight):
        self.weight = weight

class Stul:
    def __init__(self):
        self.max_weight = 100
        self.sitter = "no"
        self.broken = False
    def sit(self, person):
        if(person.weight > self.max_weight):
            self.broken = True
            self.sitter = "broken"
        else:
            self.sitter = person.name
    def stand(self):
        if(self.broken == False):
            self.sitter = "no"

gleb = Chel("Gleb")

stul = Stul()

stul.sit(gleb)
print(stul.sitter)

stul.stand()
print(stul.sitter)

gleb.set_weight(120)
stul.sit(gleb)
print(stul.sitter)

stul.stand()
print(stul.sitter)
