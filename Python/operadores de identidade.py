# Verifica se os objetos ocupam o mesmo espaço na memória

curso = "Curso de Python"
nome_curso = curso
saldo,limite = 200,200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)

saldo = 1000
limite = 1000
print()
print(saldo is limite)
print(saldo is not limite)

a = [1,2,3]
b = [1,2,3]

print("a b:",a is b)