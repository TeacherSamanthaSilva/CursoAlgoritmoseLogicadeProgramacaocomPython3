#escreva uma função que recebe um dado texto e se esse texto tem mais de 20 caracteres retorque que é um texto longo se tem menos retorne que é um texto curto

def classificar_texto(texto):
    if len(texto) > 20:
        return "É um texto longo"
    else:
        return "É um texto curto"


# Programa principal
texto_usuario = input("Digite um texto: ")
resultado = classificar_texto(texto_usuario)
print(resultado)
