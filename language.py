#1
f = open("prepositions.txt", "r")
x = f.read()
y = x.splitlines()
#2
f2 = open("nouns.txt", "r")
x2 = f2.read()
y2 = x2.split()
#3
f3 = open("verb.txt", "r")
x3 = f3.read()
y3 = x3.split()
#4
f4 = open("adjectives.txt", "r")
x4 = f4.read()
y4 = x4.split()
#5
f5 = open("conjunctions.txt", "r")
x5 = f5.read()
y5 = x5.splitlines()
#6
f6 = open("determiners.txt", "r")
x6 = f6.read()
y6 = x6.splitlines()
#7
f7 = open("pronouns.txt", "r")
x7 = f7.read()
y7 = x7.splitlines()


def parseTree(txtTag):
    verbPhrase = 0
    sliced = False
    for i in range(len(txtTag)):
        if txtTag[i] == "VERB" and sliced == False:
            verbPhrase = i
            sliced = True
    return txtTag[0:verbPhrase], txtTag[verbPhrase:]

def parseTree2(nounPhrase, verbPhrase):
    propositionalPhrase = 0
    sliced = False
    for i in range(len(verbPhrase)):
        if verbPhrase[i] == "PREPOSITION" and sliced == False:
            propositionalPhrase = i
            sliced = True
    return nounPhrase, verbPhrase[0:propositionalPhrase], verbPhrase[propositionalPhrase:]

def construction(tag):
    h1, h2 = parseTree(tag)
    return parseTree2(h1, h2)