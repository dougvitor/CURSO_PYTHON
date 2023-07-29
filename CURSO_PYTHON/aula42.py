# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
senha = input('Senha: ')

if senha != '123':
    print('Senha não é válida')


print(not True)  # False
print(not False)  # True