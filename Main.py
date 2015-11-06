from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def Silvester(func):
    dx = diff(func, x)
    dy = diff(func, y)
    dz = diff(func, z)
    print(dx, dy, dz)
    result = solve([dx, dy, dz], [x, y, z])
    print(result)

    dxx = diff(dx, x)
    dxy = diff(dx, y)
    dxz = diff(dx, z)

    dyx = diff(dy, x)
    dyy = diff(dy, y)
    dyz = diff(dy, z)

    dzx = diff(dz, x)
    dzy = diff(dz, y)
    dzz = diff(dz, z)

    M = Matrix([[dxx, dxy, dxz], [dyx, dyy, dyz], [dzx, dzy, dzz]])
    N = Matrix([[dxx, dxy], [dyx, dyy]])
    print(M)
    minor1 = M[0, 0]
    minor2 = N.det()
    minor3 = M.det()
    m1 = minor1.evalf(subs={x: result[0][0]})
    m2 = minor2.evalf(subs={x: result[0][0]})
    m3 = minor3.evalf(subs={x: result[0][0]})
    print(m1, m2, m3)
    if m1 >= 0 and m2 >= 0 and m3 >= 0:
        matrix_status = "matrix >= 0"
        print(matrix_status)
        return print("X - locmin")
    elif m1 <= 0 and m2 >= 0 and m3 <= 0:
        matrix_status = "matrix <= 0"
        print(matrix_status)
        return print("X - locmin")
    else:
        matrix_status = "matrix unindentified"
        print(matrix_status)
        return print("X - isn't locextrm")

def OptimizationDeter(func):
    m = 0
    done = False
    while not done:
        dx = diff(func, x, m)
        print(dx)
        check = dx.evalf(subs={x:0})
        print(check)
        print(m)
        if check != 0:
            return m
        else:
            m += 1
    return m

def Lagrange(func, equation):
    j0 = 1
    L = j0*(func) + j1*(equation)
    Lx = diff(L, x)
    Ly = diff(L, y)
    print(Lx, '\n', Ly, '\n', equation)
    calc = solve([Lx, Ly, equation])
    print(calc)
    j = calc[0][j1]
    LM = Matrix(((diff(Lx, x), diff(Lx, y)), (diff(Ly, x), diff(Ly, y))))
    print(LM)
    minor1 = LM[0, 0].evalf(subs={j1:j})
    minor2 = LM.det().evalf(subs={j1:j})
    print(minor1, minor2, j)
    H = h1 * diff(equation, x) + h2 * diff(equation, y)
    print(H)
    y1 = calc[-1][y]
    x1 = calc[-1][x]
    print(y1, x1, x1/y1)
    result = solve(H, h1)
    print(result)
    LH = h1**2 + 2*h1*h2 + h2**2
    results = result[0].subs({x:x1, y:y1})
    LH = LH.subs({h1:results})
    print(LH)
    Result = LH.subs({h2:1})
    print(results)
    if Result > 0:
        print('local minimum')
    elif Result < 0:
        print('local maximum')
    else:
        print('not extremum')
    return Result

x, y, z = symbols('x y z')
j0, j1, h1, h2 = var('j0 j1 h1 h2')
task = input('Silv, Opti or Lag?')
if task == 'Silv':
    try:
        func = parse_expr(input('Give me function'))
    except IOError:
        func = x**3 + y**2 + z**2 + y * z - 3 * x + 6 * y + 2
    Silv = Silvester(func)
elif task == 'Opti':
    try:
        func = parse_expr(input('Give me function'))
        print(func)
    except IOError:
        func = sin(x) * (-x)**5
    Opti = OptimizationDeter(func)
elif task == 'Lag':
    try:
        func = parse_expr(input('Give me function'))
        equation = parse_expr(input('Give me Equation'))
    except IOError:
        func = 5 * x**2 + y**2 + 2 * x * y
        equation = x * y - 10
    Lag = Lagrange(func, equation)
