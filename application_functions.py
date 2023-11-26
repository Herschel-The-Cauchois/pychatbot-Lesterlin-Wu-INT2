from elementary_functions import president_fullname, name_extractor, list_of_files


def highest_score_word(matrix: list) -> list:
    """This function displays the list of words with the highest TF-IDF score, aka the rarest according to the TF-IDF
    method."""
    highest_score_words = {matrix[1][0]: sum(matrix[1][1:])}  # Creates a dictionary with the first word of the TF-IDF
    # matrix and its total TF-IDF score (sum of its score in each file)
    for i in range(2, len(matrix)):  # Loops through each row of the matrix except the column header and first one.
        if sum(matrix[i][1:]) == highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words[matrix[i][0]] = sum(matrix[i][1:])  # If the word at ith row has a total score equal
            # to the one of the words already present in the dictionary, adds the word as a key and the score as a
            # value inside the dictionary.
        elif sum(matrix[i][1:]) > highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words = {matrix[i][0]: sum(matrix[i][1:])}  # If the word at ith row has a total score
            # superior to the word inside the highest score dic, resets the dictionary with the word with higher
            # score as its only entry and its score as the value.
    return list(highest_score_words.keys())  # Returns the list of keys in the highest score words dictionary.


def chiracs_favorite_word(matrix: list) -> list:
    """As the silly name of the function indicates, it returns the list of the most repeated words by president
    Chirac outside unimportant words."""
    final_list = ["sample_10"]  # Initialise the list that wille be returned with a sample word and a score so high
    # it will be replaced.
    for i in range(0, len(matrix[0])):
        """Runs through the column headers to find the index of the columns of Chirac's speeches to put them in a 
        local variable."""
        if matrix[0][i] == "Nomination_Chirac1_cleaned.txt":
            ind_first_speech = i
        if matrix[0][i] == "Nomination_Chirac2_cleaned.txt":
            ind_second_speech = i
    chirac_dic = {}  # Creates a temporary dictionary for the job.
    for i in range(1, len(matrix)):
        # The dictionary will be filled with each word of the matrix as a key and the sum of their TF-IDF score in
        # each speech of Chirac as a value.
        chirac_dic[matrix[i][0]] = matrix[i][ind_first_speech] + matrix[i][ind_second_speech]
    for key in chirac_dic.keys():
        if float(chirac_dic[key]) < float(final_list[0].split("_")[1]) and chirac_dic[key] != 0:
            final_list = [key + "_" + str(chirac_dic[key])]  # As it goes through the keys of the dictionary, if its
            # value is inferior to the float number associated with the word in the string-variable, resets the list
            # with a string containing the key followed by an underscore and its value.
        elif float(chirac_dic[key]) == float(final_list[0].split("_")[1]) and chirac_dic[key] != 0:
            final_list.append(key + "_" + str(chirac_dic[key]))  # If the key's value in the dictionary is equal,
            # appends a new string-variable to the list.
    final_list = [k.split("_")[0] for k in final_list]  # Splits each string value with the underscore as separator
    # and appends the key-words to the final list via comprehension.
    return final_list


def nation_word_president(matrix: list):
    """This function is polyvalent : it looks to return both the list of the names of presidents that mention the
    word nation, the most patriotic referenced here being the president who uses its word the most."""
    list_of_presidents = []  # Creates the list that will host the names of presidents that mention the word "nation".
    most_patriotic_president = [0, 10]  # Creates a 2 element list that references the name of a start most patriotic
    # president, then a TF-IDF score high enough to be replaced by the algorithm.
    for i in range(1, len(matrix)):
        if matrix[i][0] == "nation":
            working_collection = matrix[i]  # Creates a working list with the row of the matrix that is referenced by
            # the word "nation" as its start.
    for i in range(1, len(working_collection)):
        # The function's core. Uses a basic minimum-looking algorithm by replacing the most patriotic president list
        # with the index associated with the president's name and the TF-IDF score of the word nation in its column
        # each time it is found a lower TF-IDF score.
        if working_collection[i] != 0:
            if working_collection[i] < most_patriotic_president[1]:
                most_patriotic_president = [i, working_collection[i]]
            list_of_presidents.append(i)  # And if the TF-IDF score isn't 0 as stated in the if condition, appends it
            # to the list of president who mentions it.
    for i in range(0, len(list_of_presidents)):
        # In the list of presidents, these branches replaces the index references with the president's name. Since
        # there is sometimes two speeches file, two if it is found that the index references the files of a president
        # with 2 speeches.
        if list_of_presidents[i] == 5 or list_of_presidents[i] == 6:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[4]
        elif list_of_presidents[i] == 1 or list_of_presidents[i] == 2:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[0]
        else:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[i]
    # Proceeds to do the same in the most patriotic president variable.
    if most_patriotic_president[0] == 5 or most_patriotic_president[0] == 6:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[4]
    elif most_patriotic_president[0] == 1 or most_patriotic_president[0] == 2:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[0]
    else:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[i]
    return sorted(list(set(list_of_presidents))), most_patriotic_president  # The set trans-typing removes duplicates
    # and the sorted function deals with the randomness that can appear with such operation.


def first_ecological_president(matrix: list):
    """This function returns the name of the first president who mentions the word climate."""
    presidents = []
    climate = []
    for i in range(1, len(matrix)):
        if matrix[i][0] == "climat":
            climate = matrix[i]  # Looks for the row/sublist with the word climate as the first element, the word
            # ecology being non-existent in every file.
    chronological_order = ["Giscard", "Mitterand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    # This allows us to search the first president which chronologically said that word.
    for j in range(1, len(climate)):
        if climate[j] != 0:
            presidents.append(matrix[0][j])  # If the TF-IDF score of this word in a column is not 0, appends the
            # column header to the president list.
    for elem in chronological_order:
        # This loop runs through each president in the chronological order list.
        for i in range(0, len(presidents)):
            # The first time it finds in the president list the name of a president in which the word is mentioned in
            # his speech, it returns its name.
            if elem in presidents[i]:
                return elem


def common_words_to_all(matrix: list):
    """This functions returns the list of words that are not unimportant, and present in each speech file."""
    common_words = []  # Creates an empty list for the future result.
    for i in range(1, len(matrix)):
        common_words.append(matrix[i][0])  # Appends first a new word to the common words list.
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0 and matrix[i][0] in common_words:
                common_words.remove(matrix[i][0])  # If in the row, one of the TF-IDF index is 0, the word is then
                # removed from the common words list.
    return common_words
