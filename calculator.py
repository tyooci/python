from pyautogui import hotkey
from time import sleep


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1**n2


def raiz(n1, n2):
    return n1**(1/n2)


def expression(formula, x):
    x = float(x)
    return eval(formula)


def clear():  # Clear console em minhas configurações (PyCharm) = ctrl + shift + s
    """
    Limpa a tela
    """
    print('Aguarde um momento...')
    sleep(5)
    hotkey('ctrl', 'shift', 's')


def restart_clear():
    """
    Interrompe o laço, limpa a tela e chama a função calculator() novamente -> Recomeça o código.
    Esse método se chama recursão.

    """
    restart_calc = True
    clear()
    calculator()


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    'raiz': raiz,
}


def calculator():  # Main
    print('===CALCULADORA===\n\n')
    wants_expression = input('Digite "S" se desejas realizar um cálculo de expressão ou "N" para prosseguir para a '
                             'calculadora normal:\n > ').upper()
    while wants_expression == 'S':
        formula = input('Digite a expressão: ')

        x_value = input('Digite o valor de x (caso não houver, digite 0): ')
        if not x_value.isnumeric():
            print('Por favor, digite um valor para x válido.')
            restart_clear()

        operation_value = expression(formula, x_value)
        print(f'\n{formula} = {operation_value}')

        # Muda a condição de while
        wants_expression = input('\nDigite "N" se desejas iniciar a calculadora normal ou "S" se desejas continuar '
                                 'realizando expressões:\n > ').upper()

        clear() if wants_expression == 'N' else None

    # O primeiro número encontra-se fora do laço a seguir, pois a ideia é que ele seja acessado uma outra vez apenas se
    # o usuário escolher reiniciar a calculadora posteriormente
    num1 = input('\nDigite um número:\n > ')

    restart_calc = False
    while not restart_calc:
        print('')

        for operation in operations:
            print(operation)

        print('\nINSTRUÇÃO: No caso da opção "raiz", digite 2 para raiz quadrada, 3 para cúbica (...)')

        user_operation = input('\nEscolha uma das operações acima:\n > ')

        # Checa se a operação escolhida é válida
        if user_operation not in operations:
            print('A operação escolhida é inválida. Tente novamente')
            restart_clear()

        num2 = input('Digite outro número:\n > ')

        # Checa no primeiro laço se as strings podem ser convertidas para float, para evitar erros
        if type(num1) == str and type(num2) == str:
            if not num1.isnumeric() or not num2.isnumeric():
                print('Um erro ocorreu. Verifique se digitou os números corretamente e tente novamente.')
                restart_clear()

        num1 = float(num1)
        num2 = float(num2)

        # Pega a função correspondente à operação escolhida no dicionário
        function = operations[user_operation]

        # Chama a função e atribui seu valor à uma variável
        operation_value = function(num1, num2)

        print(f'\n{num1} {user_operation} {num2} = {operation_value}')

        want_restart = input(f'\nDigite "S" se quiser continuar usando o valor {operation_value} ou "N" se quiser '
                             f'reiniciar a calculadora:\n > ').upper()
        if want_restart == 'S':

            # O primeiro número se torna o resultado, para que o mesmo possa ser reutilizado
            # que se trata da escolha do usuário
            num1 = operation_value
        else:
            restart_clear()


calculator()
