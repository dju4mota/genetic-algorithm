from math import inf 
class Gene():
    
    apitdao =  -inf
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = format(x, '#08b')
        self.y = format(y, '#09b')
    

    def setValores(self, x,y):
        self.x = x
        self.y = y