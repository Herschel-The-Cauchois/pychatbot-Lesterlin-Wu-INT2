from math import *
from elementary_functions import list_of_files
from datetime import datetime


def tf_method(string: str) -> dict:
    """As asked in the pdf, this is the function that calculates the tf scores of each word of a string (since all
    content of the file is concatenated in a string after cleaning, it will treat all the content of the file) and
    returns it in a dictionary that associate each word with its tf idf score."""
    working_list = string.split()  # First splits the string into a list of the words by following the remaining
    # spaces in the cleaned files.
    tf_dict = {}  # Creates an empty dictionary which will contain the expected tf dictionary.
    for elem in working_list:  # Looks through all the words in the word list created.
        if elem not in tf_dict.keys():
            tf_dict[
                elem] = 1  # if an entry corresponding to the word isn't found, create an entry with the starting
            # score of 1.
        else:
            tf_dict[elem] += 1  # If such an entry already exists, adds 1 to its associated tf score.
    return tf_dict


def idf_method(directory: str) -> dict:
    """This function establishes a dictionary, connecting each unique word contained in a file found in the specified
    directory to its IDF score in a dictionary."""
    corpus = list_of_files(directory, ".txt")  # First stores in a variable the list of files in the directory.
    treated_words = []
    idf_dict = {}
    for text in corpus:
        f = open("./cleaned/" + text, "r")  # Opens each time a corresponding file in the list of files to proceed.
        treated_string = f.readline().split()  # Reads the entire content of the file with the readline method,
        # then split it into a list of strings following the whitespace separator.
        for elem in treated_string:
            if elem not in idf_dict.keys():  # If the word found isn't referenced in the dictionary, creates a new
                # entry with a score of 1 and adds it to the list of treated words in the file.
                idf_dict[elem] = 1
                treated_words.append(elem)
            elif elem not in treated_words:  # If the found word isn't treated but has an entry in the dictionary,
                # adds 1 to the special score at each discovery of it in another file.
                idf_dict[elem] += 1
                treated_words.append(elem)
        treated_words = []  # Resets the treated words list each time the function proceeds a new file.
    for key in idf_dict.keys():
        idf_dict[key] = log((len(corpus) / idf_dict[key]
            )+1)  # Calculates the IDF score from the number of files where the word was found and stores it in
        # the value of each word-key.
    return idf_dict


def tf_idf(directory: str) -> list:
    """This function produces the tf/idf matrix by first creating an empty matrix with the name of each files as
    columns, and each word found as rows. Then proceeds to replace the 0 placeholders with their TF-IDF score if it
    is not null."""
    log_file = open("tf_idf_log.txt", "w")  # Opens a log file for debugging the functions.
    idf = idf_method(directory)  # Directly creates the global idf dictionary.
    matrix = [["x"]]  # Produces a draft of the matrix by putting in the first sublist an x placeholder, that serves
    # as an aesthetic separator for rows and columns when printing.
    to_be_analyzed = list_of_files(directory, ".txt")  # Fetches the list of files that will be analyzed in the
    # directory.
    matrix[0] = matrix[0] + to_be_analyzed  # Completes the first sublist with all the column names, consisting of
    # the name of each file.
    for file in to_be_analyzed:
        log_file.write("------- [START {} : {}] -------\n".format(datetime.now(), file))
        f = open(directory + file, "r")
        tf = tf_method(f.readline())  # Creates for each file their tf dictionary.
        for key in tf.keys():
            log_file.write("Now checking key " + key + "\n")
            log_file.write("With tf value " + str(tf[key]) + "\n")  # Those log entries are done due to previous
            # loop-related issues with keys.
            is_not_indexed = True
            for i in range(0, len(matrix)):
                if matrix[i][0] == key:
                    is_not_indexed = False  # Assumes at first a word isn't index in the first elements of the
                    # remaining rows sublist. If the word in found in said rows, the boolean is set to False.
            if is_not_indexed:
                matrix.append([str(key)] + [0 for k in range(0, len(matrix[
                                                                        0]) - 1)])  # If the word isn't indexed,
                # proceeds to create a new word by creating a sublist consisting of the string of the word as the
                # first element, then 0s.
        f.close()
    for i in range(1, len(matrix[0])):
        f = open(directory + to_be_analyzed[i - 1], "r")
        tf = tf_method(f.readline())  # Since we are looping again through the files, we proceed to recreate the tf
        # dictionary each time for each file.
        for j in range(1, len(matrix)):  # Goes through all the rows to fill the associated box at the column treated
            # with the TF-IDF score.
            if matrix[j][0] in tf.keys():
                matrix[j][i] = tf[matrix[j][0]] * idf[matrix[j][0]]  # If the word is in the TF dictionary of the
                # file's keys, calculate the TF-IDF score before putting it in the appropriate box.
            if len(matrix[j]) > 9:
                log_file.write("Ghost value ? \n")
                log_file.write(to_be_analyzed[i - 1] + "\n")
                log_file.write(str(tf[matrix[j][0]] * idf[matrix[j][0]]) + "\n")
                log_file.write(matrix[j][0] + "\n")
    log_file.write("------- [END {}] -------\n\n".format(datetime.now()))  # Puts in the file log a reference end date.
    log_file.write("------- [RESULTED MATRIX {}] -------\n\n".format(datetime.now()))
    for i in range(0, len(matrix)):  # Prints in the log file the resulting matrix with the length of each rows to
        # check if they are of the correct length.
        log_file.write(str(matrix[i]) + "\n")
        log_file.write(str(len(matrix[i])) + "\n")
    log_file.close()
    return matrix  # Closes the file and return the waited matrix.

    # Former code of the tf_idf matrix production function for comparison
    """for file in to_be_analyzed:
        log_file.write("------- [START {} : {}] -------\n".format(datetime.now(), file))
        f = open(directory+file, "r")
        tf = tf_method(f.readline())
        matrix[0].append(file)
        for key in tf.keys():
            log_file.write("Now checking key "+key+"\n")
            log_file.write("With tf value " + str(tf[key]) + "\n")
            for i in range(0, len(matrix)):
                if matrix[i][0] == key:
                    is_not_indexed = False
            if is_not_indexed:
                matrix.append([str(key)])
                for j in range(1, len(matrix[0]) - 1):
                    matrix[len(matrix) - 1].append(0)
                matrix[len(matrix) - 1].append(tf[key] * idf[key])
            else:
                for j in range(0, len(matrix)):
                    if matrix[j][0] == key:
                        index = j
                if len(matrix[index]) != expected_len and len(matrix[index]) <= 9: # Trying to fix rows with len<=9
                    print("I work !")
                    for i in range(0,expected_len-len(matrix[index])):
                        matrix[index].append(0)
                matrix[index].append(tf[key] * idf[key])
                if len(matrix[index]) > 9:
                    log_file.write("Ghost value ? \n")
                    log_file.write(file+"\n")
                    log_file.write(str(tf[key] * idf[key])+"\n")
                    log_file.write(key+"\n")
        log_file.write("------- [END {}] -------\n\n".format(datetime.now()))
        is_not_indexed = True
        index = 0
        expected_len += 1
    log_file.write("------- [RESULTED MATRIX {}] -------\n\n".format(datetime.now()))
    for i in range(0,len(matrix)):
        log_file.write(str(matrix[i])+"\n")
        log_file.write(str(len(matrix[i])) + "\n")
    return matrix"""
