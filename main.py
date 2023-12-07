from elementary_functions import *
from tf_idf import *
from application_functions import *
from q_tokenization import *
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

selection = 0  # This part is for the menu selection.

while selection != "x":
    # This launches the loop of the start menu. It subdivides in another while loop, when selection is equal to 1
    # for the part 1 functions and another while loop for the part 2 when selection is equal to 2.
    print("-------- [START MENU] --------")
    print("Welcome to PyChatBot v0.1.1, written by Julien Wu and Lesterlin Raphaël. Please enter an integer or an x to "
          "select one option from the menu. Please wait 5s before each new instruction. Based on the investiture "
          "speeches of all french president since VGE. Dedicated to EFREI PARIS.")
    print("\n")
    print("[1] - Access the basic speech analysis functionalities.")
    print("[2] - Enter Chatbot Mode.")
    print("[x] - Stops the program.")
    print("\n")
    selection = str(input("Enter an option :"))
    option = 0
    while selection == "1":
        while option != "x" and option != "b":
            temp = ""
            print("\n\n\n")
            print("-------- [BASIC MENU] --------")
            print("Please select a basic functionality among the proposed list.")
            print("\n")
            print("[1] - Display the list of least important words in the president speech corpus.")
            print("[2] - Display the word(s) with the highest TF-IDF score.")
            print("[3] - Display the most repeated words by president Chirac.")
            print("[4] - Display the list of presidents who spoke of the nation and the most patriotic of them.")
            print("[5] - Displays the name of the first president who talks about ecology.")
            print(
                "[6] - Displays the list of words, that are not unimportant in the TF-IDF classification, common to all"
                " speeches.")
            print("[b] - Goes back to main menu.")
            print("[x] - Stops the program.")
            print("\n")
            option = input("Enter an option :")
            if option == "1":
                for i in range(0, len(least_important_words(tf_idf_dic))):
                    if i == len(least_important_words(tf_idf_dic)) - 1:
                        temp += least_important_words(tf_idf_dic)[i] + "."
                    else:
                        temp += least_important_words(tf_idf_dic)[i] + ", "
                print("The words of lowest importance in all of the speeches are : " + temp)
                sleep(5)
            elif option == "2":
                # For each involved function that returns a list, a similar loop is used to concatenate in the temp
                # string each string contained in the list.
                for i in range(0, len(highest_score_word(tf_idf_dic))):
                    if i == len(highest_score_word(tf_idf_dic)) - 1:
                        # This only triggers if the loop arrives at the last element of the result list, therefore
                        # ending the new string with a dot.
                        temp += highest_score_word(tf_idf_dic)[i] + "."
                    else:
                        temp += highest_score_word(tf_idf_dic)[i] + ", "
                print("The words with the highest score are : " + temp)
                sleep(5)  # The sleep function allows the user to be able to read the answer before looping back.
            elif option == "3":
                for i in range(0, len(chiracs_favorite_word(tf_idf_dic))):
                    if i == len(chiracs_favorite_word(tf_idf_dic)) - 1:
                        temp += chiracs_favorite_word(tf_idf_dic)[i] + "."
                    else:
                        temp += chiracs_favorite_word(tf_idf_dic)[i] + ", "
                print("Chirac's most common words in his speech are : " + temp)
                sleep(5)
            elif option == "4":
                for i in range(0, len(nation_word_president(tf_idf_dic)[0])):
                    if i == len(nation_word_president(tf_idf_dic)[0]) - 1:
                        temp += nation_word_president(tf_idf_dic)[0][i] + "."
                    else:
                        temp += nation_word_president(tf_idf_dic)[0][i] + ", "
                print(
                    "The president who use the word nation in their speech are : " + temp + " The most patriotic "
                                                                                            "president of "
                                                                                            "them all with its most "
                                                                                            "common use "
                                                                                            "is " +
                    nation_word_president(
                        tf_idf_dic)[1] + ".")
                sleep(5)
            elif option == "5":
                print("The first president who mentioned ecological themes such as ecology and climate is : " +
                      first_ecological_president(tf_idf_dic))
                sleep(5)
            elif option == "6":
                for i in range(0, len(common_words_to_all(tf_idf_dic))):
                    if i == len(common_words_to_all(tf_idf_dic)) - 1:
                        temp += common_words_to_all(tf_idf_dic)[i] + "."
                    else:
                        temp += common_words_to_all(tf_idf_dic)[i] + ", "
                # A small variation of the loop is used here in the case there is no common words to all speeches.
                if temp == "":
                    print("There are no important words common to all speeches.")
                else:
                    print("The words common to all speeches are : " + str(temp))
                sleep(5)
            elif option == "b":
                selection = 0  # Changes the selection variable to cancel the while loop of part 1 and reloop
                # on the start menu input.
            elif option == "x":
                selection = "x"  # Changes the selection variable to x in order to terminate this while loop and
                # directly trigger the goodbye message instruction.
            else:
                # Instruction in case of non recognized input.
                print(
                    "Input not recognized. Please enter a valid character as put between square brackets in the menu.")
                sleep(5)
            print("\n")
    while selection == "2":
        print("Part 2 function test :\n")
        print("\n")
        print(is_in_corpus(question_words(input("Enter a question :")), tf_idf_dic))
        print("Part 2 function test done.")
        sleep(5)
        selection = "x"
    if selection == "x":
        print("We hope you have enjoyed your experience on Python Chatbot 0.1.1. Have a good day :)")
        sleep(3)
        # And here a nice goodbye message !
    else:
        # Message in case of non recognized input.
        print("Input not recognized. Please enter a valid character as put between square brackets in the menu.")
        sleep(5)
        print("\n")
