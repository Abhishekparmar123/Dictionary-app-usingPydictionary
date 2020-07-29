from PyDictionary import PyDictionary

dictionary = PyDictionary()

word = input("Enter A word : ")

meaning = dictionary.meaning(word)
antonyms = dictionary.antonym(word)

dic = meaning['Noun']
print("THE MEANING OF " + word.upper() + " :")
for i in dic:
    print("->>> " + i)
print(antonyms)