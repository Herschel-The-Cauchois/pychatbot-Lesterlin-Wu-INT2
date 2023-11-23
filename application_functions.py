def highest_score_word(matrix: list) -> list:
    highest_score_words = {matrix[1][0]: sum(matrix[1][1:])}
    for i in range(2, len(matrix)):
        if sum(matrix[i][1:]) == highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words[matrix[i][0]] = sum(matrix[i][1:])
        elif sum(matrix[i][1:]) > highest_score_words[list(highest_score_words.keys())[0]]:
            highest_score_words = {matrix[i][0]: sum(matrix[i][1:])}
    return list(highest_score_words.keys())

