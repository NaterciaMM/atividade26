# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 7.0

notalist = []
for x in range (5):
    nota= float(input(f"insira as notas{x}: "))
    notalist.append(nota)


maior = max(notalist)

menor = min(notalist)

media = sum(notalist) / len(notalist)

print(f"""
Maior nota - {maior}
Menor nota - {menor}
Media nota - {media}
""")