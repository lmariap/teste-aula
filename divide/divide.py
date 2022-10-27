"""
Programa divide
Requisito: Crie um programa que leia dois números inteiros do teclado, calcula a divisão dele e coloca o resultado na tela junto com uma frase explicativa
Autora: Letícia Maria Pereira
Data: 26/10/2022
Versão: 0.0.1
Corrige o bug: chamar de parcela o que é na verdade, fator.
Inclusão de funcionalidade: informar ao usuário para que serve o programa
"""
#Entrada
print("Este programa calcula a razão de dois números dados pelo usuário")
numerador = int(input("\nDigite o numerador: "))
denominador= int(input("\nDigite o denominador: "))

#Processamento
razão= numerador / denominador

#Saída

print (f"A divisão dos números {numerador} e {denominador} é igual a {razão}")
