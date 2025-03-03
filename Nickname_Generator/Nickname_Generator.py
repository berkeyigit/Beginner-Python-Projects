import random

print("Kullanici adiniz icin istediginiz kelimeleri giriniz. Cikmak icin ise 'Q' tusuna basiniz")
words = []
while True:
    word = input("Kullanici adiniz:").capitalize()
    if word.upper() == "Q":
        break
    words.append(word)

print("Kelimeleriniz : ", words)

wordlengt = int(input("Kullanici adinizin kac kelime barindirmasini istediginizi giriniz."))

nickname = ""
for _ in range(wordlengt):
    choisewords = random.choice(words)
    words.remove(choisewords)
    nickname += choisewords

print("Kullanici adiniz : ", nickname)