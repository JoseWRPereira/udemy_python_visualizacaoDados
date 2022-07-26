import matplotlib.pyplot as plt

entrada = open("bacteria.fasta").read()
saida = open("bacteria.html", "w")

atcg = ['A', 'T', 'C', 'G']

cont = {}

for i in atcg:
    for j in atcg:
        cont[i+j] = 0

entrada = entrada.replace("\n","")

# for k in range(len(entrada)-1):
    # cont[entrada[k]+entrada[k+1]] += 1

print( cont )