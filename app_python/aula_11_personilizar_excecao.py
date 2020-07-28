class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com um número entre 0 a 10 '))
        print(x)
        if x > 10:
            raise InputError('Número não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Digite um número')
    except InputError as ex:
        print(ex)