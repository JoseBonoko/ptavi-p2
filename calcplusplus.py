#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcplus
import csv

if __name__ == "__main__":
    with open(sys.argv[1], newline='') as f:
        fich = open(sys.argv[1], 'r', encoding='utf-8')
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        lineas = fich.readlines()
        calcul = calcplus.calcoohija.CalculadoraHija()
        for linea in lineas:
            elementos = linea.split(',')
            if elementos[0] == "suma":
                resultsuma = 0
                for elemento in elementos[1:]:
                    elemento = int(elemento)
                    resultsuma = calcul.plus(resultsuma, elemento)
                print(linea)
                print(resultsuma)
            elif elementos[0] == "resta":
                resultresta = elementos[1]
                for elemento in elementos[2:]:
                    resultresta = int(resultresta)
                    elemento = int(elemento)
                    resultresta = calcul.minus(resultresta, elemento)
                print(linea)
                print(resultresta)
            elif elementos[0] == "multiplica":
                resultmulti = elementos[1]
                for elemento in elementos[2:]:
                    resultmulti = int(resultmulti)
                    elemento = int(elemento)
                    resultmulti = calcul.multi(resultmulti, elemento)
                print(linea)
                print(resultmulti)
            elif elementos[0] == "divide":
                resultdivis = elementos[1]
                for elemento in elementos[2:]:
                    resultdivis = int(resultdivis)
                    elemento = int(elemento)
                    if resultdivis == 0 or elemento == 0:
                        sys.exit("Division by zero is not allowed")
                    else:
                        resultdivis = calcul.divide(resultdivis, elemento)
                print(linea)
                print(resultdivis)
            else:
                sys.exit('Sólo se puede sumar, restar, multiplicar o dividir')
