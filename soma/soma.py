"""
Programa multiplica
Requisito: este programa pega dois números digitados pelo usuário, calcula produto dele e coloca o resultado na tela junto com uma frase explicativa
Autora: Letícia Maria Pereira
Data: 26/10/2022
Versão: 0.0.2
Corrige o bug: chamar de parcela o que é na verdade, fator.
Inclusão de funcionalidade: informar ao usuário para que serve o programa
"""
#Entrada
print("Este programa calcula o produto de dois números dados pelo usuário")
numero_1 = int(input("\nDigite o primeiro fator: "))
numero_2= int(input("\nDigite o segundo fator: "))

#Processamento
produto= numero_1 * numero_2

#Saída

print (f"A multiplicação dos números {numero_1} e {numero_2} é igual a {produto}")
