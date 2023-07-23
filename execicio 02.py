numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
multiplicacao = numero1 * numero2
subtracao = numero1 - numero2
opcao = int(input('1 - Soma\n2 - Multiplicacao \n3 - Subtração\nEscolha uma opção: '))
if opcao == 1:
	print(f'A soma entre os números é {soma}')
if opcao == 2:
	print(f'A multiplicacao entre os números é {Multiplicacao}')
if opcao == 3:
	print(f'A Subtração entre os números é  {subtracao}')