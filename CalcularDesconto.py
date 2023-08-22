valor = float(input("Insira o valor de sua compra: "))
Desconto = float(input("Insira o desconto recebido em %: "))
desconto= Desconto/100
res = valor-(valor*desconto)
print(f'Valor descontado: -R${res-valor}')
print(f'valor final: R${res}')
