# Vamos resolver o desafio seguindo um passo a passo.
# Nesse estudo de caso, desenvolveremos um programa em Python para calcular
# o valor final de uma compra com desconto. A principal competência é a
# aplicação do pensamento lógico para construir um programa funcional,
# que ajude os vendedores a calcularem o preço final.


def get_price_input():
    price = 0
    while True:
        try:
            print('Digite o preço do produto (Máximo: DUAS casas decimais).')
            price = float(input('Preço: '))

            if price == round(price, 2):  # if len(valor.split('.')[-1]) == 2:
                break
            else:
                print(f'"{price}" não se adequa em duas casas decimais.')

        except ValueError:
            print(f'O valor "{price}" é inválido! Insira novamente.')
    return price


def get_discount_input():
    discount = 0

    print('Use "ponto" para os valores decimais')

    while True:
        try:
            print('Digite o valor do desconto em porcentagem, apenas o valor:')
            discount = float(input('Desconto: '))
            break
        except ValueError:
            print(f'O valor {discount} não se adequa a porcentagem! Reinsira.')

    return discount


def calc_discount(price, discount):
    return price - (price * discount/100)


def main_function():
    price = get_price_input()
    discount = get_discount_input()
    discounted_price = calc_discount(price, discount)

    print(f'Produto de $"{price}", com desconto de "{discount}%"')
    print(f'Passa a ser de {discounted_price}')


main_function()
