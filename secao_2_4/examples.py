# Móduloes e Bibliotecas
# primeiro modo
import math
# segundo modo
import math as m
# terceiro modo
from math import sqrt, log2, cos
# Matplot
import matplotlib.pyplot as plt

# Usos math
math.sqrt(25)
math.log2(1024)
math.cos(45)
m.sqrt(25)
m.log2(1024)
m.cos(45)
sqrt(25)
log2(1024)
cos(45)


# Uso Matplot
# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Criar um gráfico de linha
plt.plot(x, y)

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar um título ao gráfico
plt.title('Exemplo de Gráfico de Linha')

# Mostrar o gráfico
plt.show()
