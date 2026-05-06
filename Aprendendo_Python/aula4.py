# idade = 17

# if idade >= 18:
#     print("Pode tirar a carteira de motorista")

# elif idade >= 16:
#     print("Pode tirar, com comprovação dos responsaveis")

# else: 
#     print("Não pode tirar a carteira de motorista")

######################################################################

# a = 5
# b = 5

# if a > b:
#     print("A é maior que B")
# elif a < b:
#     print("A é menor que B")
# else:
#     print("A é igual a B")

######################################################################

# media = float(input("Digite sua media: "))

# if media >= 7: 
#     print("Aprovado")
# elif media >= 5:
#     print("Recuperação")
# else:
#     print("Reprovado")

######################################################################

# dia = int(input("Digite um número: "))

# if dia == 1:
#     print("É Domingo")

# elif dia == 2:
#      print("É Segunda")

# elif dia == 3:
#      print("É Terça")

# elif dia == 4:
#      print("É Quarta")

# elif dia == 5:
#      print("É Quinta")

######################################################################
# DESAFIO

gasto = float(input ("Quanto você gastou? "))

if gasto >= 100:
    desconto = gasto - 10
    print (f"Você ganhou 10 reais de desconto, sua compra agora custa {desconto}")
    
elif gasto < 100: 
    print (f"Chegue em 100 e ganhe 10 reais de desconto")
