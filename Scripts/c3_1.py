class Person:
    n =10
    def __init__(self, name, age):
        print 'init '
        self.__name=name
        self.__age=age
    def __del__(self):
        print 'releasig '
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name is',self.__name
    #@staticmethod 
    def wel():
        print 'welcome to person class'
 
        
p1=Person('vijay',33)
print dir(Person)
print dir(p1)
print Person.n
print p1.n
print p1.wel()
print Person.wel()

#print p1.__name__ #AttributeError: Person instance has no attribute '__name__'
print p1._Person__name # name mangling 
 
    


          
