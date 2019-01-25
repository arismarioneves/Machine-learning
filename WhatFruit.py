#Created by Arismário Neves
#25/01/2019

from sklearn import tree

lisa = 1
irregular = 0

maca = 1
laranja = 0

arvore = [[150, lisa], [130, lisa], [180, irregular], [160, irregula]]

resultado = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(pomar, resultado)

peso = int(input("Informe o peso da Fruta: "))
superficie = int(input("Informe a superficie [Lisa - 1] [Irregular - 0]: "))

resultado = cl.predict([[peso, superficie]])

if resultado == 1:
    print("É uma Maça")
else:
    print("É uma Banaca")