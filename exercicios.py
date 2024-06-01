import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# Solicita ao usuário para inserir o primeiro número inteiro
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicita ao usuário para inserir o segundo número inteiro
num2 = int(input("Digite o segundo número inteiro: "))

# Calcula a soma dos dois números
soma = num1 + num2


# Imprime o resultado
print("A soma dos dois números é:", soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Calcula o resto da divisão do número por 5
resto = numero % 5

# Imprime o resultado
print("O resto da divisão de", numero, "por 5 é:", resto)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# Solicita ao usuário para inserir o primeiro número inteiro
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicita ao usuário para inserir o segundo número inteiro
num2 = int(input("Digite o segundo número inteiro: "))

multiplicacao = num1 * num2

# Imprime o resultado
print("A multiplicação entre os números é:", multiplicacao)


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num3 = int(input("Digite o primeiro número inteiro: "))
num4 = int(input("Digite o primeiro número inteiro: "))

resultado = num3 // num4

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num3 = int(input("Digite o primeiro número inteiro: "))
print(num3 ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num3 = float(input("Digite o primeiro número inteiro: "))
float(input("Digite o primeiro número inteiro: "))float(input("Digite o primeiro número inteiro: "))

soma = num3 + num4
print(soma)


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num5 = float(input("Digite o primeiro número inteiro: "))
num6 = float(input("Digite o primeiro número inteiro: "))

media = num5 + num6 /2
print("A média dos dois números é:" media)




# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))

potencia = base ** expoente
print("O resultado é: ", potencia)


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura de {celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}"".format(area_do_circulo)
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto1 = input("Digite um texto em minúsculo: ")
texto_maiusculo = texto1.upper()
print("A string em maiúsucla é:", texto_maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
texto2 = input("Digite o seu nome em letras maiuscúla: ")
texto_minusculo = texto2.lower()
print("O nome em minusculo é:", texto_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()

print("A frase sem espaços no início e no final é:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o : {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o : {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o : {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a primeira string: ")

conc = string1 + '' +  string2  
print("A string concatenada é: ", conc)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1 = input("Digite a primeira expressão booleana (True ou False): ")
expressao2 = input("Digite a segunda expressão booleana (True ou False): ")

bool1 = expressao1.strip().lower() == 'true'
bool2 = expressao2.strip().lower() == 'true'

resultado = bool1 and bool2
print("O resultado da operação AND entre as duas expressões booleanas é:", resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

expressao1 = input("Digite a primeira expressão booleana (True ou False): ")
expressao2 = input("Digite a segunda expressão booleana (True ou False): ")

bool1 = expressao1.strip().lower() == 'true'
bool2 = expressao2.strip().lower() == 'true'

resultado = bool1 or bool2
print("O resultado da operação AND entre as duas expressões booleanas é:", resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

expressao = input("Digite um valor booleano (True ou False): ")
booleano = expressao.strip().lower() == 'true'

inverso = not booleano
print("O valor booleano invertido é:", inverso)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 != numero2:
    print("Os números", numero1, "e", numero2, "são diferentes.")
else:
    print("Os números", numero1, "e", numero2, "são iguais.")


# #### try-except e if

# 21: Conversor de Temperatura
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        # Solicita ao usuário para escolher o tipo de conversão
        conversion_type = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ").strip().upper()
        
        if conversion_type == 'C':
            # Solicita ao usuário a temperatura em Celsius e tenta converter para float
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} graus Celsius são equivalentes a {fahrenheit} graus Fahrenheit.")
        
        elif conversion_type == 'F':
            # Solicita ao usuário a temperatura em Fahrenheit e tenta converter para float
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} graus Fahrenheit são equivalentes a {celsius} graus Celsius.")
        
        else:
            print("Tipo de conversão inválido. Por favor, digite 'C' ou 'F'.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a temperatura.")

# Chama a função de conversão
convert_temperature()

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
