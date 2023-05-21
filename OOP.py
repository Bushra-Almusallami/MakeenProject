class person:
    no_of_person=0
    def __init__(self,name,age):
        self.name=name
        self.__age= age
        person.no_of_person +=1 #number of persons is increasing
        
    #def descrip(self):
    def __str__(self):
        return "This person name is {} and {} yers old".format(self.name, self.__age)
    def set_age(self, new_age):
        self.__age= new_age
    
p1=person("Hamza",22)
p2=person("Ali",32)
#print(p1)
#print(type(p1))
print(person.no_of_person) #number of persons

#print(dir(person))
#print(p1.__str__())# same output of dir

p2.set_age(40)
#p2.age=42
print(p2.__str__())
