import math

ângulo = eval(input('Digite o valor do ângulo  '))
con = math.cos(math.radians(ângulo))
print ('O valor do conseno de {} é {:.3f}'. format(ângulo, con))