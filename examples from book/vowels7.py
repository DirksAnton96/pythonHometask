vowels = set('a,e,i,o,u')
#word = "Milliways"
word = input("Provide a word tto search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
#print(found)