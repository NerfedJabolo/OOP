#create a Student class
class Student:
    __id = 0
    #create init function with private name and id
    def __init__(self, name):
        self.__name = name
        self.__id = Student.__id
        Student.__id += 1
    #get name
    def get_name(self):
        return self.__name
    #get id
    def get_id(self):
        return self.__id
    #set name
    def set_name(self, name):
        self.__name = name

#create student objects
student1 = Student("John")
student2 = Student("Mary")
student3 = Student("Bob")
print(student1.get_id(), student2.get_id(), student3.get_id())
