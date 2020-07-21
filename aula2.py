a = int(input('Entre com o primeiro valor '))
b = int(input('Entre com o segundo valor '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


print('Soma: {som}.'
      '\nSubtração: {sub}.'
      '\nMultiplicação: {mul}.'
      '\nDivisão: {div}.'
      '\nResto: {res}.'
      .format(som = soma, sub = subtracao, mul = multiplicacao, div = divisao, res = resto))

print ()

# métodos do python str() retorna string, int() retorna um inteiro

'''print(type(soma))
print('Soma: {}. Subtração: {}'.format(soma,subtracao))
print('Soma: {som}. \nSubtração: {sub}'.format(som = soma, sub = subtracao))
soma = str(soma)
print(type(soma))
print("Soma é " + soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)'''