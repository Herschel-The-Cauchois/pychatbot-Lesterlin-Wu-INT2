# Python Chatbot - LESTERLIN Raphaël and WU Julien - Generation and treatment of an answer to the user's question

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


def refine_answer(question: str, answer: str):
    """Function that takes a generated base answer and the question asked to determine an appropriate starter for
    the generated answer, then after processing appropriately the base answer merge the incipit and base answer
    to be returned and printed in the main program."""
    incipit = ""  # The starting of the answer is treated separately to avoid taking too many resources and time
    # for nothing.
    starters = {
        "peux-tu": "bien sûr !",
        "comment": "après réflexion,",
        "pourquoi": "car",
        "est-ce que": "d'après mon humble analyse,",
        "quand": "lorsque",
        "a qui": "a",
        "a quoi": "a",
        "qui": "le/la",
        "lequel": "le",
        "laquelle": "la",
        "où": "là",
        "combien": "il y a",
        "quel": "le",
        "quels": "les",
        "quelle": "la",
        "quelles": "les",
        "il y a": "il y a",
        "faut-il": "il faut",
        "qu'est ce qu": "c'est",
        "pour ou contre": "c'est compliqué,",
        "est-il": "oui et non",
        "est-elle": "oui et non",
    }  # This non-exhaustive dictionary collects the most common interrogative starters in French and
    # the appropriate answer starters.
    temp = ""
    for i in range(0, len(question)):
        # First, for more readability converts all uppercase characters of the question into lowercase.
        if 64 < ord(question[i]) < 91:
            temp += chr(ord(question[i]) + 32)
        else:
            temp += question[i]
    for key in starters.keys():
        # Proceed to generate the incipit by going through each key of the dictionary and adding an answer starter
        # in the future final incipit.
        if key in temp:
            if incipit[:-2] != "!":
                incipit += starters[key]+" "
            else:
                # since only one answer starter ends with an end of sentence mark, it is only in this case that the
                # added starter answer in this iteration of the incipit generation will have its first letter
                # turned into uppercase.
                incipit += chr(ord(starters[key][0]) - 32) + starters[key][1:] + " "
    if len(incipit) != 0:
        # If the incipit generated isn't empty, turns into uppercase the first letter of the answer starter.
        incipit = chr(ord(incipit[0]) - 32)+incipit[1:]
    else:
        # If the generated incipit is empty, proceeds to replace it by a default answer starter.
        incipit = "Eh bien, "
    temp = ""
    premiere_majuscule = 0
    for i in range(0, len(answer)):
        # Proceeds now to process the base answer.
        if 64 < ord(answer[i]) < 91 and premiere_majuscule == 0:
            # Since the added speeches line often starts with an uppercase letter, converts the first occurrence
            # of this case into lower case for better syntactical logic in the reply.
            temp += chr(ord(answer[i]) + 32)
            premiere_majuscule = 1
        elif answer[i] == "\n":
            # Removes new line characters in the base answer.
            temp += ""
        elif answer[i] in ",;:" and i == len(answer)-1:
            # Replaces final commas, colons and semicolons at the end of some speech lines by a dot.
            temp += "."
        else:
            temp += answer[i]
    if temp[len(temp)-1] in ";,:":
        # Reiterates the last procedure of the loop above.
        temp = temp[:-1] + "."
    final_answer = incipit + temp  # Finally, merges the answer starter and the treated base answer.
    return final_answer
