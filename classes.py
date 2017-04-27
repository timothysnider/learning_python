class Hero:
    '''
    a hero who is allegic to apples
    '''
    def __init__(self, name):
        '''
        whateever we want
        '''
        self.name=name
        self.health=100
    def eat(self, food):
        if(food=='apple'):
            self.health-=100
        elif(food=='ham'):
            self.health+=20
Bob=Hero('Bob')
print(Bob.name)
print(Bob.health)
Bob.eat('ham')
print(Bob.health)
