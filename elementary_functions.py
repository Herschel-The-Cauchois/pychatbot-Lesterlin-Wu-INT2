import os
from datetime import datetime


def list_of_files(directory, extension):
    """Function collecting in a list all the names of the file in a directory with a specific extension specified
    in the second parameter. Taken from the project PDF."""
    files_names = []
    for filename in os.listdir(
            directory):  # Loop that will, for each file located in specified directory collect the name of the file
        # if it has specified extension.
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def name_extractor(files_mentioned: list):
    """This function extract the names of the president according to the file names retrieved in a list, usually by
    the function list_of_files, to turn it into a set containing all of their names."""
    treatment = []
    treated = []  # Creating the two necessary lists for processing
    for elem in treatment:
        for elem in files_mentioned:  # Starts by cutting in two the name of the president contained in the file
            # name, separating them by an underscore.
            name_breaker = elem.split("_")
            name_breaker[1] = name_breaker[1][:-4]  # Then removes the file extension from the name
            treatment.append(
                name_breaker[1])  # Stores what's remaining of the last name to the first temporary storage list
        if elem[-1:] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            treated.append(elem[
                           :-1])  # Removes any iteration number in the file names still attached to the obtained
            # data before appending to the treated list.
        else:
            treated.append(elem)  # If there's no such thing, directly appends it.
    return set(treated)  # Converts the treated list into a set to remove duplicates.


def president_fullname(name_list: set):
    """This functions creates the list of each Vth Republic president's full name by associating the last name
    obtained in the name_extractor function to its first name via a dictionary."""
    output = []
    first_names = {"Mitterrand": "Francois", "DeGaulle": "Charles", "Giscard dEstaing": "Valery", "Chirac": "Jacques",
                   "Sarkozy": "Nicolas", "Macron": "Emmanuel", "Hollande": "Francois",
                   "Pompidou": "Georges"}  # Said dictionary with first names.
    for elem in name_list:
        output.append(
            first_names[elem] + " " + elem)  # puts in the output list each first name + last name combination.
    return output


