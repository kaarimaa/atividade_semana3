preco_produto0052= 50
preco_produto0054= 30

entrada=input("Bem vinda (o) a Farmácia Popular!")
print(entrada)
codigo_produto1= input(("Coloque o código do seu 1º produto aqui: "))
codigo_produto2= input(("Coloque o código do seu 2º produto aqui: "))
if codigo_produto1 == codigo_produto2 :
    print("Parabéns! Você ganhou 5 reais de desconto \U0001F60A")
    int(preco_produto0052 + preco_produto0054 - 5)
    print("O valor total do seu pedido é de R$75,00 🎉")
elif codigo_produto1 == str("0052") and codigo_produto2 == str("0054"):
    print("Você ganhou 50% de desconto!!! 🎉")
    print("O valor total do seu pedido é de R$40,00!!!")
else:
    print("Código inválido :( ")
    print("Fim do programa")
