#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person():
    def __init__(self,name, designation):
        self.name = name
        self.designation = designation
    def display(self):
        print(self.name)
        print(self.designation)
    def learn(self):
        print(self.name+' Learning')
    def walk(self):
        print(self.name+' Walking')

    def eat(self):
        print(self.name+' Eating')

class Programmer(Person):
    def __init__(self,name,designation,company):
        self.company = company
        Person.__init__(self, name,designation )
    def company_name(self):
        print(self.name)
        print(self.company)
    def coding_work(self):
        print(self.name+' is doing coding')
Prg = Programmer('Rohit','coder',"CSE")
Prg.coding_work()

class Dancer(Person):
    def __init__(self,name,designation,groupName):
        self.groupName = groupName
        Person.__init__(self, name,designation )
    def group_Name(self):
        print(self.name)
        print(self.groupName)
    def dancing(self):
        print(self.name+' is dancing')
my_dancer = Dancer('Sunny','dancer',"Dancing Angels")
my_dancer.dancing()

class Singer(Person):
    def __init__(self,name,designation,bandName):
        self.bandName = bandName
        Person.__init__(self, name,designation )
    def band_Name(self):
        print(self.name)
        print(self.bandName)  
    def singing(self):
        print(self.name+' is singing')
    def play_guitar(self):
        print(self.name+' is playing guitar')
my_singer = Singer('Gandhi','Singer',"The Vocals")
my_singer.singing()
my_singer.play_guitar()

