# Herramientas de revisión

Scripts usados en la revisión de 2026 (ver `docs/revision-2026.md`).

- `check_blocks.py`: ejecuta todos los bloques de código Python (`minted`)
  de uno o varios capítulos y lista los que fallan. Es el germen de la
  comprobación automática del código propuesta en la medida G.

      python tools/check_blocks.py . introprog.tex intronumpy.tex

  Algunos fallos son esperados: errores puestos a propósito, pseudocódigo
  y bloques que solo muestran la salida.

- `spellcheck.py`: corrector ortográfico bilingüe que distingue la
  columna española de la inglesa. Requiere `pip install spylls` y los
  diccionarios Hunspell (`es.aff/.dic`, `en.aff/.dic`) en `tools/dict/`
  o en la carpeta indicada por la variable `LCC_DICT`. Solo detecta
  palabras mal escritas, no errores gramaticales.
  En Linux basta con instalar `hunspell-es` y `hunspell-en-us` y enlazar
  `/usr/share/hunspell/es_ES.*` y `en_US.*` como `tools/dict/es.*` y
  `en.*`; en Windows, descargar los `.aff/.dic` de los diccionarios de
  LibreOffice (github.com/LibreOffice/dictionaries).

Necesitan el Python de Anaconda (numpy, scipy, sympy, pandas, matplotlib).
