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
