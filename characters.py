class Player:
    
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self._level = 1
        self.score = 0
    #set_lives method
    def _set_lives(self, lives):
        if lives >= 0:
            self.lives = lives
        else:
            print("Live can't drop below 0")
    
    #get_lives method
    def _get_lives(self):
        return self.lives
    
    def _set_level(self, level):
        if level>=0:
            delta = self.level - level
            self.level = level
            self.score = delta*1000
        
    def _get_level(self):
        return self.level
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
    
    level = property(_get_level, _set_level)