## an app that stores / loades date about different developers
# basic CRUD --- deseori solicitata incepatorilor --- BREAD
# * creat (save)    developer data
# * read (citesti)  developer data
# * update          developer data
# * delete          developer data
# ** after --- sortare si flitrare 
import os
from os import remove
from os.path import exists


name        = "John"
experience  = 5         # Years
success     = 90        # %
rate        = 30        # $/h

# -------- FUNCTION creat/save -------- #
def create(name, experience, success, rate):
    file = open("E:\\Doc pers\\IT cursuri\\VANAR centru\\Phyton\\Bazic_folder\\DEV-APP\\data\\"+name+"-dev.csv", "w")
    file.write(name + "," + str(experience) + "," + str(success) + "," + str(rate))
    file.close()
# -------- FUNCTION creat/save -------- #


# -------- FUNCTION read/load -------- #
def read(name):
    if exists("E:\\Doc pers\\IT cursuri\\VANAR centru\\Phyton\\Bazic_folder\\DEV-APP\\data\\"+name+"-dev.csv"):
        file = open("E:\\Doc pers\\IT cursuri\\VANAR centru\\Phyton\\Bazic_folder\\DEV-APP\\data\\"+name+"-dev.csv", "r")
        data = file.read()
        file.close()

        name, experience, success, rate = data.split(",")

        experience = int(experience)
        success = int(success)
        rate = int(rate)

        return[name, experience, success, rate]
    else:
        return None
# -------- FUNCTION read/load -------- #


# -------- FUNCTION Menu  -------- #
def menu_function():
    print("##########################")
    print("1. add ")
    print("2. view ")
    print("3. delete ")
    print("0. exit" )
    print("##########################")
    
    op = int(input("--> "))
    return (op)
# -------- FUNCTION Menu  -------- #


######### APP ############
while True:
    # HW1 - Menu function
    # HW2 - add option 3 - delete, name < input, delete the file, hint os, os.path   
    option = menu_function()

    if option == 1:
        name        = input("name: ")
        experience  = input("experience: ")
        success     = input("success(%): ")
        rate        = input("rate($/h): ")
        create(name, experience, success, rate)
        # HW3. Add a success message 
        print("Developer - ", name, " is successfull registreted !!! ")
        
    
    if option == 2:
        name        = input("name: ")
        date = read(name)
        if date != None:
            name, experience, success, rate = date
            print(name, experience, success, rate)
        else:
            print(name, "was not found !")

    if option == 3:
        if exists("E:\\Doc pers\\IT cursuri\\VANAR centru\\Phyton\\Bazic_folder\\DEV-APP\\data\\"+name+"-dev.csv"):
            name        = input("name: ")
            if name == name:
                file = remove("E:\\Doc pers\\IT cursuri\\VANAR centru\\Phyton\\Bazic_folder\\DEV-APP\\data\\"+name+"-dev.csv")
                print("Developer: ", name, " was removed from data folder !!! ")
            else:
                print( name, "- was not found !")
        else:
            print(name, "- was not found ! ") 
                

    if option == 0:
        break
    
"""
# -------- FUNCTION Delete -------- #
def delete():
    name        = input("name: ")
    file = name.csv     # ------ aici greseala nu se poate de atribuit file .csv la o valoare str 
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file delited")
    else:
        print("file not found")
  
# -------- FUNCTION Delete -------- #

"""
    



