# Entrada de dados (com restrições)

nome = str(input("Digite o seu nome: "))

destino = str(input("Digite o seu país de destino: "))

orçamento = float(input("Digite o orçamento disponível para a viagem em reais: "))
if orçamento < 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))

qtd_dias = int(input("Digite a duração da viagem em dias: "))
if qtd_dias <= 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))


passagem = float(input("Digite o valor da passagem aérea em reais: "))
if passagem < 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))

hospedagem_diária_EUR = float(input("Digite o custo diário de hospedagem em euros: "))
if hospedagem_diária_EUR < 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))

alimentação_diária_USD = float(input("Digite o custo diário de alimentação em dólares: "))
if alimentação_diária_USD < 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))

lazer_GBP = float(input("Digite o valor total reservado para lazer em libras esterlinas: "))
if lazer_GBP < 0:
    raise(ValueError("Ops, parece que você digitou um valor inválido! Digite um número positivo!"))

while True: 
    hospedagem = str(input("Informe o tipo de hospedagem (hotel ou hostel): "))
    if hospedagem == "hotel" or hospedagem == "hostel":
        break
    else:
        raise(ValueError("Ops, parece que você digitou uma opção inválida! Escolha entre hotel ou hostel!"))

# Conversão monetária para reais

EUR = 6.20
USD = 5.70
GBP = 7.10

hospedagem_diária_BRL = hospedagem_diária_EUR * EUR
alimentação_diária_BRL = alimentação_diária_USD * USD
lazer_BRL = lazer_GBP * GBP

# Regras do negócio

hospedagem_total = ()
if hospedagem == "hostel" and qtd_dias > 15:
    hospedagem_total = 0.9 * (hospedagem_diária_BRL * qtd_dias)
else:
    hospedagem_total = hospedagem_diária_BRL * qtd_dias

alimentação_total = alimentação_diária_BRL * qtd_dias

seguro = 45 * qtd_dias

custo_parcial = passagem + hospedagem_total + alimentação_total + lazer_BRL + seguro
taxa = ()
if custo_parcial > 15000:
    taxa = 0.08 * custo_parcial
else: 
    taxa = 0

custo_total = custo_parcial + taxa

# Validação do orçamento e viabilidade da viagem

orçamento_possível = ()
if custo_total <= orçamento:
    orçamento_possível = True
else:
    orçamento_possível = False

viável = ()
if qtd_dias > 0 and orçamento_possível == True:
    viável = True
else:
    viável = False

diferença = orçamento - custo_total
falta = ()
if diferença < 0:
    falta = True
else:
    falta = False

# Exibição de resultados
print(f"O nome do viajante é {nome}.")
print(f"O destino da viagem é {destino}.")
print(f"A duração da viagem é de {qtd_dias} dias.")
print(f"O tipo de hospedagem é {hospedagem}.")
print(f"O valor total da hospedagem é {round(hospedagem_total,2)} reais.")
print(f"O valor total da alimentação é {round(alimentação_total,2)} reais.")
print(f"O valor total do lazer é {round(lazer_GBP,2)} reais.")
print(f"O valor do seguro de viagem é {round(seguro,2)} reais.")
print(f"O valor da taxa internacional é {round(taxa,2)} reais.")
print(f"O custo total da viagem é {round(custo_total,2)} reais.")

if orçamento_possível == True:
    print("O orçamento disponível é possível.")
else: 
    print("O orçamento disponível é impossível.")

if viável == True:
    print("O status da viagem é viável.")
else:
    print("O status da viagem é inviável")

if falta == True:
    print(f"Faltaram {round(abs(diferença), 2)} reais para cobrir os custos da viagem.")
else:
    print(f"Sobraram {round(diferença,2)} reais do orçamento disponível para a viagem.")