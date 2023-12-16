# **PyChatBot v0.2**


*Created by :*
- *LESTERLIN Raphaël L1 INT2 - alias __<u>Hershel_TC</u>__*
- *WU Julien L1 INT2 - alias __<u>Number6272</u>__*

[Git repository](    https://github.com/Herschel-The-Cauchois/pychatbot-Lesterlin-Wu-INT2)

## **Setup instructions**


Download the release as a zip file containing all the code, and extract it to the desired folder.
Do NOT tamper with the structure of folders and files once extracted or their names, which would break the program. Tampering with the speeches .txt file with non-unicode characters may also hinder the bot's capacities.

Once done, launch the program by running __<u>main.py</u>__ in any python console interpreter. You may now interact with the program :)

[Python Download](https://python/org/downloads/)

## **App description**

This ChatBot consists of two separate parts. It bases any of its answers on the investiture speeches of the last 6 French presidents.

First, it will be able to review the given corpus and give 6 different results :

- Least important words;
- Words with the highest TF-IDF score (the rarest);
- The most repeated words by president Chirac;
- Names of president who mentions the word nation, and the president who mentions it the most;
- The first president talking about climate in his speech;
- Words which all president mentioned in their speeches.

Secondly, it will be able to take into input any user question (*NB: In French*) and generate an appropriate answer based on the given corpus. Let your imagination be wild !

Mind before each new input that there is a 5s~ cooldown before each command to allow you to read the answer of the bot, be patient !

## **List of the different files**

- main.py : the main program;
- elementary_functions.py (log for the file cleaner : cleaner_log.txt) : the main text and file processing functions that helps the program treating the corpus;
- tf_idf.py (log : tf_idf_log.txt) : the program that converts the text into a TF-IDF matrix, that allows it to be machine-processed;
- application_functions.py : functions that will give you the statistics and trivia of the first part;
- q_tokenization.py : functions processing the questions of the user;
- q_answer.py (log : generation_log.py) : functions that allow the bot to generate a user-friendly answer !

The speeches folder contains the original corpus made for this bot, and the cleaned folder the pre-processed version of them.

Enjoy the program :)