#!/bin/python3

import latexcalc
import math


print('testing operations only with numbers...')
fail = False
tests = []
tests.append([r'e^(1)                       ', math.e, 'exp()'])
tests.append([r'2*1e20                      ', 2*1e20, 'scientific numbers'])
tests.append([r'2^-2.5                      ', math.pow(2, -2.5), 'power of x'])
tests.append([r'-2/(0-3)                    ', -2/(0-3), 'simple brackets'])
tests.append([r'2+2^2*2                     ', 2+math.pow(2,2)*2, 'order of execution'])
tests.append([r'\cos((120/360)*(2*\pi))     ', math.cos((120/360)*(2*math.pi)), 'trigonometric function'])
tests.append([r'\sqrt 2                     ', math.sqrt(2), 'sqare root'])
tests.append([r'\sqrt{3^2+4^2}              ', math.sqrt(3**2+math.pow(4, 2)), 'pythagoras'])
tests.append([r'[1*2*3+4*5*6]/(2+1*1)       ', (1*2*3+4*5*6)/(2+1*1), 'long terms with * & / first, then + & -'])
tests.append([r'1/1/10                      ', 1/1/10, 'double division'])
tests.append([r'2*\sqrt{2+2+2}*2            ', 2*math.sqrt(2+2+2)*2, 'sqrt with {} brackets'])
tests.append([r'2\frac 1 2 2*\frac 1 3      ', 2+(1/2)*2*(1/3), 'fractions without brackets (abbreviated form)'])
tests.append([r'2*\frac{14}{10}+2           ', 2*14/10+2, 'fractions with {} brackets (normal form)'])

for test in tests:
    if latexcalc.calc(test[0]) == test[1]:
        print('ok:   '+test[0]+' > '+test[2])
    else:
        print('FAIL: '+test[0]+' # result: '+str(texCalc.calc(test[0])))
        fail = True
if fail:
    print('!!! TEST FAILED !!!')
    exit(1)
else: print('=== SUCCESS ===')


print('testing with values...')
fail = False
tests = []
tests.append([r'\sqrt(a^2+b^2)                          ', {'a':3,'b':4}, 5, 'pythagoras with values'])
tests.append([r'-\frac{p}{2}-\sqrt{{\frac{p}{2}}^2-q}   ', {'p':4,'q':3}, -2-math.sqrt(4-3), 'pythagoras with values'])
for test in tests:
    if latexcalc.calc(test[0], test[1]) == test[2]:
        print('ok:   '+test[0]+' > '+test[3])
    else:
        print('FAIL: '+test[0]+' # result: '+str(texCalc.calc(test[0], test[1])))
        fail = True
if fail:
    print('!!! TEST FAILED !!!')
    exit(1)
else: print('=== SUCCESS ===')



