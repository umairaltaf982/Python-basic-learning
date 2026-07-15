# Exercise 5 - Swedish Robber Translator
# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between.
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(sentence):
    y = ""
    for s in sentence:
        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u' or s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U' or s == ' ':
            x = s
            y = y + x
        else :
            x = s.replace(f"{s}", f"{s}o{s}")
            y = y + x
    print(y)

translate("this is fun")