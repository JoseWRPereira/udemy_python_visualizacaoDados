import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,6,4,8,3]

x2 = [2,4,6,8,10]
y2 = [2,7,5,9,0]

plt.title("Gráfico de linhas")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.plot(x1,y1)
plt.show()

plt.title("Gráfico de barras")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.bar(x1,y1)
plt.show()

plt.title("Gráfico comparação de barras")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.bar(x1,y1, label="legenda 1")
plt.bar(x2,y2, label="legenda 2")
plt.legend()
plt.show()

plt.title("Gráfico de dispersão")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.scatter(x1,y1)
plt.show()

plt.title("Gráfico de barras com dispersão")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.bar(x1,y1)
plt.scatter(x1,y1, marker="*", color="r")
plt.plot(x1,y1, color="r")
plt.legend()
plt.show()

# Salvando figura
plt.title("Gráfico de barras com dispersão")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.bar(x1,y1)
plt.scatter(x1,y1, marker="*", color="r")
plt.plot(x1,y1, color="r")
plt.legend()
plt.savefig("grafico.pdf")
plt.savefig("grafico.png", dpi=300)
