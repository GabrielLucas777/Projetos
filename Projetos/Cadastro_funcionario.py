# Cadastro funcionario
# funcionalidades
from datetime import datetime

import random

nome_funcionario = input('Insira seu nome: ')

idade = int(input('Insira sua idade: '))

registro = datetime.now()


conclusao = print("Seu registro foi concluido com sucesso ás:",
                  registro)

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']

sorteio = (random.choice(cartoes))

data_aniversario = datetime.strptime(
    input('Qual a data do seu aniversário?: '), '%d/%m/%Y')
print(type(data_aniversario))


# funcionalidade 2

print('Olá,', nome_funcionario, 'Seu registro foi concluido com sucesso ás:', registro.day, '/', registro.month,
      '/', registro.year, '\n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de', sorteio)
