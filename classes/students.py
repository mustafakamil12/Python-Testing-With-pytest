class Student:
    def __init__(self,first_name,last_name,department,age,specialist,id):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.age = age
        self.specialist = specialist
        self.id = id

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def student_info(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old and studies {self.specialist}"