while True:
    nome = input("Qual o nome do Gasto? ")
    valor = input("qual é o valor? ")

    with open ("gastos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + ";" + valor + "\n")

    print("Gasto registrado!")

    outro = input("Deseja adicionar outro gasto? (s/n)" )
    if outro.lower() == "n" or outro == "Não":
        break
