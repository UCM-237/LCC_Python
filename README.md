Para compilar el manuel completo:

1. Es preciso tener instalado Pygments (python):
$ pip install Pygments

2. Compilar con pdfLatex el manual completo:
$ pdflatex -synctex=1 -interaction=nonstopmode -shell-escape lcc_manual.tex

3. Compilar capítulos por separado: 
$ pdflatex -synctex=1 -interaction=nonstopmode -shell-escape cabecera_nombredelcapltulo.tex

Por ejemplo: 
cabecera_numpy.tex
$ pdflatex -synctex=1 -interaction=nonstopmode -shell-escape cabecera_numpy.tex

Compila solo el capítulo de introducción a numpy
