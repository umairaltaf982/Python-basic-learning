# Exercise 18 - Pangram

# A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it is a pangram or not.


def pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence_lower = sentence.lower()

    for char in alphabet:
        if char not in sentence_lower:
            return "This sentence/word is not pangram"
    return "This sentence/word is pangram"

x = pangram("The quick brown fox jumps over the lazy dog.")
print(x)
y = pangram("Hello World")
print(y)