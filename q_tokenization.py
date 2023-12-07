

def question_words(question: str):
    """This functions takes as a parameter a question-string and processes it like the text files before returning
    a list of the processed words of the question."""
    temp1 = question.split()  # Begins by splitting the questions by words using the default whitespace separator.
    for i in range(0, len(temp1)):
        temp1[i] = list(temp1[i])  # Then proceeds to split each word into a list of its characters.
        j = 0
        while j < len(temp1[i]):  # loops through each word-list of characters.
            if temp1[i][j] == "'" and temp1[i][j-1] in "ldmntsj":
                # Here, proceeds to remove characters such as l' or d' in french which may confuse the chatbot.
                del temp1[i][j-1]
                del temp1[i][j-1]
            if temp1[i][j] in "-_.?!,;:/§'\"":
                # Removes punctuation.
                del temp1[i][j]
            elif 64 < ord(temp1[i][j]) < 91:
                # Turns capital letter into lowercase letters.
                temp1[i][j] = chr(ord(temp1[i][j]) + 32)
            j += 1
        temp1[i] = "".join(temp1[i])  # Proceeds then to merge the lists of characters into a word-string.
    i = 0
    while i < len(temp1):
        # Proceeds to clean up in the list of words the empty strings and strings with only punctuation.
        if temp1[i] == "":
            del temp1[i]
        elif temp1[i][0] in "-_.?!,;:/§'\"":
            del temp1[i]
        i += 1
    return temp1   # Returns the expected list.


def is_in_corpus(question: list, matrix: list):
    """This functions takes a list of words and produces a list of the words common to the corpus and that list."""
    list_of_corpus_words = []
    intersection = []
    for i in range(1, len(matrix)):
        list_of_corpus_words.append(matrix[i][0]) # For less line codes, we create directly a list of the words
        # in the corpus there.
    for word in question:
        if word in list_of_corpus_words:
            intersection.append(word)  # If a word in the question belongs to the list of the corpus' words, it is
            # Added to the common words list.
    return intersection


def question_tf_idf(question: list, idf: dict, matrix: list):
    """This functions processes the question as a list of its words to produce the TF-IDF matrix of its words present
    in the text corpus as done by previous function."""
    common_words = is_in_corpus(question, matrix)  # Stores in a variable the list of common words.
    matrix_result = [["x", "Score"]]  # Initialize the resulting matrix with a more visually understandable beginning.
    for key in idf.keys():
        if key in common_words:
            # If the idf dictionary key is in the common words, proceeds to add to the resulting matrix the
            # number of times encountered in question / length of question string ratio with the associated word.
            matrix_result.append([key, ((question.count(key) / len(question)) * idf[key])])
        else:
            # Else, just appends a 0.
            matrix_result.append([key, 0])
    return matrix_result
