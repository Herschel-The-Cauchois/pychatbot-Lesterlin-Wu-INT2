from elementary_functions import president_fullname, name_extractor, list_of_files

def highest_score_word(matrix: list) -> list:
    highest_score_words = {matrix[1][0]: sum(matrix[1][1:])}
    for i in range(2, len(matrix)):
        if sum(matrix[i][1:]) == highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words[matrix[i][0]] = sum(matrix[i][1:])
        elif sum(matrix[i][1:]) > highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words = {matrix[i][0]: sum(matrix[i][1:])}
    return list(highest_score_words.keys())


def chiracs_favorite_word(matrix: list) -> list:
    final_list = ["sample_10"]
    for i in range(0, len(matrix[0])):
        if matrix[0][i] == "Nomination_Chirac1_cleaned.txt":
            ind_first_speech = i
        if matrix[0][i] == "Nomination_Chirac2_cleaned.txt":
            ind_second_speech = i
    chirac_dic = {}
    for i in range(1, len(matrix)):
        chirac_dic[matrix[i][0]] = matrix[i][ind_first_speech] + matrix[i][ind_second_speech]
    for key in chirac_dic.keys():
        if float(chirac_dic[key]) < float(final_list[0].split("_")[1]) and chirac_dic[key] != 0:
            final_list = [key + "_" + str(chirac_dic[key])]
        elif float(chirac_dic[key]) == float(final_list[0].split("_")[1]) and chirac_dic[key] != 0:
            final_list.append(key + "_" + str(chirac_dic[key]))
    final_list = [k.split("_")[0] for k in final_list]
    return final_list


def nation_word_president(matrix: list):
    list_of_presidents = []
    most_patriotic_president = [0,10]
    for i in range(1,len(matrix)):
        if matrix[i][0] == "nation":
            working_collection = matrix[i]
    for i in range(1, len(working_collection)):
        if working_collection[i] != 0:
            if working_collection[i] < most_patriotic_president[1]:
                most_patriotic_president = [i, working_collection[i]]
            list_of_presidents.append(i)
    for i in range(0, len(list_of_presidents)):
        if list_of_presidents[i] == 5 or list_of_presidents[i] == 6:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches",".txt")))[4]
        elif list_of_presidents[i] == 1 or list_of_presidents[i] == 2:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches",".txt")))[0]
        else:
            list_of_presidents[i] = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[i]
    if most_patriotic_president[0] == 5 or most_patriotic_president[0] == 6:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[4]
    elif most_patriotic_president[0] == 1 or most_patriotic_president[0] == 2:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[0]
    else:
        most_patriotic_president = president_fullname(name_extractor(list_of_files("./speeches", ".txt")))[i]
    return sorted(list(set(list_of_presidents))), most_patriotic_president


def first_ecological_president(matrix: list):
    presidents = []
    climate = []
    for i in range(1,len(matrix)):
        if matrix[i][0] == "climat":
            climate = matrix[i]
    chronological_order = ["Giscard", "Mitterand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    for j in range(1, len(climate)):
        if climate[j] != 0:
            presidents.append(matrix[0][j])
    for elem in chronological_order:
        for i in range(0, len(presidents)):
            if elem in presidents[i]:
                return elem


def common_words_to_all(matrix: list):
    common_words = []
    for i in range(1, len(matrix)):
        common_words.append(matrix[i][0])
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0 and matrix[i][0] in common_words:
                common_words.remove(matrix[i][0])
    return common_words

