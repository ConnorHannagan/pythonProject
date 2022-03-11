class person:

    def __init__(self, name, age, luckynumber):
        self.name = name
        self.age = age
        self.luckynumber = luckynumber

    def gettinold(self):
        self.age +=1




p1 = person("Carl", 69, 7)

p1.gettinold()