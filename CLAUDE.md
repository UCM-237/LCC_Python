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
- La rama `revision-2026` está en GitHub (`UCM-237/LCC_Python` y
  `UCM-237/onlyforyoureyes`) y la consultan otros profesores de la
  asignatura: hacer `git push` cuando el profesor lo pida (lo pidió en nov
  2026 al terminar los capítulos), no por iniciativa propia.
- **Antes de seguir, leer [docs/revision-2026.md](docs/revision-2026.md)**: es
  el cuaderno de bitácora con la propuesta, el estado de cada capítulo, lo hecho
  y las decisiones pendientes. Actualizarlo al terminar cada capítulo.
- Orden de revisión (el del curso): introprog ✔, intronumpy ✔, matplotlib ✔,
  aritmetica ✔, calraiz ✔, sistemas ✔, interpolacion ✔, integracion ✔,
  tratamientoest ✔, simbolico ✔, introduccion ✔ y preface ✔ (nov 2026): la
  revisión capítulo a capítulo está terminada. Claude (Anthropic) figura como
  cuarto autor en la portada (`lcc_manual.tex`) a petición del profesor.
  Siguiente fase (hoja de ruta del
  documento de revisión): capítulo nuevo sobre programar con IA, guía de uso
  de la IA y evaluación.
- Patrón seguido en cada capítulo: corregir errores (comprobando cada número
  y cada salida), sección o apartados de verificación, ejercicios de los tipos
  nuevos (*predice y mide*, *depura*, *¿cuál es correcta?*, *critica la
  explicación* de una IA, *primero los tests*) y solucionario
  `onlyforyoureyes/<tema>/EjerciciosLibro.ipynb` comprobado con `assert`.
- **Al terminar la revisión**, recordar al profesor los "Recordatorios" del
  principio de `docs/revision-2026.md` (subir `datosLauraLucia.txt` nuevo al
  campus virtual, recompilar `pdfs/`).
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
  Al compilar un capítulo suelto, las referencias a otros capítulos salen
  como "??" (no es un error).
- Etiquetas de capítulo: `ch:raices`, `ch:integracion`, `chp:arit`, etc.
  (comprobar con `grep '\\label' <capitulo>.tex | head`). Las secciones
  inglesas repiten la etiqueta con `-2` y los ejercicios ingleses con `-en`.
- Los capítulos revisados empiezan con `\sloppy` (tras `\chaptermark`) y
  terminan con `\fussy`; los bloques que solo muestran salida van en
  `\begin{minted}{text}` (así `check_blocks` no los ejecuta).
- **PDFs**: los finales van solo en `pdfs/` (la raíz los ignora
  `.gitignore`). El manual completo se compila con tres pasadas de
  `pdflatex -shell-escape` (unos 3,5 min cada una en casa).
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

- Finales de línea: en el despacho (Windows) muchos ficheros tienen CRLF; en
  el ordenador de casa (Linux) son LF. Conservar los que tenga cada fichero
  (leer y escribir con `newline=''`).
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
  darla por buena o corregirla. Comparar también las salidas impresas en el
  texto con las reales (extraer el bloque y ejecutarlo).
- `tools/figuras/figuras_cap9.py` y `figuras_cap10.py` regeneran las figuras
  nuevas (semillas fijas). Al regenerar, los PDF cambian solo en la fecha
  interna: restaurar con `git checkout` los que no deban cambiar.

## Entorno: ordenador de casa (Linux)

- `python3` es Anaconda (`/home/juan/anaconda3`) con numpy, scipy, sympy 1.12,
  pandas y jupyter; `pdflatex` es TeX Live 2023 de Debian y encuentra
  `pygmentize`. Diccionarios del corrector en `tools/dict/`.
- **pdfTeX 1.40.25 se cae (violación de segmento)** si un enlace de
  `hyperref` queda partido entre niveles de caja (en el log, justo antes:
  "\pdfendlink ended up in different nesting level than \pdfstartlink"). Solo
  pasa con el `.aux` completo, así que alterna pasadas buenas y malas. Se
  arregló (nov 2026) cambiando el `\ref` culpable por `\ref*` (sin enlace) en
  `sistemas.tex`; si reaparece tras cambiar la maquetación, buscar el aviso y
  hacer lo mismo (pendiente 8 del documento de revisión).
- Con `paracol`, una figura flotante colocada entre dos `paracol` puede
  perderse sin aviso (pasó con `fig:residuos`): si una referencia oscila
  entre número y "??" de una pasada a otra, convertir la figura en `minipage`
  con `\captionsetup{type=figure}`. Comprobar siempre que la última pasada no
  pida "Rerun".

## Entorno: ordenador del despacho (Windows)

- Python con numpy/scipy/sympy: `C:/Users/abierto/anaconda3/python.exe` (el
  `python` del PATH es un 3.9 sin sympy).
- pdflatex (MiKTeX) necesita `anaconda3` y `anaconda3/Scripts` al principio del
  PATH para encontrar `pygmentize`. El manual completo tarda unos 4 minutos.
- Ghostscript para revisar páginas renderizadas:
  `C:/Program Files/gs/gs10.01.2/bin/gswin64c.exe`.
