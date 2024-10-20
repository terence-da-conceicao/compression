 # -*- coding: utf-8 -*-

dictionnaire = {
 'texte': '1',
 'lorem': '2',
 'qui': '3',
 'donc': '4',
 'est': '5',
 'que': '6',
 'pour': '7',
 'ceci': '8',
 'faux-texte': '9',
 'dans': '10',
 'plus': '11',
 'avec': '12',
 'un': '13',
 'pas':'14',
 'le': '15',
 'on': '16',
 'la': '17',
 'en': '18',
 'une': '19',
 'et': '20',
 'il': '21',
 'ce': '22',
 'au': '24',
 'a': '25',
 'à': '26',
 'de': '27',
 'des': '28'
 }

loremIpsum = "généralement, on utilise un texte en faux latin ( le texte ne veut rien dire, il a été modifié ), le lorem ipsum ou lipsum, qui permet donc de faire office de texte d'attente. l'avantage de le mettre en latin est que l'opérateur sait au premier coup d'oeil que la page contenant ces lignes n'est pas valide, et surtout l'attention du client n'est pas dérangée par le contenu, il demeure concentré seulement jamais dans le faux-texte"


#//COMPRESSION

def split(texte):
    return texte.split()

def wordToInt(liste, dico):
    for i in range(len(liste)):
        if liste[i] in dico:
            liste[i] = dico[liste[i]]
    return liste

def build(liste):
    return " ".join(liste)
    

def compression(texte, dico):
    newList = split(texte)
    newSwitched = wordToInt(newList, dico)
    compText = build(newSwitched)
    return compText

compLorem = compression(loremIpsum, dictionnaire)



#//DECOMPRESSION

def intToWord(liste, dico):
    newDico = {v:k for k,v in dico.items()}
    for i in range(len(liste)):
        if liste[i] in newDico:
            liste[i] = newDico[liste[i]]
    return liste


def decompression(texte, dico) : 
    newliste = split(texte)
    newSwitched = intToWord(newliste, dico)
    decompText = build(newSwitched)
    return decompText

decompLorem = decompression(compLorem, dictionnaire)

#OU BIEN

def intToWord2(liste, dico):
    for key, value in dico.items():
        for i in range(len(liste)):
            if value == liste[i]:
                liste[i] = key
    return liste

def decompression2(texte,dico):
    newliste = split(texte)
    newSwitched = intToWord2(newliste, dico)
    decompText = build(newSwitched)
    return decompText

decompLorem2 = decompression2(compLorem, dictionnaire)


def createDictionnary(liste):
    dictionnaire = {}
    for i in range(len(liste)):
        dictionnaire[liste[i]] = liste.count(liste[i])
    return dictionnaire

listeLorem = split(loremIpsum)
dict = createDictionnary(listeLorem)

#Si le mot fait plus de 3 caractères et apparait au moins 2 fois
def conditionReplace(liste):
    dictionnaire = createDictionnary(liste)
    for i in range(len(liste)):
        if len(liste[i]) > 3 and liste.count(liste[i]) > 2 :
            liste[i] = dictionnaire[liste[i]]
    return liste



#avec un dictionnaire de référence de nombre d'apparitions des mots

dictNbMots = createDictionnary(listeLorem)


def conditionReplace2(liste, dico):
    for i in range(len(liste)):
        if liste[i] in dico:
            #print("liste i = ",liste[i])
            liste[i] = str(dico[liste[i]])
            #print("dico i = ",dico[liste[i]])
        else : 
            print("nope")
    
    return liste

complisteLorem = conditionReplace2(listeLorem, dictNbMots)
print(complisteLorem)

