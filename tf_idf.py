from math import *
from elementary_functions import list_of_files


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
    idf = idf_method(directory)
    matrix = [["x"]]
    to_be_analyzed = list_of_files(directory, ".txt")
    is_not_indexed = True
    index = 0
    for file in to_be_analyzed:
        f = open(directory+file, "r")
        tf = tf_method(f.readline())
        print(file)
        matrix[0].append(file)
        print(file in matrix[0])
        for key in tf.keys():
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
                matrix[index].append(tf[key] * idf[key])
        is_not_indexed = True
        index = 0
    return matrix

# à résoudre : trop de 0 dans les sous listes colonnes
