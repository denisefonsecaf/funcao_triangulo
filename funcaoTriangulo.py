#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
#ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
#os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
#não formam triângulo escrever os valores lidos. (Se a > b + c não formam
#triângulo algum, se a é o maior).

import math

# Função para verificar se os valores formam um triângulo
def forma_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

# Função para calcular a área de um triângulo usando a fórmula de Heron
def calcular_area_triangulo(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Solicita ao usuário que insira os valores a, b e c
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verifica se os valores formam um triângulo
if forma_triangulo(a, b, c):
    area = calcular_area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo. A área do triângulo é {area:.2f}")
else:
    print(f"Os valores não formam um triângulo. Valores digitados: a = {a}, b = {b}, c = {c}")