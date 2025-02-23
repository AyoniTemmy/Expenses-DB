class Project:
    
    def __init__(self, topic, timeframe):
       self.my_topic = topic
       self.my_timeframe = timeframe
       self.scope = '1999 - 2025'
        
    

my_project = Project('Advertisement', '20 days')
print(f"The topic for my grade 2 project is : {my_project.my_topic}")
print(f"my project scope is: {my_project.scope}")

my_project2 = Project('Physical Touch', '10 days')
print(f"The topic for my grade 2 project is : {my_project2.my_topic}")
print(f"my project scope is: {my_project2.scope}")

class Person():
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def greet (self):
        print(f"Good day {self.Name}!")
    def change (self, name):
        print(f"Good morning {name}!")
        print(f"Are you {self.Age} years old?")
        
A = Person("Ada", 30)
A.greet()
A.change("Kunle Remi")

students = ["Ade", "Bashir"]
print (students[1])
print("abc. DEF".capitalize())
person = {'name': 'Alice', 'age': 30}
print (person.get('name'))
print(min(max(False,-3,-4), 2,7))