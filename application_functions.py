def highest_score_word(matrix: list) -> list:
    highest_score_words = {matrix[1][0]: sum(matrix[1][1:])}
    for i in range(2, len(matrix)):
        if sum(matrix[i][1:]) == highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words[matrix[i][0]] = sum(matrix[i][1:])
        elif sum(matrix[i][1:]) > highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words = {matrix[i][0]: sum(matrix[i][1:])}
    return list(highest_score_words.keys())


def chiracs_favorite_word(matrix: list):
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
