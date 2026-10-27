# ZeroDivisioneError
'x = 1 / 0'

# IndexError
'''x = [5, 6, 10, 4]
print(x[8])'''

# ValueError
'''x = int(input('Informe um inteiro: '))'''

# KeyError
x = { 'RN' : 'Natal' }
'''print(x['PB'])'''

import math
import numpy as np
arr = np.array([10, 15, 20, 25, 30])
result = np.where(arr > 20)
print(result) # Output: (array([3, 4]),)