from abc import ABC, ABCMeta , abstractmethod
##flyweight
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
    
    

###############################################################################################################

#single tone
class singletone():
    def __new__(cls):
        return cls
    
    def __init__(self):
        self.name = None

s1 = singletone()
s1.name = 'ahmed'
s2 = singletone()

print(s1.name)
print(s2.name)
print(s1 is s2)

#########################################################################################################################
#factory
class shape (ABC) :
    def draw (self):
        pass
        
class circle (shape):
    def draw(self):
        print("drawing circle")
        
class square (shape):
    def draw(self):
        print("drawing square")

class rectangle (shape):
    def draw(self):
        print("drawing rectangle")
        
class shapeFactory():
    def create_shape (shape_type):
        if shape_type == "circle":
            return circle()
        elif shape_type == "square":
            return square()
        elif shape_type == "rectangle":
            return rectangle()
        else:
            raise ValueError("invalid shape type")
shape1 = shapeFactory.create_shape("circle")
shape2 = shapeFactory.create_shape("square")
shape3 = shapeFactory.create_shape("rectangle")

shape1.draw()
shape2.draw()
shape3.draw()   



#####################################################################################################################

#builder

class pizza():
     def __init__(self, sauce , cheese , toping):
          self.sauce = sauce
          self.cheese = cheese
          self.toping = toping
          
     def __str__(self) :
          return f'suace: {self.sauce} , the cheese : {self.cheese} , topings: {self.toping}'
     

class builder ():
     def __init__(self):
          self.sauce= None
          self.cheese = None
          self.toping = [] 
          
     def set_sauce(self , sauce):
          self.sauce = sauce
          return self
     def set_cheese (self , cheese):
          self.cheese = cheese
          return self
     
     def add_topings(self , toping):
          self.toping.append(toping)
          return self
     
     def build(self):
          return pizza(self.sauce ,self.cheese , self.toping)
     

p1 = builder()\
     .set_sauce('tomato')\
     .set_cheese('cheddar')\
     .add_topings('chicken')\
     .add_topings('mushroum')\
     .add_topings('extra cheese')\
     .build()
     
print(p1)
     


####################################################################################################
#memento
class Memento:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class player:
    def set_name(self, name):
        print("setting data", name)
        self.name = name
    
    def set_score(self, score):
        print("setting data", score)
        self.score = score
    
    def save(self):
        print("state saved")
        return Memento(self.name, self.score)
    
    def restore(self, memento):
        print("restore data")
        self.name = memento.name
        self.score = memento.score
        print(self.name)
        print(self.score)

obj = player()
obj.set_name("mohamed")
obj.set_score(100)
mem = obj.save()
obj.set_name("ahmed")  
obj.set_score(80)
obj.restore(mem)


##########################################################################################
#facade
class first:
    def operation1(self):
        print("Subsystem1 operation")

class second:
    def operation2(self):
        print("Subsystem2 operation")

class Facade:
    def __init__(self):
        self.first = first()
        self.second = second()

    def operation(self):
        self.first.operation1()
        self.second.operation2()


facade = Facade()
facade.operation()
