from math import *
from elementary_functions import list_of_files
from datetime import datetime


def tf_method(string: str) -> dict:
    working_list = string.split()
    tf_dict = {}
    for elem in working_list:
        if elem not in tf_dict.keys():
            tf_dict[elem] = 1
        else:
            tf_dict[elem] += 1
    return tf_dict


def idf_method(directory: str) -> dict:
    corpus = list_of_files(directory, ".txt")
    treated_words = []
    idf_dict = {}
    for text in corpus:
        f = open("./cleaned/" + text, "r")
        treated_string = f.readline().split()
        for elem in treated_string:
            if elem not in idf_dict.keys():
                idf_dict[elem] = 1
                treated_words.append(elem)
            elif elem not in treated_words:
                idf_dict[elem] += 1
                treated_words.append(elem)
        treated_words = []
    for key in idf_dict.keys():
        idf_dict[key] = log(1 / (idf_dict[key] / len(corpus)))
    return idf_dict


def tf_idf(directory: str) -> list:
    log_file = open("tf_idf_log.txt","w")
    idf = idf_method(directory)
    matrix = [["x"]]
    to_be_analyzed = list_of_files(directory, ".txt")
    matrix[0] = matrix[0] + to_be_analyzed
    for file in to_be_analyzed:
        log_file.write("------- [START {} : {}] -------\n".format(datetime.now(), file))
        f = open(directory + file, "r")
        tf = tf_method(f.readline())
        for key in tf.keys():
            log_file.write("Now checking key " + key + "\n")
            log_file.write("With tf value " + str(tf[key]) + "\n")
            is_not_indexed = True
            for i in range(0, len(matrix)):
                if matrix[i][0] == key:
                    is_not_indexed = False
            if is_not_indexed:
                matrix.append([str(key)]+[0 for k in range(0,len(matrix[0])-1)])
        f.close()
        print(matrix)
    for i in range(1,len(matrix[0])):
        print(i)
        f = open(directory + to_be_analyzed[i-1], "r")
        tf = tf_method(f.readline())
        for j in range(1,len(matrix)):
            if matrix[j][0] in tf.keys():
                matrix[j][i] = tf[matrix[j][0]] * idf[matrix[j][0]]
    log_file.write("------- [END {}] -------\n\n".format(datetime.now()))
    log_file.write("------- [RESULTED MATRIX {}] -------\n\n".format(datetime.now()))
    for i in range(0, len(matrix)):
        log_file.write(str(matrix[i]) + "\n")
        log_file.write(str(len(matrix[i])) + "\n")
    return matrix
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

# à résoudre : trop de nombres dans les sous listes colonnes indice : longueur ligne en fonction somme des tfs documents
