from elementary_functions import *

list1 = list_of_files("./speeches", ".txt")
for elem in list1:
    file_cleaner("./speeches/" + elem)
for elem in list_of_files("./cleaned", ".txt"):
    file_check("./cleaned/" + elem)