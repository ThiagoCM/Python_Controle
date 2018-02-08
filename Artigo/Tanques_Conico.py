# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import control.matlab
import math
import matplotlib.pyplot as plt
import numpy
import scipy
from sympy.solvers import solve
from sympy import Symbol #essa biblioteca vai servir para definir os símbolos u, h1, h2
import sympy


# ------------------ #
# Definindo as variáveis como variáveis simbólicas    #
# ------------------ #
A1 = Symbol ('A1')
A2 = Symbol ('A2')
A3 = Symbol ('A3')
a1 = Symbol ('a1')
a2 = Symbol ('a2')
a3 = Symbol ('a3')
h1 = Symbol ('h1')
h2 = Symbol ('h2')
h3 = Symbol('h3')
km = Symbol('km')
u = Symbol ('u')
g = Symbol ('g')
p = Symbol('p')

# Áreas transversais dos tanques 1 e 2
A1 = math.pi*math.pow(0.5,2)
A2 = 0.7*1.2

# Constante do tanque 3
p = math.pi*math.pow(0.6,2)

# Áreas transversais de tubulação de saída dos tanques 1, 2, 3
a1 = math.pow(0.03, 2) * math.pi
a2 = math.pow(0.025, 2) * math.pi
a3 = math.pow(0.028, 2) * math.pi

# Constante do motor
km = 0.0007

# Constante da gravidade
g = 9.87

# Ponto de equilíbrio desejado p/ tanque 3
h3 = 0.7

# Área transversal do tanque 3
A3 = p*(h3 + 0.2)

# ------------------ #
# Equações de altura #
# ------------------ #
dh1 = Symbol('(km*u - (a1*math.sqrt(2*g*h1)))/A1') # definir h1

dh2 = Symbol('((a1*math.sqrt(2*g*h1)) - (a2*math.sqrt(2*g*h2)))/A2') # definir h2

dh3 = Symbol('((a2*math.sqrt(2*g*h2)) - (a3*math.sqrt(2*g*h3)))/A3')
# ------------------------------- #
# Matrizes do sistema linearizado #
# ------------------------------- #

As = numpy.zeros((3,3))


# Primeira linha
As[0][0] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #a variável a ser integrada é h1
As[0][1] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em h2
As[0][2] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em h3

# Segunda linha
As[1][0] = scipy.misc.derivative(dh2, 1.0, dx = 0.01) #modificar a variável p/ ser em h1
As[1][1] = scipy.misc.derivative(dh2, 1.0, dx = 0.01) #modificar a variável p/ ser em h2
As[1][2] = scipy.misc.derivative(dh2, 1.0, dx = 0.01) #modificar a variável p/ ser em h3

# Terceira linha
As[2][0] = scipy.misc.derivative(dh3, 1.0, dx = 0.01) #modificar a variável p/ ser em h1
As[2][1] = scipy.misc.derivative(dh3, 1.0, dx = 0.01) #modificar a variável p/ ser em h2
As[2][2] = scipy.misc.derivative(dh3, 1.0, dx = 0.01) #modificar a variável p/ ser em h3

#B = numpy.zeros((3, 1))
#
## Primeira linha
#B[0][0] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em u
#
## Segunda linha
#B[1][0] = scipy.misc.derivative(dh2, 1.0, dx = 0.01) #modificar a variável p/ ser em u
#
## Terceira linha
#B[2][0] = scipy.misc.derivative(dh3, 1.0, dx = 0.01) #modificar a variável p/ ser em u
#
#C = numpy.zeros(3)
#
## Primeira coluna
#C[0][0] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em h1
#
## Segunda coluna
#C[0][1] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em h2
#
## Terceira coluna
#C[0][2] = scipy.misc.derivative(dh1, 1.0, dx = 0.01) #modificar a variável p/ ser em h3
#
#D = numpy.zeros(1)
#
#D = scipy.misc.derivative(h3, 1.0, dx = 0.01) #modificar a variável p/ ser em u
#

## ------------------------------- #
## Pontos de equilíbrio p/ h3      #
## ------------------------------- #
#
#sh2 = Symbol('h2')
#peH3 = solve(dh3, sh2)
#
#sh1 = Symbol('h1')
#peH2 = solve(dh2, sh1)
#
#su = Symbol('u')
#peH1 = solve(dh1, su)
#
#
#peH1 = solve()
#num = [4.5 * math.exp(-4), 2.3*math.exp(-4)]
#den = [1, 0.9, 0.24, 0.02, 9.7*math.exp(-5)]
#sys = control.tf(num, den)
#
#print(sys)
#
#[Ta, yout] = control.step_response(sys)
#
#plt.plot(Ta, yout)
