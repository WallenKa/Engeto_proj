"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karolína Wallenfelsová
email: wallenka@icloud.com
"""
def underscore():  # defines printing underscores as shown in the assignment
    print("-" * 40)

# load user usernames and passwords as a dictionary username : password
users_passwords = {"bob" : "123",
                  "ann" : "pass123",
                  "mike" : "password123",
                  "liz" : "pass123"}

# load given texts
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# inputs usernames
username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")
underscore()

# membership testing for inputed username and password
if username in users_passwords and password == users_passwords[username]:
    print("Welcome to the app,", username, "\nWe have 3 texts to be analyzed.")
    text_number_str = input("Enter a number between 1 and 3 to select: ")
    while text_number_str not in ["1", "2", "3"]:  # input new number until condition becomes False
        text_number_str = input("Wrong number, enter a number between 1 and 3 to select: ")
    underscore()
    text_number = int(text_number_str)  # turns string input into an integer
    text_id = text_number - 1  # creates an id of text from inputed number
    chosen_text = texts[text_id]  # choses text based on inputed id
    chosen_text_splited = chosen_text.split()  # splits text into list of words, sep. is white spaces
    number_of_words = len(chosen_text_splited)  # returns number of words
    # sets up variables for for cycle
    lowercase_words = int()
    uppercase_words = int()
    titlecase_words = int()
    numbers_counter = int()
    only_numbers = list()
    # counters for lower, upper and titlecase words and numbers
    for word in chosen_text_splited:
        if word.islower():
            lowercase_words = lowercase_words + 1
        elif word.isupper():
            uppercase_words = uppercase_words + 1
        elif word.istitle():
            titlecase_words = titlecase_words + 1
        elif word.isnumeric():
            numbers_counter = numbers_counter + 1
            only_numbers.append(int(word))
    sum_of_numbers = sum(only_numbers)  # sum of strings that are numeric
    # print counters
    print(f"There are {number_of_words} words in the selected text.")
    print(f"There are {titlecase_words} titlecase words.")
    print(f"There are {lowercase_words} lowercase words.")
    print(f"There are {uppercase_words} uppercase words.")
    print(f"There are {numbers_counter} numeric strings.")
    print(f"The sum of all the numbers is {sum_of_numbers}.")
    underscore()
    # sets up variables for later for cycle
    word_length = None
    length_frequencies = None
    word_length_all = {}
    # takes word length, tries to find it in a dict, if False, add to a dict with 0 value
    # if True, adds 1 to the value
    for word in chosen_text_splited:
        word_length = len(word)
        length_frequencies = chosen_text_splited.count(word_length)
        word_length_all[word_length] = word_length_all.get(word_length, 0) + 1
    print("LEN | OCCURENCES | NR.")  # print header for bar chart
    # print bar chart
    for word_length, length_frequencies in sorted(word_length_all.items()):
        bar_chart_stars = "*" * length_frequencies  # number of stars for each line
        bar_chart_white_spaces = " " * (12 - length_frequencies)  # number of white spaces for the chart
        print(f"{word_length} | {bar_chart_stars + bar_chart_white_spaces} | {length_frequencies}")
    underscore()
else:
    print("Unregistered user, terminating the program...")

