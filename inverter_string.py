def inverter_string(string):
    # Inicializamos uma string vazia para armazenar a string invertida
    string_invertida = ""
    # Percorremos a string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Concatenamos cada caractere na string invertida
        string_invertida += string[i]
    # Retornamos a string invertida
    return string_invertida

# Exemplo na prática
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("A string invertida é:", string_invertida)
