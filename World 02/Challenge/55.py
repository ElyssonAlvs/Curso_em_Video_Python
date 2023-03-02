"""
Programa leia o peso de cinco pessoas, no final mostra qual foi o maior
e o menor peso lido

Program reads the weight of five people, at the end it shows which one was the biggest
and the lowest read weight
"""
kg_upper = 0
kg_lower = 0
for i in range(1, 6):
    kg = float(input('Write a kg: '))
    if i == 1:
        kg_upper = kg
        kg_lower = kg
    else:
        if kg > kg_upper:
            kg_upper = kg
        if kg < kg_lower:
            kg_lower = kg
print(kg_upper)
print(kg_lower)
