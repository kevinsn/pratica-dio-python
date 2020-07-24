lista =[1, 10]
arquivo = open('teste.txt','r')

try:
    texto = arquivo.read()
    divisao = 10/0
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar a divisão')
except ZeroDivisionError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fecha arquivo')
    arquivo.close()


