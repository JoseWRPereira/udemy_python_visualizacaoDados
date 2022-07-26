
entrada = open("human.fasta").read()
saida = open("human.html", "w")

atcg = ['A', 'T', 'C', 'G']

cont = {}

for i in atcg:
    for j in atcg:
        cont[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    cont[ entrada[k+1]+entrada[k] ] += 1

# print( cont )

## HTML
i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px;\
                border: 1px solid #111; color:#fff;\
                height:100px; float:left;\
                background-color:rgba(0,0,200,\
                "+str(transparencia)+"')>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")

    i += 1
saida.close()