
def word_frequency(text):

    text = text.lower()
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
    words = text.split()

    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    sorted_frequency = dict(sorted(frequency_dict.items(), key = lambda item : item[1], reverse=True))
    return sorted_frequency


input_text = input("Bir Metin giriniz:")

result = word_frequency(input_text)

print("\n Kelime frekanslari : ")
for word, frequency in result.items():
    print(f"'{word}' : {frequency} kez")
