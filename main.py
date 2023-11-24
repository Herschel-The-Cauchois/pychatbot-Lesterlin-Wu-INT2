from elementary_functions import *
from tf_idf import *
from application_functions import *

list_files = list_of_files("./speeches", ".txt")

for elem in list_files:
    if elem[:-4]+"_cleaned.txt" not in list_of_files("./cleaned", ".txt"):
        file_cleaner("./speeches/" + elem)
        file_check("./cleaned/" + elem)

for files in list_of_files("./cleaned", ".txt"):
    f = open("./cleaned/"+files, "r")
    treated_line = f.readline()
    dict1 = tf_method(treated_line)
    for string in treated_line:
        if len(string) != 1:
            if dict1[string] != treated_line.count(string):
                print(False)
                print(string)
                print(dict1[string])
                print(treated_line.count(string))

tf_idf_dic = tf_idf("./cleaned/")
print(highest_score_word(tf_idf_dic))
print(chiracs_favorite_word(tf_idf_dic))
