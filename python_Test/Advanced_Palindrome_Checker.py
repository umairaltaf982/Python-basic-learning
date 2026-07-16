# Exercise 17 - Advanced Palindrome Checker

# Write a version of a palindrome recognizer that also accepts phrase palindromes
# such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
# "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored.

def advanced_palindrome(sentence):
    a_sentence = sentence.lower()
    b_sentence = a_sentence.replace(" ", "")
    c_sentence = b_sentence.replace("'", "")
    d_sentence = c_sentence.replace(",", "")
    new_sentence = d_sentence.replace(".", "")


    reversed_text = ""
    for char in new_sentence:
        reversed_text = char + reversed_text
    if new_sentence == reversed_text:
        return True
    else:
        return False

x = advanced_palindrome("Go hang a salami I'm a lasagna hog.")
y = advanced_palindrome("I roamed under it as a tired nude Maori")
z = advanced_palindrome("Hello I'm Umair.")
print(x)
print(y)
print(z)
