with open('text_.txt', mode='r') as f:
    data = f.read()


punctuations = '.«»!"—#$%&()*+,-./:;<=>?@[\]^_`{|}~'
for i in range(len(punctuations)):
    data = data.replace(punctuations[i], ' ')

data = data.lower()
words = data.split()


dict_wods = {}
for i in range(len(words)):
    dict_wods[words[i]] = words.count(words[i])

d = list(dict_wods.items())
d.sort(key=lambda x: x[1], reverse=True)
print(d)

for word, amount in d[:5]:
    print(word, '--', amount)

print(len(d))