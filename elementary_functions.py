import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def name_extractor(files_mentioned: list):
    treatment = []
    treated = []
    for elem in files_mentioned:
        name_breaker = elem.split("_")
        name_breaker[1] = name_breaker[1][:-4]
        treatment.append(name_breaker[1])
    for elem in treatment:
        if elem[-1:] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            treated.append(elem[:-1])
        else:
            treated.append(elem)
    return set(treated)


def president_fullname(name_list: set):
    output = []
    first_names = {"Mitterrand": "Francois", "DeGaulle": "Charles", "Giscard dEstaing": "Valery", "Chirac": "Jacques",
                   "Sarkozy": "Nicolas", "Macron": "Emmanuel", "Hollande": "Francois", "Pompidou": "Georges"}
    for elem in name_list:
        output.append(first_names[elem] + " " + elem)
    return output


def file_cleaner(file_path: str):
    print("Now doing "+file_path)
    file = open(file_path, "r", encoding="utf-8")
    cleaned_file = open("./cleaned/" + file_path.split("/")[len(file_path.split("/")) - 1][:-4] + "_cleaned.txt",
                        "a")
    file_lines = file.readlines()
    for elem in file_lines:
        ascii_temp = []
        for i in range(0, len(elem)):
            ascii_temp.append(elem[i])
        i = 0
        while i < len(ascii_temp):
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
            elif ascii_temp[i] == "-" and i == 0:
                del ascii_temp[i]
                del ascii_temp[i]
            elif ascii_temp[i][0] == "\x9c":
                del ascii_temp[i]
            else:
                i += 1
        i = 0
        while i < len(ascii_temp):
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
        cleaned_file.write("".join(ascii_temp))
    file.close()
    cleaned_file.close()


# reste à faire : traitement tirets, apostrophes (attention discours chirac avec tiret de dialogue), tout commenter,
# bonus ajouter assertions

def file_check(file_path: str):
    error_info = [0,0,0]
    f = open(file_path, "r")
    checking = f.readlines()
    for elem in checking:
        for i in range(0, len(elem)):
            if elem[i] in ";!?-,.:_\'\"\n":
                print("Punctuation remaining in " + file_path + " in spot "+elem[i-10:i+10])
                error_info[0] += 1
            if elem[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                print("Uppercase letter remaining in " + file_path + " in spot "+elem[i-10:i+10])
                error_info[1] += 1
            if i != len(elem) - 1:
                if elem[i] == " " and elem[i + 1] == " ":
                    print("Double space detected in " + file_path + " in spot "+elem[i-10:i+10])
                    error_info[2] += 1
    f.close()


list1 = list_of_files("./speeches", ".txt")
for elem in list1:
    file_cleaner("./speeches/" + elem)
for elem in list_of_files("./cleaned", ".txt"):
    file_check("./cleaned/" + elem)
