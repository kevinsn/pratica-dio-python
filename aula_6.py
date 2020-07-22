#-------------------CONJUNTO-------------------
# tipo é set
# conjunto = {1, 2, 3, 4}
# print(type(conjunto))
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

# Union, intersection e difference
# conjunto = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
# conjunto_uniao = conjunto.union(conjunto2)
# print(conjunto_uniao)
# conjunto_interseccao = conjunto.intersection(conjunto2)
# print(conjunto_interseccao)
# conjunto_diferenca1 = conjunto.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto1)
# print(conjunto_diferenca1)
# print(conjunto_diferenca2)
# Diferença simétrica:
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# print(conjunto_diff_simetrica)

# Subset (se o conjunto a está presente em b)
# E Superset (se o conjunto b possui o conjunto a)
# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4 ,5}
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print(conjunto_subset)
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print(conjunto_superset)

# Transformando lista em conjunto e vice versa, retira duplicidade
# listaDuplicada = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
# print(listaDuplicada)
# conjunto_animais = set(listaDuplicada)
# print(conjunto_animais)
# lista_animais = list(conjunto_animais)
# print(lista_animais)