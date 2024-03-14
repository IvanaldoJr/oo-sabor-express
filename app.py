from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('melancia', 5.00, 'grande')
prato_paozinho = Prato('Pãoziho', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)



def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()