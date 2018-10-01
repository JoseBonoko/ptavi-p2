#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":
    fich = open(sys.argv[1], 'r', encoding = 'utf-8')
    calc =  calcoohija.CalculadoraHija()
    lineas = fich.readlines()
    for linea in lineas:
        elementos = linea.split(',')
        if elementos[0] == "suma":
            resultsuma = 0
            for elemento in elementos[1:]:
                elemento = int(elemento)
                resultsuma = calc.plus(resultsuma, elemento)
            print(resultsuma)
        elif elementos[0] == "resta":
            resultresta = elementos[1]
            for elemento in elementos[2:]:
                resultresta = int(resultresta)
                elemento = int(elemento)
                resultresta = calc.minus(resultresta, elemento)
            print(resultresta)
        elif elementos[0] == "multiplica":
            resultmulti = elementos[1]
            for elemento in elementos[2:]:
                resultmulti = int(resultmulti)
                elemento = int(elemento)
                resultmulti = calc.multi(resultmulti, elemento)
            print(resultmulti)
        elif elementos[0] == "divide":
            resultdivision = elementos[1]
            for elemento in elementos[2:]:
                resultdivision = int(resultdivision)
                elemento = int(elemento)
                if resultdivision == 0 or elemento == 0:
                    sys.exit("Division by zero is not allowed")
                else:
                    resultdivision = calc.divide(resultdivision, elemento)
            print(resultdivision)
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')
