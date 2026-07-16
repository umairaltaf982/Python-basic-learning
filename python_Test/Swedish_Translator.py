# Exercise 20 - Swedish Translator

# Represent a small bilingual lexicon as a Python dictionary in the following fashion
# "{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}"
# and use it to translate your Christmas cards from English into Swedish.
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

def translate(my_list):
    new_list = []
    dictionary = {
        "happy": "nich",
        "birthday": "burdeyy",
        "and": "och",
        "Good": "gott",
        "new": "nytt",
        "year": "år"
    }
    for l in my_list:
        for key, value in dictionary.items():
            if key == l:
                new_list.append(value)

    return new_list

x = translate(["happy", "birthday", "Bhai", "year"])
print(x)