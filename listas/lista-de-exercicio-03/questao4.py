vogais_maiusculas = ['A','E','I','O','U']
vogais_minusculas = ['a','e','i','o','u']
letra = str (input("Digite uma letra: "))


if letra in vogais_minusculas:
    print('Vogal')
elif letra in vogais_maiusculas:
    print('Vogal')
elif letra not in vogais_minusculas:
    print('consoante')
elif letra not in vogais_maiusculas:
    print('consoante')
