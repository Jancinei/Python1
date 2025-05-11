import math

ângulo = eval(input('digite o ãngulo  '))
tang = math.tan(math.radians(ângulo))
print('A tangente de {} é {:.3f}'.format(ângulo, tang))
