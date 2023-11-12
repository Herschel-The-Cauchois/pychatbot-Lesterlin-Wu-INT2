from elementary_functions import *

"""The main.py file here is a small testing program cleaning all the speeches files downloaded, then checking the 
cleaning errors in that treated output."""
list1 = list_of_files("./speeches", ".txt")
for elem in list1:
    file_cleaner("./speeches/" + elem)
for elem in list_of_files("./cleaned", ".txt"):
    file_check("./cleaned/" + elem)
