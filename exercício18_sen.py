import math
ângulo = eval(input('Digite o ângulo  '))
seno = math.sin(math.radians(ângulo))
print('O valor de seno de {}º é: {:.3f}'.format(ângulo, seno))
