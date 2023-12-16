from datetime import datetime


def generate_answer(question_matrix: list, relevant_document: str):
    """Function that will take the TF-IDF matrix of a question and the most relevant document corresponding to it,
    then proceeds to find the word (or words if equal TF-IDF score in the question) with the highest score,
    then return as a base answer the line(s) of the relevant speech document."""
    log_file = open("generation_log.txt", "a", encoding="utf-8")  # To be able to have more insight in the
    # answer generation process, we have created a log file.
    f = open("./speeches/"+relevant_document, "r", encoding="utf-8")
    log_file.write("------- [NEW GENERATION {} ] -------\n".format(datetime.now()))
    speech_lines = f.readlines()  # Converts the base speech into a list of the speech's lines.
    relevant_word = ["", 0]  # The structure of the list is done so that there is stored the relevant word and
    # Its TF-IDF score.
    similar_scores = []
    for i in range(1, len(question_matrix)):
        if question_matrix[i][1] > relevant_word[1]:
            # If a word with a higher TF-IDF score is found, the words with similar score list is reset and the
            # new relevant word is pushed associated with its TF-IDf score in the relevant word variable.
            relevant_word = [question_matrix[i][0], question_matrix[i][1]]
            similar_scores = []
        elif question_matrix[i][1] == relevant_word[1]:
            # If a word has a similar TF-IDF score as the relevant word, appends it to the words with similar score list
            similar_scores.append(question_matrix[i][0])
    if len(similar_scores) == 0:
        # If there is no word with similar score, directly searches for the first line in the relevant speech
        # that contains the most relevant word and returns it.
        log_file.write("Relevant word associated : "+relevant_word[0]+"\n")
        for i in range(0, len(speech_lines)):
            if relevant_word[0] in speech_lines[i]:
                log_file.write("Relevant associated speech line found : "+speech_lines[i]+"\n")
                log_file.write("------- [ANSWER GENERATED {} ] -------\n".format(datetime.now()))
                return speech_lines[i]
    else:
        # Else, will proceed to create a final base sentence adding each time a sentence containing the relevant words
        # into the final sentence string.
        similar_scores.append(relevant_word[0])
        final_sentence = ""
        log_file.write("Words with similar scores : "+str(similar_scores)+"\n")
        log_file.write("Relevant document associated : "+relevant_document+"\n")
        for elem in similar_scores:
            log_file.write("Now looking for speeches sentences containing "+elem+";\n")
            for i in range(0, len(speech_lines)):
                if elem in speech_lines[i]:
                    log_file.write("Sentence found ["+speech_lines[i]+"]\n")
                    final_sentence += " "+speech_lines[i]
        if final_sentence != "":
            log_file.write("Final sentence obtained : "+final_sentence+"\n")
        else:
            # This specific condition is when a paradox between the most relevant document and the most relevant word
            # in the question, that isn't contained in the most relevant document to respond to the question occurs.
            # More details will be detailed in the report.
            log_file.write("Paradox question found : question "+str(question_matrix)+" has the highest similarity to a "
                                                                                     "document that doesn't contain "
                                                                                     "the words with its highest "
                                                                                     "TF-IDF !\n")
        log_file.write("------- [ANSWER GENERATED {} ] -------\n\n\n".format(datetime.now()))
        return final_sentence
