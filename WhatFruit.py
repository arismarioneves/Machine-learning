from sklearn import tree

lisa = 0
irregular = 1

maca = 0
laranja = 1

arvore = [[130, lisa], [150, lisa], [160, irregular], [180, irregular]]

resultado = [maca, maca, laranja, laranja]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(arvore, resultado)

peso = int(input("Informe o peso da Fruta: "))
superficie = int(input("Informe a superficie [Lisa - 0] [Irregular - 1]: "))

resultado = clf.predict([[peso, superficie]])

if resultado == 0:
    print("É uma Maça")
else:
    print("É uma Laranja")
