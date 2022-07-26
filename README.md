# Visualização de Dados com Python

Curso na plataforma Udemy

Data Science: Visualização de Dados com Python

Criado por Diego Mariano, Ph.D.

Objetivo: Visualizações de dados usando a linguagem de programação Python e a biblioteca Pyplot


## Criação de gráficos com python

Requisitos: biblioteca Matplotlib.pyplot

```bash
pip install matplotlib
```

#### Exemplo
```python
plt.plot(x1,y1, color="r", linestyle="--")

```

* Parâmetros do método plot
    * color: cor (ver exemplos abaixo)
        * 'b' blue
        * 'g' green
        * 'r' red
        * 'c' cyan
        * 'm' magenta
        * 'y' yellow
        * 'k' black
        * 'w' white
    * label: rótulo
    * linestyle: estilo de linha
        * '-' solid line style
        * '--' dashed line style
        * '-.' dash-dot line style
        * ':' dotted line style
    * linewidth: largura da linha
    * marker: marcador
        * '.' point marker
        * ',' pixel marker
        * 'o' circle marker
        * 'v' triangle_down marker
        * '^' triangle_up marker
        * '<' triangle_left marker
        * '>' triangle_right marker
        * '1' tri_down marker
        * '2' tri_up marker
        * '3' tri_left marker
        * '4' tri_right marker
        * 's' square marker
        * 'p' pentagon marker
        * '*' star marker
        * 'h' hexagon1 marker
        * 'H' hexagon2 marker
        * '+' plus marker
        * 'x' x marker
        * 'D' diamond marker
        * 'd' thin_diamond marker
        * '|' vline marker
        * '_' hline marker

Fonte: [matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)