saldo = 1000
saque = 250
limite = 200

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)

# Operador de negação
contatos = []

print(not 1000 > 1500)

print(not contatos)

print(not 'saque 1500;')

print(not '')

# parêntenses
conta_especial = True

print('\n')
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

print(True or False)
print(True and False)