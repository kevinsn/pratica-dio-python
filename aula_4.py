# FOR, aceita dois parâmetros
# 1 param = do zero até o parm - 1
# 2 params = primeiro parm até o segundo parm - 1

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range (1, a + 1):
#     resto = a % x
#     print (a, resto)
#     if resto == 0:
#         div = div + 1
#
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))

# Código abaixo para números primos até tal valor
# a = int(input('Insira um número para verificar se é primo: '))
# for num in range(a + 1):
#     div = 0
#     for x in range (1, num + 1):
#         resto = num % x
#         # print (num, resto)
#         if resto == 0:
#             div = div + 1
#
#     if div == 2:
#         print(num)

# While
# a = 0
# while a <= 10:
#     print(a)
#     a += 1
# # Código de boletim com uso de while
# nota = int(input('Digite a primeira nota: '))
# while nota > 10 or nota < 0:
#     nota = int(input('Digite uma nota entre 0 e 10: '))
#
# print(nota)

a = int(input('Primeiro bimestre: '))
while a > 10 or a < 0:
      a = int(input('Você digitou errado. 1º bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10 or a < 0:
      b = int(input('Você digitou errado. 2º bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10 or a < 0:
      c = int(input('Você digitou errado. 3º bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10 or a < 0:
      d = int(input('Você digitou errado. 4º bimestre: '))
media = (a + b + c + d)/4

print(media)
