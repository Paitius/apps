letters = []
alphabet = {}
z = 0

for i in range(97, 123):
    letters.append(chr(int(i)))

for i in letters:
    z += 1
    alphabet[i] = [int(z)]


def scoring_sum(words):
    scoring = 0
    for i in words:
        z = alphabet.get(i)
        scoring += int(z[0])
    return scoring


def high(x):
    words = x.split()
    scoring_words = {}
    for i in words:
        scoring_words[i] = scoring_sum(i)
        temp = max(scoring_words.values())
        res = []
        for key, value in scoring_words.items():
            if (value == temp):
                res.append(key)
    return print(res[0])
    # strongest = dict(sorted(scoring_words.items(), key=lambda item: item[1], reverse= True))
    # return list(strongest.items())[0][0]


high("man i need a taxi up to ubud")
high("what time are we climbing up the volcano")
high("take me to semynak")
high("aa b")
high("b a c")
