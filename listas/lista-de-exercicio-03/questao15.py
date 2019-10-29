lado_a = float (input("Digite o primeiro lado: "))
lado_b = float (input("Digite o segundo lado: "))
lado_c = float (input("Digite o terceiro lado: "))


if (lado_b - lado_c) < lado_a and (lado_b - lado_c) < lado_b and (lado_b - lado_c) < lado_c : 
	print('Formam triangulo')
elif (lado_a - lado_c) < lado_b and (lado_a - lado_c) < lado_a and (lado_a - lado_c) < lado_c :
	print('Formam triangulo')
elif (lado_a - lado_b) < lado_c and (lado_a - lado_b) < lado_a and (lado_a - lado_b) < lado_b :
	print('Formam triangulo')  
elif lado_a == lado_b and lado_b == lado_c:
     print('Triangulo equilatero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
     print('Triangulo isosceles')
elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
     print('Triangulo Escaleno')
else:
	print('Não formam triangulo')