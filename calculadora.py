num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo  valor: "))
operacao = input("Insira a operação matemática (+, -, *, /): ")

if(operacao == "+"):
    print(f'{num1} + {num2} = {num1+num2}')
elif(operacao == "-"):
    print(f'{num1} - {num2} = {num1-num2}')
elif(operacao == "*"):
     print(f'{num1} * {num2} = {num1*num2}')
elif(operacao == "/"):
      print(f'{num1} / {num2} = {num1/num2}')
