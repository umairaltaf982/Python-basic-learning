# Exercise 24 - Third Person Transformer
#
# The third person singular verb form in English is distinguished by the suffix -s,
# which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
#
# If the verb ends in y, remove it and add ies
# If the verb ends in o, ch, s, sh, x or z, add es By default just add s
# Your task in this exercise is to define a function make_3sg_form() which given a verb in
# infinitive form returns its third person singular form. Test your function with words
# like try, brush, run and fix. Note however that the rules must be regarded as heuristic,
# in the sense that you must not expect them to work for all cases.
# Tip: Check out the string method endswith().

def make_3sg_form(word):
    size = len(word)
    count = 1
    new_word = ""
    if word.endswith('y') or word.endswith('o') or word.endswith('ch') or word.endswith('s') or word.endswith('sh') or word.endswith('x') or word.endswith('z'):
        for n in word:
            if count == size and n == 'y':
                new_word = new_word + "ies"
            elif count == size and n == 'o':
                new_word = new_word + "os"
            elif count == size and n == 'h':
                new_word = new_word + "hs"
            elif count == size and n == 's':
                new_word = new_word + "ss"
            elif count == size and n == 'x':
                new_word = new_word + "xs"
            elif count == size and n == 'z':
                new_word = new_word + "zs"
            else:
                new_word = new_word + n
            count = count + 1
        print(new_word)

make_3sg_form("honey")
make_3sg_form("church")

