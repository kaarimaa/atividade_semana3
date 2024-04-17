idade_minima_brasil= 18
idade_minima_eua= 16

entrada=input("Olá! Vamos te ajudar a alugar um carro nos Estados Unidos. Digite os campos abaixo e veja se está apta (o):")
print(entrada)

ano_de_nascimento=int(input(("Insira seu ano de nascimento aqui: ")))
if ano_de_nascimento <=2007 :
    print("Parabéns! 🎉 Siga com o aluguel do seu carro nos nossos canais de atendimento.")
else:
    print("Poxa 😞 Você ainda não pode alugar seu carro conosco, pois não tem idade mínima para dirigir aqui no Brasil. Você precisa ter a CNH brasileira para conseguir dirigir no EUA. Nos vemos na próxima!")