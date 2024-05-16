class car():
    def __init__(self, model , color):
        self.model = model
        self.color = color
        
class factory:
    _cars= {}
    
    def get_car(self , model , color):
        key = (model , color)
        if key not in factory._cars:
            factory._cars[key] = car(model , color)
        return self._cars[key]
    
f = factory()
c1 = f.get_car('toyota' , 'white')
c2 = f.get_car('toyota' , 'white')

print(c1.model , c1.color)
print(c2.model , c2.color)

print(c1 is c2)   