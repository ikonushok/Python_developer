with open('text_.txt', mode='r') as f:
    data = f.read()


punctuations = '.«»!"—#$%&()*+,-./:;<=>?@[\]^_`{|}~'
for i in range(len(punctuations)):
    data = data.replace(punctuations[i], ' ')

data = data.lower()
words = data.split()


## Лемматизация текста
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
lem = morph.parse(words[1])[0]
print(words[1], '===> ', lem.normal_form)

dict_words_lem = {}
for i in range(len(words)):
    lem = morph.parse(words[i])[0]
    dict_words_lem[lem.normal_form] = words.count(words[i])
#print(dict_words_lem)

# Продолжение из Light
d = list(dict_words_lem.items())
d.sort(key=lambda x: x[1], reverse=True)
print(d)

for word, amount in d[50:65]:
    print(word, '--', amount)

print(len(d))