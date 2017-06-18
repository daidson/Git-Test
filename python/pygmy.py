""" this is my first program using python
    as since, it should not be considered
    to any work or distribution devices
    because it can also be found online 
    in many different platforms. for more
    information about this game, just go
    and search for 'Pig Latin Translator'

    this is just a study practice.

    Yours, truly,

    Daidson F. Alves                   """


#the program starts here

#variables to add 'ay' to the word

pyg = 'ay'

#program asks for a word

raw_input = input

original = raw_input('Enter a word: ')

#statements to get the word

if len(original) > 0 and original.isalpha():
    word = original.lower
    first = word[0]
    print (original)
else:
    print ('Where is your word?')

#this now prints the new word (word + first letter + 'ay')

new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

print (new_word)

#end of the program
