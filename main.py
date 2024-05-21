import math
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
import sympy as sp
from sympy import init_session
from sympy.plotting import plot
from sympy.parsing.latex import parse_latex
from sympy.vector import CoordSys3D, matrix_to_vector

init_session()
a, b, c, A, B, C = symbols('a b c A B C', real=True)
r, phi, theta = symbols('r phi theta', real=True)
k = Function('k')(t)

O = CoordSys3D('O')


A = Matrix(2, 2, [2, 8*sqrt(2), -8*sqrt(2)*sin(4*sqrt(2)) + 2*cos(4*sqrt(2)), 8*sqrt(2)*cos(4*sqrt(2))+2*sin(4*sqrt(2))])
print("A ="); pprint(A)
print(f'{det(A)=} = {N(det(A))}')

print("\nsolve is")
pprint(A.solve(Matrix([0, 0])))
