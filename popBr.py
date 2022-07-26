# Crescimento da população brasileira 1980-2016
# DataSUS

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title("Crescimento populacional no Brasil (1980-2016)")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color='b')
# plt.show()
plt.savefig("popBr.png", dpi=300)