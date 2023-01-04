#create a Student class
class Student:
    #create init function with private name and id
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    #get name
    def get_name(self):
        return self.__name
    #get id
    def get_id(self):
        return self.__id
    #set name
    def set_name(self, name):
        self.__name = name
    #set status
    def set_status(self, status):
        if status == "Active" or status == "Inactive" or status == "Expelled" or status == "Finished":
            self.__status = status
    #get status
    def get_status(self):
        return self.__status

    

#create student objects
student1 = Student("John", 1)
student2 = Student("Mary", 2)
student3 = Student("Bob", 3)
print(student1.get_id(), student2.get_id(), student3.get_id())
