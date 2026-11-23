# Notas para Claude (revisión 2026 del manual de LCC)

Este repositorio contiene el manual bilingüe (ES/EN) de *Laboratorio de
Computación Científica* (1.º del grado en Física, UCM) y los códigos de ejemplo
(`codigos/`). Las soluciones para el profesorado están en el repositorio
hermano `onlyforyoureyes`, que suele estar abierto en el mismo workspace.

## Proyecto en curso

- Revisión a fondo del manual y rediseño del curso para integrar la IA, con el
  enfoque "obtener, verificar y defender un resultado numérico".
- Se trabaja en la rama `revision-2026` en **los dos** repositorios. No tocar
  `main` ni abrir pull requests sin que se pida.
- **Antes de seguir, leer [docs/revision-2026.md](docs/revision-2026.md)**: es
  el cuaderno de bitácora con la propuesta, el estado de cada capítulo, lo hecho
  y las decisiones pendientes. Actualizarlo al terminar cada capítulo.
- Orden de revisión (el del curso): introprog ✔, intronumpy ✔, matplotlib ✔,
  aritmetica ✔, calraiz ✔, sistemas ✔, interpolacion ✔, integracion, tratamientoest,
  simbolico. Más adelante, un capítulo nuevo sobre programar con IA.
- Decisión tomada: se mantiene **Spyder** (con el plug-in spyder-notebook) como
  IDE del curso. No proponer cambiarlo.
- Las decisiones abiertas listadas en el documento de revisión no se ejecutan
  sin preguntar.

## Privacidad

- **No abrir nunca `onlyforyoureyes/big_brother/`**: contiene notas de
  estudiantes (datos personales).
- No enviar datos personales del profesorado ni del alumnado a servicios
  externos.

## Estructura del LaTeX

- Cada capítulo es un `.tex` (p. ej. `intronumpy.tex`) incluido en
  `lcc_manual.tex`; los `cabecera_*.tex` compilan un capítulo suelto
  (`cabecera_programacion` → introprog, `cabecera_numpy` → intronumpy, etc.).
- Disposición bilingüe con `paracol`: texto en español, `\switchcolumn`, texto
  en inglés. Un `\switchcolumn` que falta intercambia los idiomas sin error.
- Los ejercicios van como `\section{Ejercicios}` en español seguido de
  `\section{Exercises}` entre `\selectlanguage{english}` …
  `\selectlanguage{spanish}`.
- Código con `minted` (requiere `-shell-escape` y `pygmentize` en el PATH).
  `\mintinline` no corta palabras: un token largo se sale de la columna; revisar
  la página renderizada.
- El repositorio se sincroniza con Overleaf (ramas `overleaf-*`); vigilar texto
  pegado desde PDF (acentos sueltos como `´a`, cabeceras "CAP´ITULO").

## Cómo editar y comprobar

- La mayoría de `.tex` y `.py` usan finales de línea CRLF: conservarlos.
- Método fiable: scripts de sustitución literal (antiguo → nuevo) con
  comprobación del número de apariciones. Muchas líneas acaban en espacios
  significativos (`\rightarrow \ `, `Out[n]: `, líneas solo con tabuladores en
  bloques minted); para esas, usar expresiones regulares.
- `python tools/check_blocks.py . <capitulo>.tex` ejecuta todos los bloques de
  código de un capítulo en una copia temporal de `datos/` (algunos escriben
  ficheros). Ver [tools/README.md](tools/README.md).
- `python tools/spellcheck.py` revisa ortografía ES/EN (necesita `spylls` y los
  diccionarios en `tools/dict/`, que no se versionan).
- Compilar en una copia de trabajo fuera del repositorio, no en el propio
  repositorio, para no ensuciarlo con auxiliares.
- Verificar numéricamente cualquier afirmación matemática del texto antes de
  darla por buena o corregirla.

## Entorno (ordenador del despacho; puede variar en otros)

- Python con numpy/scipy/sympy: `C:/Users/abierto/anaconda3/python.exe` (el
  `python` del PATH es un 3.9 sin sympy).
- pdflatex (MiKTeX) necesita `anaconda3` y `anaconda3/Scripts` al principio del
  PATH para encontrar `pygmentize`. El manual completo tarda unos 4 minutos.
- Ghostscript para revisar páginas renderizadas:
  `C:/Program Files/gs/gs10.01.2/bin/gswin64c.exe`.
