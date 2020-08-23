import os
import shutil

def square(number):
    return number*number
def print_file(file_name):
    file = open(file_name,"r")
    for line in file:
        print(line)
    file.close()
def play_with_file(file_name):
    file = open(file_name,"w")
    file.write("Hello")
    file.close()
    file = open(file_name,"a")
    file.write(" Geek")
    print_file(file_name)
def move_file(old_file_location, new_file_location):
    os.mkdir(new_file_location)
    shutil.move(old_file_location,new_file_location)
def copy_file(old_file_location, new_file_location):
    os.mkdir(new_file_location)
    shutil.copy(old_file_location,new_file_location)
def rename_file(old_file_location, new_file_location):
    os.rename(old_file_location,new_file_location)

#os.remove()
'''a =5
print(a)
print(square(a))
file_name = "C:\\Users\\utumma\\Desktop\\IndiaSuperBrain\\Files_Python\\testfile.txt"
print_file(file_name)
play_with_file(file_name)
print_file(file_name)
#move_file(file_name, "C:\\Users\\utumma\\Desktop\\IndiaSuperBrain\\Files_Python\\Temp")
copy_file(file_name, "C:\\Users\\utumma\\Desktop\\IndiaSuperBrain\\Files_Python\\Temp")'''