def file_cleaner(file_path: str):
    """This 2-in-one function proceeds to pre-process the speeches file to convert uppercase letters to lower case,
    and remove any punctuation to leave only the words and spaces separator that we will use later in the project."""
    print(
        "Now doing " + file_path)  # For each file processed specified in the parameter, it will print in the console
    # the file being processed.
    file = open(file_path, "r",
                encoding="utf-8")  # Opens in reading mode the file to be processed, to avoid tampering with the
    # starting data.
    cleaned_file = open("./cleaned/" + file_path.split("/")[len(file_path.split("/")) - 1][:-4] + "_cleaned.txt",
                        "a")  # Creates a new file, that will host the cleaned content.
    file_lines = file.readlines()  # Reads all the lines of the file that will be processed.
    for elem in file_lines:
        ascii_temp = []  # List that will contain every caracter of the line being processed, added in the next loop.
        for i in range(0, len(elem)):
            ascii_temp.append(elem[i])
        i = 0
        while i < len(
                ascii_temp):  # Due to the deleting process modifying the lenght of the list, a while loop is more
            # appropriate to use since it adapts to the new lenght of the list each time an element is deleted.
            if 64 < ord(ascii_temp[
                            i]) < 91:  # This condition uses ascii table conversion to convert uppercase letter to
                # lowercase by using a mathematical relationship to their respective ID in the table.
                ascii_temp[i] = chr(ord(ascii_temp[i]) + 32)
                i += 1
            elif ascii_temp[i] == "," or ascii_temp[i] == "." or ascii_temp[i] == "\"" or ascii_temp[
                i] == "_":  # If it detects any underscore, quote-marks, dots or comma, it will directly remove them.
                del ascii_temp[i]
            elif ascii_temp[i] == "!" or ascii_temp[i] == "?" or ascii_temp[i] == ":" or ascii_temp[
                i] == ";":  # For any question marks, colons, semi-colons, and exclamation point, it will remove the
                # caracter itself then the space after to avoid double spaces at the maximum.
                del ascii_temp[i]
                del ascii_temp[i]
                i += 1
            elif ascii_temp[i] == "\n" or (ascii_temp[i] == "-" and not (ascii_temp[i + 1] == " ")) or ascii_temp[
                i] == "'":  # If it detects any apostrophe, new line character or dash not followed by a space,
                # it replaces it with a space.
                ascii_temp[i] = " "
            elif ascii_temp[
                i] == "-" and i == 0:  # This is a condition specific to the formatting of the chirac speeches. It
                # removes the starting dash and the space after without creating out of range related problems.
                del ascii_temp[i]
                del ascii_temp[i]
            elif ascii_temp[i][
                0] == "\x9c":  # This is a condition specific to the Hollande speeches. An unknown unicode character
                # was inside replacing the oe one, so the oe was manually added and the character removed by this code.
                del ascii_temp[i]
            else:
                i += 1  # If no such treatment is needed, goes directly to the next character.
        i = 0
        while i < len(
                ascii_temp):  # The loop is repeated here as a failsafe, since it happened that remaining punctuation
            # or non-wanted caracters stayed despite the cleaning.
            if 64 < ord(ascii_temp[i]) < 91:
                ascii_temp[i] = chr(ord(ascii_temp[i]) + 32)
                i += 1
            elif ascii_temp[i] == "," or ascii_temp[i] == "." or ascii_temp[i] == "\"" or ascii_temp[i] == "_":
                del ascii_temp[i]
            elif ascii_temp[i] == "!" or ascii_temp[i] == "?" or ascii_temp[i] == ":" or ascii_temp[i] == ";":
                del ascii_temp[i]
                del ascii_temp[i]
                i += 1
            elif ascii_temp[i] == "\n" or (ascii_temp[i] == "-" and not (ascii_temp[i + 1] == " ")) or ascii_temp[
                i] == "'":
                ascii_temp[i] = " "
            elif ascii_temp[i] == "-" and ascii_temp[i + 1] == " ":
                del ascii_temp[i]
                del ascii_temp[i]
            elif ascii_temp[i][0] == "\x9c":
                del ascii_temp[i]
            else:
                i += 1
        cleaned_file.write("".join(
            ascii_temp))  # After the treatment of all the caracters of the line, the line is then written in the
        # cleaned file right next to the precedent one.
    file.close()
    cleaned_file.close()  # Once done, closes the files.


def file_check(file_path: str):
    """This is a supplementary function destined more to testing. It creates then fills a log with all the remarks
    regarding processing errors in the produced cleaned files."""
    error_info = [0, 0, 0]  # This is an error-counter list.
    f = open(file_path, "r")
    log = open("cleaner_log.txt", "a")  # Opens a cleaned file, and creates or append to a specified log file.
    log.write("------- [START {} : {}] -------\n".format(datetime.now(), file_path))  # Incipit in the log file.
    checking = f.readlines()
    for elem in checking:  # Directly takes the strings of each line and check each caracters before, if there is any
        # error found, writing it in the log file.
        for i in range(0, len(elem)):
            if elem[i] in ";!?-,.:_\'\"\n":
                log.write("Punctuation remaining in " + file_path + " in spot " + elem[i - 10:i + 10] + "\n")
                error_info[0] += 1
            if elem[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                log.write("Uppercase letter remaining in " + file_path + " in spot " + elem[i - 10:i + 10] + "\n")
                error_info[1] += 1
            if i != len(elem) - 1:
                if elem[i] == " " and elem[i + 1] == " ":
                    log.write("Double space detected in " + file_path + " in spot " + elem[i - 10:i + 10] + "\n")
                    error_info[2] += 1
    log.write("List of detected errors, read [Punctuation errors, Uppercase errors, Space errors] : " + str(
        error_info) + "\n")  # Writes in the log file the conclusion of the checking.
    log.write("------- [END {}] -------\n\n".format(datetime.now()))  # After processing, ends the part of the log
    # file with the date and time of processing end.
    log.close()
    f.close()
