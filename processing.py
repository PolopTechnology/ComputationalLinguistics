import random as r
import language as L

f = open("dataset.txt", "r")
x = f.read()
y = x.split()
nlp = []

for z in y:
    nlp.append(z.lower())

nlp.sort()


txt = "Gojo is awesome"
txtTag = []
txt = txt.split()
for i in txt:
    activatedWord = False
    for a in L.y:
        if a == i:
            txtTag.append("PREPOSITION")
            activatedWord = True
    for b in L.y2:
        if b == i:
            txtTag.append("NOUN")
            activatedWord = True
    for c in L.y3:
        if c == i:
            txtTag.append("VERB")
            activatedWord = True
    for d in L.y4:
        if d == i:
            txtTag.append("ADJECTIVE")
            activatedWord = True
    for d in L.y5:
        if d == i:
            txtTag.append("CONJUNCTION")
            activatedWord = True
    for d in L.y6:
        if d == i:
            txtTag.append("DETERMINER")
            activatedWord = True
    for d in L.y7:
        if d == i:
            txtTag.append("PRONOUN")
            activatedWord = True

    if activatedWord == False:
        txtTag.append("NOUN")
    
print(txt)
print(L.construction(txtTag))
print(len(nlp))