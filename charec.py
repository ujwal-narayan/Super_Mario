""" List of All characters and their capabilities """
class characters :
        """ Common for all characters """
        def __init__(self , x, y ):
            """ Figure out the x and Y shit later """
            self._x = x
            self._y = y 
            self._ch = ch
            self.speed = 0 
            self.damage = 0 
            self.dies = True
            self.lives = 0
        def get_type(self):
            """ Returns the characters name"""
            return self._type


class Mario(characters) :
    """ issa me , Mario """
    def __init__(self , x , y , lives = config.lives ):
        super(Mario, self ).__init__(x,y)
        self.lives = lives 
        self.score = 0 
        self.speed = 1 
        self.damage = 10
        
        
class Mushroom(characters):
    """ Low level easy peasy enimies """
    def ___init___(self , x, y ):
        super(Mushroom , self ).__init__(x,y)
        self.lives = 1 
        self.damage = 50 
        self.speed = 5

class Turtles(characters):
    """Medium level annoying beasts """
    def __init__(self, x, y) :
        super(Turtles,self).__init__(x,y)
        self.lives = 1
        self.damage =50
        self.speed = 10

class DarthVader(characters):
    """I AM THE SENATE < the big bad boss himself """
    def __init__(self, x, y,lives = 2):
        super(DarthVader , self).__init__(x,y)
        self.damage = 10
        self.lives = 2 
        self.speed = 10             
        



