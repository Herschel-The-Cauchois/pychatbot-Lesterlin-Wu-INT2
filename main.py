from elementary_functions import *
from tf_idf import *
from application_functions import *
from time import sleep  # Import the functions of each file and an additional sleep functions for user comfort.

list_files = list_of_files("./speeches", ".txt")  # First create the list of files in the speech folder.

for elem in list_files:
    # Proceeds to clean the files and use the file_check to report any errors in the cleaning process.
    if elem[:-4]+"_cleaned.txt" not in list_of_files("./cleaned", ".txt"):
        file_cleaner("./speeches/" + elem)
        file_check("./cleaned/" + elem)

for files in list_of_files("./cleaned", ".txt"):
    # This loop was used to report any problems in the processing of counting words for the TF index for each file.
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

tf_idf_dic = tf_idf("./cleaned/")  # Creates the TF-IDF matrix that will be used and puts it in a variable.

option = 0  # To emulate the Do - While algorithmic loop by setting the option selector variable to 0, which will
# trigger the loop.

while option != "x":
    temp = ""
    print("-------- [START MENU] --------")
    print("Welcome to PyChatBot v0.1, written by Julien Wu and Lesterlin Raphaël. Please enter an integer or an x to "
          "select one option from the menu. Please wait 5s before each new instruction. Based on the investiture "
          "speeches of all french president since VGE. Dedicated to EFREI PARIS.")
    print("\n")
    print("[1] - Display the list of least important words in the president speech corpus.")
    print("[2] - Display the word(s) with the highest TF-IDF score.")
    print("[3] - Display the most repeated words by president Chirac.")
    print("[4] - Display the list of presidents who spoke of the nation and the most patriotic of them.")
    print("[5] - Displays the name of the first president who talks about ecology.")
    print("[6] - Displays the list of words, that are not unimportant in the TF-IDF classification, common to all "
          "speeches.")
    print("[x] - Stops the program.")
    print("\n")
    option = input("Enter an option :")
    if option == "1":
        print("WIP.")
    elif option == "2":
        # For each involved function that returns a list, a similar loop is used to concatenate in the temp string
        # each string contained in the list.
        for i in range(0, len(highest_score_word(tf_idf_dic))):
            if i == len(highest_score_word(tf_idf_dic))-1:
                # This only triggers if the loop arrives at the last element of the result list, therefore ending the
                # new string with a dot.
                temp += highest_score_word(tf_idf_dic)[i] + "."
            else:
                temp += highest_score_word(tf_idf_dic)[i]+", "
        print("The words with the highest score are : "+temp)
        sleep(5)
    elif option == "3":
        for i in range(0, len(chiracs_favorite_word(tf_idf_dic))):
            if i == len(chiracs_favorite_word(tf_idf_dic))-1:
                temp += chiracs_favorite_word(tf_idf_dic)[i] + "."
            else:
                temp += chiracs_favorite_word(tf_idf_dic)[i]+", "
        print("Chirac's most common words in his speech are : "+temp)
        sleep(5)
    elif option == "4":
        for i in range(0, len(nation_word_president(tf_idf_dic)[0])):
            if i == len(nation_word_president(tf_idf_dic)[0])-1:
                temp += nation_word_president(tf_idf_dic)[0][i] + "."
            else:
                temp += nation_word_president(tf_idf_dic)[0][i]+", "
        print("The president who use the word nation in their speech are : "+temp+" The most patriotic president of "
                                                                                  "them all with its most common use "
                                                                                  "is "+nation_word_president(
            tf_idf_dic)[1])
        sleep(5)
    elif option == "5":
        print("The first president who mentioned ecological themes such as ecology and climate is : " +
              first_ecological_president(tf_idf_dic))
        sleep(5)
    elif option == "6":
        for i in range(0, len(common_words_to_all(tf_idf_dic))):
            if i == len(common_words_to_all(tf_idf_dic))-1:
                temp += common_words_to_all(tf_idf_dic)[i] + "."
            else:
                temp += common_words_to_all(tf_idf_dic)[i]+", "
        # A small variation of the loop is used here in the case there is no common words to all speeches.
        if temp == "":
            print("There are no important words common to all speeches.")
        else:
            print("The words common to all speeches are : "+str(temp))
        sleep(5)
    elif option == "x":
        print("We hope you have enjoyed your experience on Python Chatbot 0.1. Have a good day :)")
        # And here a nice goodbye message !
