# Revisión del material y propuesta de reorientación de LCC (2026)

Rama de trabajo: `revision-2026` (en `LCC_Python` y en `onlyforyoureyes`).

Este documento recoge (1) lo que se ha corregido en la primera pasada, (2) lo
que queda pendiente y necesita una decisión, y (3) una propuesta para
reorientar la asignatura asumiendo que los alumnos tienen acceso a asistentes
de IA.

---

## 1. Qué se ha corregido

### Cómo se ha revisado

- Compilación completa del manual (540 págs.) y análisis del log de LaTeX.
- Ejecución de todos los scripts de `codigos/` y del solucionario.
- **Extracción y ejecución de los ~320 bloques de código del texto**,
  capítulo a capítulo, para encontrar ejemplos que no funcionan tal como
  están impresos.
- Corrector ortográfico bilingüe (Hunspell es_ES / en_US) que respeta la
  estructura `paracol` (columna izquierda en español, derecha en inglés);
  ~690 candidatos revisados a mano.
- Comprobación numérica de los métodos del solucionario frente a
  `numpy`/`scipy`.

### Manual (`LCC_Python`)

| Tipo | Qué | Dónde |
|---|---|---|
| **Grave** | ~168 líneas de texto copiadas de un PDF (cap. 2: suma de matrices, Fibonacci) pegadas por error en mitad de una frase, partiendo `\ref{errn}`. Se introdujo en el commit `778ef2f` (sincronización con Overleaf, ago-2024) y aparecía en el PDF publicado. | `calraiz.tex` |
| **Grave** | Faltaba un `\switchcolumn`: el teorema del punto fijo atractivo salía con el español en la columna inglesa y viceversa. | `calraiz.tex` |
| Conceptual | Se afirmaba que `Polynomial.roots` devuelve la parte real de las raíces complejas, con el ejemplo x²+2x+1 (raíz doble real). Reescrito. | `calraiz.tex` |
| Conceptual | El código de las funciones de sistemas copiaba con `.copy()`: con arrays de enteros las divisiones **se truncan sin aviso**. Cambiado a `.astype(float)` con una nota bilingüe que lo explica. | `sistemas.tex` |
| Conceptual | Regla de relleno de la matriz S en la SVD incorrecta (`n>m` dos veces). | `intronumpy.tex` |
| Ejemplos | Ejemplos que no se ejecutan tal como están impresos: `3e -4`, `tex`/`tex2`, `LL = [1, 'p,,L,-0.7]`, módulo `eq_sec_grado` (el fichero es `eq_seg_grado.py`), `norm(A,inf)`, `S` sin crear en la SVD, `bP`/`Pb`, `norma`/`norma_naive`, `prin2t`, `np.pi` dentro de SymPy. | varios |
| LaTeX | 2 referencias rotas (`fig:regula_eng`, capítulo de sistemas sin etiqueta) y 15 etiquetas duplicadas que hacían que algunas referencias apuntaran a la ecuación equivocada. | varios |
| Erratas | ~340 erratas ortográficas en ambos idiomas, y algunas gramaticales del prefacio. | todos |
| Repo | 1418 ficheros de caché de `minted`, checkpoints de Jupyter y un fichero de bloqueo dejan de versionarse; `.gitignore` ampliado. | raíz |

Tras los cambios el manual compila sin errores ni referencias rotas.
**Los PDF de `pdfs/` no se han regenerado.**

### Solucionario (`onlyforyoureyes`)

- `raices.py`: `regula_falsi` estaba sangrada **dentro** de `biseccion`, después
  del `return`: era código inalcanzable y no se podía importar.
- `sistemas.py` (dos copias): mismo problema de truncamiento con enteros.
  Con `A=[[3,1,2],[1,4,1],[2,1,5]]`, `b=[1,2,3]`, `gaussSolve` devolvía
  `[0 0 0]` en lugar de `[-0.2 0.4 0.6]`. Corregido y verificados los 11
  métodos frente a `numpy.linalg.solve`.
- Tres notebooks de `introduccion/` tenían **marcas de conflicto de merge sin
  resolver** (no se podían abrir en Jupyter). Los conflictos eran sólo de
  metadatos y se han resuelto sin pérdida de contenido.
- Imports que faltaban en tres notebooks; `rc.secant` → `rc.secante`.

### Revisión a fondo por capítulos

| Capítulo | Estado | Notas |
|---|---|---|
| 2. Introducción a Python (`introprog.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 3. Introducción a Numpy (`intronumpy.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 4. Introducción a Matplotlib (`matplotlib.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 5. Aritmética del computador (`aritmetica.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 6. Cálculo de raíces (`calraiz.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 7. Sistemas de ecuaciones lineales (`sistemas.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 8. Interpolación y ajuste (`interpolacion.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| 9. Diferenciación e integración (`integracion.tex`) | **Revisado** (nov 2026) | Ver detalle abajo. |
| Resto | Pendiente | Solo han pasado la revisión automática (sección anterior). |

**Capítulo 2: qué se ha hecho**

*Errores de contenido corregidos*
- `h=(c1^2+c2^2)**(1/2)`: en Python `^` es XOR bit a bit, no la potencia.
  No da error, da 2.6458 en lugar de 5 para catetos 3 y 4. En la fórmula
  de la ecuación de segundo grado faltaba además el 4 (`b^2-a*c`).
- `R=5*3-6/3+2**3+2-4` vale 19.0, no 17. `2+4/2` imprime `4.0`, no `4`.
- `//` no redondea hacia cero, sino hacia −∞ (`-7//2` da `-4`).
- Tabla de operadores relacionales: las descripciones inglesas de `>=` y `<=`
  estaban intercambiadas.
- **Ámbito de las variables (regla LEGB)**: el texto lo explicaba como si
  dependiera de qué función *llama* a cuál ("el namespace de `soleq2`
  encierra al de `print`"; global = "el módulo que ha llamado a la
  función"). En Python el ámbito es léxico: depende de dónde está
  *definida* la función. Reescrito con un ejemplo de función anidada.
- `primos.py`: el contador del `while` se sobrescribía con el `for i in
  primos`; `numpr(10)` devolvía 6 primos. Corregido, y la versión con el
  fallo se usa ahora como ejercicio de depuración.
- Conjuntos: no son inmutables (se les pueden añadir elementos); lo que
  impide `C[1]=23` es que no son indexables.
- `L.count()` no cuenta elementos de la lista, sino las apariciones de un
  elemento. El modo `'w'` borra el contenido del fichero (no se decía).
- Coherencia entre ejemplos: los valores de `L`, `D['día']`, la ecuación
  resuelta en el ejemplo de `import`, el número buscado en
  `listadelistas`, `c = -3,2` (creaba una tupla).
- Números de línea citados que no correspondían con los scripts incluidos
  (`eq_seg_grado.py`, `numero_parytres_nested.py`, `ejemplo_for.py`,
  `primos.py`) y listados con la etiqueta de otro fichero.
- Ejercicios con el código mal sangrado (no se podían copiar y ejecutar),
  una referencia a una línea 12 inexistente y una sucesión de Fibonacci con
  `F(2)=2`.
- Los errores de ejecución (`AttributeError`) se presentaban como un tipo
  de error de sintaxis.

*Estilo*: unas 300 correcciones gramaticales y de estilo en ambas columnas
(sobre todo falsos amigos y calcos en inglés: *eventually*, *assignation*,
*true table*, *minor than*…).

*Contenido nuevo (primeros pasos de la propuesta)*
- Nota "¡Cuidado con el símbolo ^!" en la sección de operadores.
- Sección nueva **"¿Es correcto mi programa?"** (tras Depuración):
  estrategias de verificación (predecir, casos conocidos, propiedades,
  casos límite), `assert`, y por qué comparar reales con `math.isclose` y
  no con `==`, usando los propios ejemplos del capítulo.
- Cuatro ejercicios nuevos: *depura este código* (primos), *primero las
  comprobaciones* (potencia), *¿cuál es correcta?* (tres versiones de una
  suma, una con un error de rango que solo cambia la cuarta cifra decimal)
  y uno con un asistente de IA.

*Completado después (nov 2026)*
- Ejercicios traducidos: sección *Exercises* tras la española (mismo
  formato que `integracion.tex`), con los mismos bloques de código.
- Depurador: las capturas muestran una copia de `eq_seg_grado.py` con un
  error intencionado (`/2/b` en la línea 28) y dos líneas de comentario más.
  Esa copia está ahora en `codigos/introduccion/eq_seg_grado_error.py`
  (reproduce exactamente la consola de la figura: 0.222 y 0.0), y el texto
  lo explica. Ya no desvela la línea del error: parte de que la comprobación
  falla y deja que el depurador lo localice.
- Pies de figura de Anaconda bilingües.

*Decisión*: **se mantiene Spyder** como entorno principal (IDE sencillo al
empezar; con el plug-in `spyder-notebook` también se trabaja con
notebooks). Las capturas son de Spyder 5.4 / Python 3.11 y siguen siendo
válidas. Cuando se rehagan con Spyder 6, aprovechar para corregir
"Get into de function" en `depu2.png`.

**Capítulo 3: qué se ha hecho**

Revisión completa de las dos columnas (unas 500 correcciones), con todos
los cálculos y ejemplos comprobados con Numpy/Scipy.

*Errores de contenido corregidos*
- Determinante $2\times 2$: el desarrollo daba $-a_{11}a_{22}+a_{12}a_{21}$
  (el signo contrario); el desarrollo por la segunda columna tenía
  $a_{22}a_{12}$ en lugar de $a_{22}a_{11}$. Un menor del ejemplo $3\times 3$
  tenía un elemento mal copiado.
- Diagonalización de la matriz $G$: el autovector dado para $\lambda=1$ no lo
  era, y la matriz $X$ no tenía como columnas los autovectores (el producto
  $XDX^{-1}$ no daba $G$). Rehecha con $x_3=[-1,0,2]^T$.
- Diagonalización ortogonal: $A=QAQ^T$ → $A=QDQ^T$. "Diagonalizable
  ortogonalmente si es normal" era incorrecto para matrices reales (es si y
  solo si es simétrica; las normales lo son mediante matrices unitarias).
- Normas 1 e ∞ de matrices: faltaban los valores absolutos y los límites
  de los sumatorios estaban mal. Las normas 1, 2 e ∞ se presentaban como
  algo distinto de las normas inducidas (lo son).
- Matrices triangulares: las condiciones de triangular y estrictamente
  triangular estaban intercambiadas.
- Producto matricial: fórmula con $a_{ij}$ en lugar de $p_{ij}$; notación
  de filas/columnas incoherente con las dimensiones; en inglés decía que
  las columnas de la primera deben coincidir con las *columnas* de la
  segunda.
- Inglés: "simétrica" traducida como *antisymmetric*, y $A=A^T$ como
  condición de antisimetría.
- Indexación: la línea [11] extrae la segunda columna, no la primera; la
  [95], la última, no la primera. El "slicing" no se detiene en `stop-step`
  sino en el último valor anterior a `stop`.
- Formas cuadráticas: dependen de $a_{11}$ y $a_{22}$ (no $a_{12}$) y dan
  paraboloides elípticos o hiperbólicos (no hiperboloides).
- Ejemplo de inversa: se invertía una matriz que no aparecía en el texto.
  Elemento neutro $I\cdot A$ sin resultado; `np.mod` al revés en la tabla;
  `matrix.power` → `matrix_power`; pie de figura $a-b+c$ → $a-0.5b+c$;
  `(4\time2)` (asignaba un registro de TeX sin imprimir nada).
- "Describir la factorización LU queda fuera de estos apuntes": se hace en
  el capítulo de sistemas; ahora se remite a él.
- Ejercicios: el 2 usaba `any(M<2)` (falla con `import numpy as np`, que
  es lo que el texto recomienda); varios usaban `ones`, `eye`, `array` sin
  `np.`; restos de MATLAB (`SumoDiag.m`).

*Código*
- `cambio_vb.py`: rechazaba como "no independiente" cualquier base con
  determinante negativo (`det(B) < eps` sin valor absoluto). Ahora usa
  `matrix_rank`, y dibuja los vectores con su tamaño real (antes todos
  normalizados a 0.1).
- `inversa.py`: la fórmula del comentario multiplicaba por el determinante.
  Comentarios de `determinante.py` corregidos.

*Contenido nuevo (verificación)*
- Nota tras `det`: por qué da 20.000000000000007 y cómo comparar
  (`isclose`, referencia a la sección de verificación y al capítulo de
  aritmética).
- Tras la inversa: comprobar con `np.allclose(B@A, np.eye(3))` y aviso de
  que `inv` de una matriz singular puede devolver, sin error, una "inversa"
  con elementos de 10^16.
- Tras LU: la línea `P@L@U` como comprobación; el determinante con
  permutación ($\vert P\vert=\pm 1$).
- Cholesky como prueba práctica de "definida positiva"; norma −∞ (no es
  una norma); coste factorial del determinante recursivo.
- Ejercicios nuevos: *depura este código* (producto de matrices que solo
  funciona con matrices cuadradas), *comprueba las propiedades* (con
  matrices aleatorias), *¿es de verdad la inversa?* (matrices de Hilbert y
  número de condición) y uno con IA (autovalores 2×2, que suele fallar con
  autovalores complejos).
- Ejercicios traducidos al inglés.

**Capítulo 4: qué se ha hecho**

Reescritura completa de las dos columnas, con todos los ejemplos
ejecutados (Matplotlib 3.8) y las figuras comparadas con el código.

*Errores de contenido corregidos*
- Tabla de marcadores: `^` (triángulo hacia arriba) y `v` (hacia abajo)
  estaban intercambiados en los dos idiomas; `*` es una estrella.
- `fig = plt.figure` y `plt.figure` sin paréntesis: no creaban ninguna
  figura (guardan la función). Ahora es además una nota de aviso.
- `plt.text(..., '$x=e^{-t}\cos(...)$')` sin `r''`: secuencia de escape no
  válida (aviso de Python). Nota sobre las cadenas en bruto.
- Espiral polar: el texto decía $r=2\sqrt{\theta}$; el código y la figura
  son $r=2\theta$.
- Histograma: el texto decía 10, 5 y 10 intervalos (el código usa 20);
  argumento `bin` → `bins`; pie de figura inglés vacío. Lectura con
  `np.loadtxt` en lugar del bucle manual.
- Superficies: llamaba "matrices de adyacencia" a las matrices de
  coordenadas de `meshgrid` (en teoría de grafos es otra cosa). Añadido
  el orden de `meshgrid(x, y)`: forma `(len(y), len(x))`, `Z[i,j]` ↔
  `(x[j], y[i])`.
- Sesiones de IPython con `Out[24]:` delante de las entradas, numeración
  incoherente y sangrías que impedían ejecutar los bloques.
- `contourf`/`pcolor`: el texto citaba `pcolor` y el código usaba
  `contour`; ahora `contour` + `contourf` con barra de color (figura nueva
  `plt_contour.png`).
- Animación: faltaba `import matplotlib.animation`; el texto decía
  `.mpg` y el código `.mp4`; dependía de `ffmpeg`, que no viene con
  Anaconda en Windows. Ahora usa `PillowWriter` (GIF, sin dependencias) y
  menciona `FFMpegWriter` y `FuncAnimation`.
- Ejercicios: $P_2=(0.5,\sqrt2/2)$ no forma un triángulo equilátero
  (√3/2); $v_x$ repetida (era $v_y$); `dibujaMUC` → `dibujaMCU`;
  "retícula cuadrada" en una región rectangular; "comando mesh" (MATLAB);
  `np.random.randn` → `default_rng`; paréntesis desequilibrados.
- Test 2020/21: "ocho subplots" (son 16), frecuencias "en rad/s" dentro de
  $2\pi\omega t$ (son s⁻¹), "movimiento en el plano" (es en el espacio),
  autorreferencia "apartados c) y d)" dentro del d).
- `precip.dat` no estaba en el repositorio del manual (solo en el
  solucionario): copiado a `datos/`, junto con `coches.dat`.

*Contenido nuevo*
- Para qué sirve una gráfica en el curso (entender y convencer); figuras y
  `Axes`; dónde aparecen las figuras en Spyder; `legend`, argumentos con
  nombre, `savefig`.
- Sección **"Dos formas de trabajar: pyplot y objetos"** con tabla de
  equivalencias (`plt.xlabel` ↔ `ax.set_xlabel`) y aviso de que mezclarlas
  da `AttributeError` (error típico del código generado por IA).
- Escalas logarítmicas: rectas en semilog (exponenciales) y log-log
  (potencias, pendiente = exponente); `log 0` se descarta sin avisar.
- Sección **"Gráficas para verificar un resultado"**: lista de comprobación
  de una figura defendible; medir el orden de un error en log-log
  (diferencia hacia delante, pendiente 1 y error de redondeo para
  h < 1e-8, figura nueva `plt_error_h.png`); "una gráfica no es una
  prueba".
- Ejercicios nuevos: *depura este código* (tiro parabólico con grados y un
  `*t` olvidado), *¿cuál es correcta?* (tres formas de rellenar Z; la de
  los bucles falla en silencio con mallas cuadradas), *mide el orden*
  (diferencia centrada) y uno con IA (superficie y curvas de nivel con
  comprobaciones previas). Verificación final añadida al de
  precipitaciones. Ejercicios traducidos al inglés.
- `\mintinline` sustituido por `\texttt` (con comilla recta, que se puede
  copiar del PDF) para que no se salga de las columnas.

*Solucionario (`onlyforyoureyes/matplotlib`)*
- `04_Ejercicio_Aplicado.ipynb`: **la solución era incorrecta**. Con
  `limite=1000`, 1998 (diferencia 690) se trataba como error de tipo b, y
  `meses[i,0:j-1]` dejaba fuera el mes anterior al erróneo (1985 quedaba
  con 102.5 en lugar de 72.5). Corregido, con `assert` final, y
  regenerado `precip_corregido.dat`. Es el ejemplo de "una gráfica no es
  una prueba" del texto.
- `EjerciciosLibro.ipynb`: tiro parabólico sin `*t`; MCU con
  `np.array([0,1,0.1])` (3 puntos); `np.arange(-1,1-0.1)`; `range(n)` en
  lugar de 1…n; juego del caos con `(P[i]-P)/2` (no es el punto medio) y
  √2/2. Todo corregido y ejecutado.
- `matplotlib.ipynb`: `ax3.meshgrid` → `ax3.contour` con barras de color;
  la última celda (respuesta de un chatbot pegada tal cual) tenía
  `plt.pause()` sin argumento y `set_data` con escalares. Corregidos con
  un comentario; puede servir de ejemplo real para un ejercicio de
  "critica el código de la IA".
- Se ha confirmado la salida de `big_brother/` (se ignora en adelante) y
  se han borrado los `.p` de MATLAB (decisión de nov 2026: hay copia en
  otro sitio).

**Capítulo 5: qué se ha hecho**

Reescritura completa de las dos columnas (el inglés tenía errores en casi
cada párrafo), con todas las cifras comprobadas en Python (`struct`,
`np.float32().view`, `decimal`, `fractions`).

*Errores de contenido corregidos*
- **Orden de los campos IEEE 754**: todas las tablas ponían
  signo | mantisa | exponente; el estándar guarda signo | exponente |
  mantisa (comprobado con los bits reales). Reordenadas las 16 tablas,
  incluida la del ejemplo de 16 bits.
- Mantisas de 22 bits en lugar de 23 en cuatro tablas (y de 51 en lugar
  de 52 en precisión doble); un exponente de 9 bits.
- Ejemplo 2 de IEEE: mantisa "= 0.25" y "0.25 × 2² = 5.0" (es 1.25).
- Notación científica: 234.25 ≠ 2.345×10², 0.000234 ≠ 2.34×10⁻⁵.
- Desplazamiento del punto con el exponente al revés (exponente 1 →
  a la derecha, no a la izquierda).
- Suma de ejemplo: el texto daba 100.152 como resultado exacto (es
  100.151) y lo usaba en el error relativo.
- **Anulación catastrófica**: con la mantisa de 5 dígitos que dice el
  texto, b²−4ac da 1.0000·10⁻³ (error del 102 %), no 5.0000·10⁻⁴ (1 %, que
  corresponde a 6 dígitos). Reescrito: el ejemplo es ahora mucho más
  convincente.
- Axioma fundamental con |δ| ≤ eps, incoherente con la cota eps/2 que el
  propio capítulo deduce. Ahora eps/2, y se explica que IEEE 754 exige
  redondeo correcto (los dígitos de guarda son el medio, no la norma).
  Añadido el redondeo al par.
- NaN descrito como "error de desbordamiento" en precisión doble; tabla
  resumen con `m_23·2^-52` y `e_8·2^8` (es 2^7).
- Historia del estándar: fechas incoherentes entre idiomas (1976/1974),
  "Kahan (Intel)", "hasta los años noventa". Corregida (Intel/8087 en 1976,
  comité en 1977, aprobación en 1985, revisiones 2008 y 2019, premio Turing
  1989).
- Avogadro: "9 de sus 23 cifras" (son 24) y valor anterior a 2019.
- Frase española duplicada fuera de `paracol`; "3. normalización" sin
  columna inglesa; índices `\index[eng]` en la columna española; cita de
  Kipling ("Not rivet" → "No rivet").
- `norm_naive.py`: `norma_robust` fallaba con un vector de ceros
  (`UnboundLocalError`). Corregido; las sesiones del texto ya no muestran
  rutas de `/home/juan` y se ejecutan (importan el módulo).

*Contenido nuevo*
- Desbordamiento silencioso en complemento a dos (7+1 = −8 con 4 bits).
- `np.linalg.norm` también desborda con el vector del ejemplo;
  `math.hypot` no.
- Sección **"La aritmética del ordenador en Python"**: `np.finfo`,
  `0.1+0.2 != 0.3` y `Fraction(0.1)`, bucle `while x != 1.0` que no
  termina, `np.spacing`, ver los bits con `view(np.uint32)` (comprueba los
  ejemplos del texto), enteros de Python frente a NumPy (`int8`, 21! con
  `int64` da un negativo sin aviso; nota sobre `int32` en Windows con
  NumPy < 2), `inf`/`nan`, `math.fsum`, `float32`/`float16` (redes
  neuronales).
- Sección **"Error de redondeo y error de truncamiento"**: explica y
  *predice* el mínimo en h ≈ √(2 eps) de la figura de la diferencia hacia
  delante del capítulo 4.
- **Ejercicios** (el capítulo no tenía ninguno), en los dos idiomas: IEEE a
  mano y con Python; complemento a dos con predicción; épsilon del
  computador; anulación en (1−cos x)/x²; *depura este código* (combinaciones
  con `np.prod`, da −3 en lugar de 4060); *¿cuál es correcta?* (tres
  fórmulas de la ecuación de segundo grado, verificación con Vieta);
  *predice y mide* (h óptimo de la diferencia centrada ∝ eps^(1/3)); y uno
  con IA (norma de un vector con las pruebas escritas antes de pedir el
  código).
- Solucionario: `onlyforyoureyes/aritmetica/EjerciciosLibro.ipynb` (nuevo),
  con las soluciones de todos los ejercicios comprobadas con `assert`.

*Herramientas*
- El corrector ortográfico funciona en Linux con los diccionarios del
  sistema (`hunspell-es`, `hunspell-en-us`); instrucciones en
  `tools/README.md`. Pasado a los capítulos 4 y 5.


**Capítulo 6: qué se ha hecho**

Reescritura completa de las dos columnas, con todas las cifras del texto
recalculadas (número de iteraciones de cada ejemplo, salidas de Python).

*Errores de contenido corregidos*
- **Polinomio con los coeficientes al revés**: el texto decía calcular las
  raíces de $x^3-6x^2+11x-6$ con `P([1,-6,11,-6])`, que es
  $1-6x+11x^2-6x^3$; las raíces impresas (1/3, 1/2, 1) eran de ese otro
  polinomio. Corregido y convertido en aviso: `Polynomial` usa orden
  ascendente y `np.roots`/`np.polyval`, descendente, y el error es
  silencioso.
- `P([0,6,2,0,3],[-2,2])`: el segundo argumento (*domain*) no es el
  intervalo de dibujo; reescala la variable (en $x=2$ da 11 en lugar de 68).
  Ahora `p.linspace(domain=[-2,2])`, con aviso.
- La raíz doble de $(x+1)^2$ ya no sale "−1.00000001, −0.99999999" con NumPy
  actual; sustituido por $(x-1)^3$ (error ~7e-6 ≈ eps^(1/3)).
- **Bisección con precisión máxima**: el diagrama de flujo del libro, sin
  comprobar $f(c)=0$, da un resultado erróneo con la propia función del
  ejemplo: en la iteración 47 $f(c)$ vale exactamente 0, `f(a)*f(c)<0` falla
  y el intervalo abandona la raíz (256 números máquina). Diagrama corregido.
  La fórmula del número de iteraciones usaba `eps` (vale solo para raíces en
  [1,2)); ahora usa `np.spacing(r)`.
- Recuentos de iteraciones: Newton desde 2.5 necesita 6, no 5; el punto fijo
  con $-\sqrt{e^x}$, 8, no 5; con $\ln(x^2)$ desde −0.2 no son 211 de forma
  reproducible (en nuestra prueba, 5163): es caótico y depende del redondeo;
  convertido en lección.
- Bisección: "si hay más de una raíz el algoritmo puede no converger" (falso:
  converge a una de ellas); la relación entre cambio de signo y número impar
  de raíces se precisa (multiplicidad).
- Punto fijo: $x^2$ también alcanza 1 desde $x_0=-1$; añadido $|g'|$ en cada
  ejemplo (0.35, 2.84, 1.70) para explicar convergencia y divergencia.
- `fsolve`: el ejemplo decía partir de 2 y partía de −2; "oír" → "por".
- Ejercicio de la secante: pedía la derivada (el método no la usa). Ejercicio
  de Steffensen con pseudocódigo `while condición` (no ejecutable): ahora
  fórmula. Maxwell: $f$ es una densidad (s/m), no una probabilidad.
- Kepler (ejercicio aplicado): **$x=a\cos E-e$ es dimensionalmente
  incorrecta** ($x=a(\cos E-e)$); $M$ es la anomalía *media*, no la
  "verdadera". Test 2024-25: $y_0$ no definido ($h_0$). Test 2020/21: el
  enunciado pedía escribir $e(t)=t-g(t)$; ahora se define $f(t)=e(t)-d$
  ($d$ = 1 miliparsec) y se escribe $f(t)=t-g(t)$ (opción elegida por el
  profesor). **El solucionario antiguo (`raices/Test2020_21.ipynb`) tenía mal
  las constantes y daba 1.64 días; lo correcto es 2.54 días** (t ≈ 219 737 s,
  17 iteraciones con $t_0=1$, tol 0.1). Corregido y verificado con `brentq`.
- Desigualdad $|f(r_0)|\ge|f(r_1)|\ge\cdots$ eliminada (no es cierta en
  general); `\text(tol)`; figura con `{h}`; subfigura repetida
  (`p3fijo3.pdf` dos veces); `\alph{enumii}` suelto; sección inglesa de
  ejercicios titulada "Problems".

*Contenido nuevo*
- **Criterios de parada**: residuo, error absoluto y relativo, número máximo
  de iteraciones; cuándo falla cada uno ($(x-1)^3$, raíces grandes o
  pequeñas).
- Predicción del número de iteraciones de la bisección; regula falsi lenta
  con $x^{10}-1$ (87 frente a 29); ciclo de Newton en $x^3-2x+2$.
- Sección **"Orden de convergencia"**: definición, tabla de órdenes, y código
  que mide el orden de Newton (cifras correctas 1→3→6→13).
- `root_scalar` (Brent) como opción recomendada; `fsolve` devuelve un
  número aunque no converja ($x^2+1$ → −2e-12, con un simple aviso).
- Ejercicios nuevos: *¿cuál es correcta?* (tres pruebas de signo en la
  bisección: el producto falla con $f(c)=0$ y con *underflow*), *mide el
  orden* (incluida la raíz doble y Newton modificado), *depura este código*
  (la bisección de precisión máxima sin comprobar $f(c)=0$) y uno con IA
  (ecuación de Kepler con pruebas previas). Los ejercicios de implementación
  piden ahora `assert`, errores explícitos y predicciones.
- Solucionario: `onlyforyoureyes/raices/EjerciciosLibro.ipynb` (nuevo), con
  todos los ejercicios del libro resueltos y comprobados.

**Capítulo 7: qué se ha hecho**

Reescritura completa de las dos columnas. Todas las salidas del texto se
han regenerado ejecutando el código y comparándolas literalmente con lo
impreso (las que dependen de la plataforma, p. ej. el texto de los
`RuntimeWarning`, corresponden a NumPy 1.26). **Ningún bloque de código del
capítulo se podía ejecutar tal como estaba** (salidas mezcladas con el
código, fragmentos sueltos, docstrings sin cerrar).

*Errores de contenido corregidos*
- **Jacobi en forma matricial: el texto construía `f = inv(A) @ b` y
  `H = -inv(A) @ (U+L)`** en lugar de `inv(D)`.
- **Código del método SOR: `xs1 = w*xs1 + (1-w)*xs` dentro del bucle** sobre
  las componentes (promedia el vector entero en cada pasada). No da ningún
  error: converge a una solución equivocada o diverge. Corregido
  (`xs1[i] = ...`) y convertido en el ejercicio *¿cuál es correcta?*
  (el `sistemas.py` del solucionario ya estaba bien).
- Forma matricial de SOR: $f=\omega(D+\omega L)^{-1}$ (faltaba $b$).
  Gauss-Seidel: "multiplicando por la inversa de $D+U$" ($D+L$).
- Ejemplo de eliminación de Gauss: $-2.6$ en lugar de $-8/3$, un $3$ que se
  convertía en $-3$, la matriz $U_2$ mostrada sin actualizar; ahora con
  fracciones exactas y comprobado con `eligauss`.
- Gauss-Jordan: "restar columnas" donde se restan filas; la matriz de partida
  no era la del ejemplo anterior (ahora se dice que es otra).
- Ejemplo de Jacobi $2\times2$: "$5-3x_2$", "$7-3\cdot1.67$".
- Espectro de Jacobi calculado con $H=+D^{-1}(L+U)$ (signo); autovalores
  impresos corregidos.
- "Para converger, $H$ tiene que tener norma 2 menor que uno" (es
  suficiente, no necesario; el criterio es $\rho(H)<1$, ahora "si y solo
  si"). La ecuación $\lVert x^{(s+1)}-x^{(s)}\rVert\le C\Rightarrow\lVert
  x^{(s+1)}-x\rVert=\vert e\vert$ no tenía sentido.
- "Cualquiera de los métodos converge si la matriz es estrictamente diagonal
  dominante": cierto para Jacobi y Gauss-Seidel, y para los amortiguados
  solo con $0<\omega\le1$. Gauss-Seidel "converge más deprisa" (en
  general, no siempre).
- SVD: la función devuelve los *valores singulares*, no los autovalores;
  variable `V` que en realidad era $V^T$. Ortogonal: $Q^T=Q^{-1}$ (decía
  $A^T=A^{-1}$). "Multiplicarla por el vector de coeficientes para obtener
  el vector de términos independientes" (al revés).
- Columna inglesa: ecuaciones corrompidas en la SVD (`A=U=U{sec:SVD}, S=V^T`),
  `x^Tdot`, `cdots`, `L^T z=b` (es $L z=b$), $U^T U^T$, "row echelon form"
  (es *reduced*); faltaba toda la sección de ejercicios en inglés.
- Epígrafe con un solo argumento (Szymborska, *Fin y principio*); figura 1 cm
  más ancha que la página; minipágina del circuito desbordada.
- Ejercicio del circuito: "usa $P\cdot A$" (con la $P$ de SciPy es
  $P^T\cdot A$).

*Contenido nuevo*
- Condicionamiento: tabla del número de condición frente a la solución,
  significado (cota del error relativo) y la regla "se pierden
  $\log_{10}\kappa$ cifras", comprobada con la matriz de Hilbert;
  **un residuo pequeño no garantiza una solución buena**; el determinante no
  mide el condicionamiento.
- Coste de cada método ($n^2$, $2n^3/3$) y por qué no se invierte la matriz.
- `lu_factor`/`lu_solve` (factorizar una vez, resolver muchas).
- Sección **"Pivoteo"**: pivote nulo (NumPy sigue con `nan` e `inf`),
  pivote pequeño ($10^{-20}$: $x_1=0$ sin aviso con un sistema bien
  condicionado); la eliminación de Gauss con pivoteo **es** la factorización
  LU (multiplicadores = $L$, comparados con SciPy).
- Sección **"Resolver sistemas con NumPy y SciPy"**: `solve`,
  `solve_triangular`, `assume_a='pos'`, no usar `inv`, y una lista de
  verificación (condición, residuo, otro método, sentido físico).
- Métodos iterativos: funciones completas y ejecutables, que lanzan un error
  si no convergen; cada forma matricial se comprueba con `assert` frente a la
  de bucles. Sección **"Criterio de parada"** (cuerda con $n=20$: paso
  $<10^{-5}$ pero error $9\times10^{-4}$) y estimación
  $e\approx\rho/(1-\rho)\cdot$paso. Predicción del número de iteraciones
  con $\rho$ (22.8 y 11.7 frente a 23 y 13 reales).
- Ejercicios: los antiguos reescritos (con `assert`, errores explícitos y
  predicciones) y nuevos: *¿cuál es correcta?* (tres SOR), *depura este
  código* (Gauss que modifica la entrada y trunca enteros: la comprobación
  `allclose(A @ x, b)` da `True` con una solución errónea), condicionamiento
  (Hilbert), *predice y mide el coste*, y uno con IA (algoritmo de Thomas para
  sistemas tridiagonales, con las pruebas escritas antes).
- `tools/check_blocks.py --prelude`: permite ejecutar los bloques que usan
  `regressive` (ejercicio del libro) sin publicar su solución; el preludio
  está en `onlyforyoureyes/sistemas_lineales/prelude_check_blocks.py`.
- Solucionario: `onlyforyoureyes/sistemas_lineales/EjerciciosLibro.ipynb`
  (nuevo), con todos los ejercicios resueltos y comprobados con `assert`. El
  antiguo `07Ejercicios_sistemas.ipynb` se conserva.

*Sin cambiar (para revisar)*
- Los tests 2020/21 y 2024-25 solo se han corregido de forma (erratas,
  unidades). El Test 3 de 2024-25 incluye un ejercicio de interpolación
  ("Newton-Gregory o diferencias finitas": son el mismo método; quizá se
  quería decir "Lagrange o Newton"). Las figuras `gjcom` y `comjjam` no se
  han regenerado (sus datos coinciden con el texto: 23/13 iteraciones).

**Capítulo 8: qué se ha hecho**

Reescritura completa de las dos columnas (la inglesa tenía restos como
"8DWM1001 degree" y `$x-= =1$`), revisión de los programas de
`codigos/interpolacion/` y salidas del texto regeneradas.

*Errores corregidos*
- **Ejercicio 1: el fichero de datos era otro.** `datos/datos.txt` tiene 201
  puntos (interpolarlos con Vandermonde da $\kappa\approx10^{20}$); el
  solucionario usaba los 10 datos de la figura, que solo estaban en
  `codigos/interpolacion/interpolacion.txt`. Copiado a
  `datos/interpolacion.txt`; `datos.txt` ($y=20x+3x^3$ con y sin ruido) pasa al
  ejercicio de mínimos cuadrados.
- **`difdiv` y `newgre` truncaban sin aviso con datos enteros** (`y.copy()`):
  con la tabla del propio libro daban $1,-2,1,0$. Ahora `astype(float)`;
  `newgre` lanza un error si los datos no están equiespaciados. Convertido en
  ejercicio de depuración.
- **`dbez` multiplicaba por $n-1$ en lugar de $n$** (derivada de Bézier).
  *La figura `bezierhodg.eps` se generó con el código erróneo: la hodógrafa
  está escalada por $(n-1)/n$; habría que regenerarla* (no se conocen los
  puntos de control usados).
- `evspc` fallaba (`IndexError`) fuera del último dato y solo admitía un
  punto: ahora `np.searchsorted`, vectorizada. `lse`: comprobación del número
  de datos ($m<n$ en vez de $m<n+1$) y `w='none'`.
- `CubicSpline(x, y, 'natural')` (el tercer argumento es `axis`: da error);
  `'not__knot'`; `scipy.interpolation`; `interp1d` "de numpy".
- Bézier: $\vec p_2^{+}$ de la curva elevada de grado usaba $\vec p_2,\vec p_3$
  (es $\vec p_1,\vec p_2$); conjunto de puntos sin $\vec p_1$; índices.
- Splines: índices de las condiciones de continuidad, $h_i$ por $h_{i-1}$ en
  $S_{i-1}(x_i)$, condición periódica.
- Vandermonde: "$n$ ecuaciones" ($n+1$). Taylor: "el error disminuye con el
  grado" (falso fuera del radio de convergencia: en $x=2.5$ el de grado 40 se
  equivoca en $10^5$). Leyendas de figuras (seno 3, 5, 7, 9) y subfiguras más
  anchas que la columna.
- Test 2020/21: referencias cruzadas a las etiquetas inglesas, "52 ángulos"
  (son 51), "apartado 2a/3b", "comando de Numpy" (es SciPy).

*Contenido nuevo*
- Convergencia de la serie de Taylor (radio de convergencia, con números).
- Condicionamiento de la matriz de Vandermonde (tabla) y por qué
  `Polynomial.fit` no resuelve las ecuaciones normales
  ($\kappa(V^TV)\approx\kappa(V)^2$; con grado 9 y 10 datos, `lse` deja un
  residuo $10^{10}$ veces mayor); `.coef` frente a `.convert().coef`.
- Sección **"Error de interpolación y fenómeno de Runge"**, con nodos de
  Chebyshev y figura nueva (`figuras/runge.pdf`).
- Orden del error medido: interpolación lineal $h^2$, spline $h^4$.
- `np.interp` como opción recomendada; `interp1d` señalada como *legacy*
  (medida H de la propuesta).
- Ejercicios nuevos: Runge (*predice y mide*), orden del spline natural con
  $\cos x$ (*mide el orden*: sale 2, no 4), *depura este código* (`difdiv`
  antigua), *¿cuál es correcta?* (pesos en `fit` y en `lse`) y uno con IA
  (ajuste exponencial linealizado: transformación de las incertidumbres).
- Solucionario: `onlyforyoureyes/interpolacion/EjerciciosLibro.ipynb`
  (nuevo). Al resolverlo salen dos matices útiles para clase: con el ruido
  de `datos.txt` el término cúbico apenas se distingue, y el ajuste
  logarítmico con pesos tiene un pequeño sesgo frente a `curve_fit`.
- `integracion.tex` tenía el capítulo sin etiqueta: añadida
  `\label{ch:integracion}`.

**Capítulo 9: qué se ha hecho**

Reescritura completa de las dos columnas (la inglesa tenía muchas erratas:
*worming*, *Nunerical*, *sprint*, *base on*\ldots), revisión de los
programas de `codigos/diferenciacion_integracion/` y figuras nuevas
generadas con los propios programas.

*Errores corregidos*
- **Tabla de fórmulas de diferencias finitas**: la segunda derivada
  adelantada de orden $h^2$ tenía $+y_2$ en lugar de $+4y_2$ (la fórmula
  impresa ni siquiera aproxima $y''$); `2yx_{-1}` en la tercera derivada; a
  la centrada de la segunda derivada le faltaba $O(h^2)$. Todas comprobadas
  con un desarrollo de Taylor simbólico.
- Diferencia adelantada de tres puntos: el término de error tenía el signo
  cambiado ($+\frac{h^2}{3}f'''$) y la deducción, una errata (`2{h^2}{2}`).
- Ejemplo de Newton-Gregory: el texto decía que añadir diferencias hace la
  derivada "cada vez más precisa", pero las cuatro estimaciones oscilan
  (1.015, 0.9725, 1.0125, 0.9875). Los datos son $\tan x$ redondeada: la
  derivada exacta es 1, y con los valores exactos de $\tan x$ pasa lo mismo
  (es el fenómeno de Runge en el extremo del intervalo). Reescrito como
  ejemplo de verificación.
- Ejemplo de `quad`: `inte.quad` con el módulo importado como `integ`
  (`NameError`).
- **Figuras del amortiguador: la leyenda estaba intercambiada** (la curva
  marcada como velocidad era la posición, que tiende a $mg/k$). Además, el
  texto decía que la primera figura era con $k=100$ (era $k=10$), y que el
  código mostrado tenía $k=100$. Las tres figuras se han sustituido por una
  (`amortiguador_euler.pdf`) generada con el código del texto.
- `Euler_method.py` y `midpoint_method.py`: `np.arange(a, b+h, h)` da a
  veces un elemento de más (177 de 1194 combinaciones probadas de $b$ y $h$),
  y entonces `t` y `x` tienen longitudes distintas; un valor inicial escalar
  daba `AttributeError` (el texto llamaba `euler(condensador,0,0,10,h)`), y
  dibujaban dentro de la función. Ahora `np.linspace`, `np.atleast_1d` y sin
  gráficas. El texto llamaba además `euler('amortiguador',[0 0],0,50,0.01)`
  (nombre como cadena y sintaxis de MATLAB). El bloque de la función
  `amortiguador` no era Python válido (cuerpo sin sangrar).
- `integrador.py`: código suelto dentro de la *docstring*; método
  desconocido daba `UnboundLocalError` (ahora `ValueError`).
- Paso de integración del condensador: el texto decía $h=0.025$ y la figura
  $0.25$. Fórmula de Simpson 3/8 con $p_2$ en lugar de $p_3$; $e^{-t/R\cdot
  C}$ ambiguo; "el error de redondeo hace que haya un $h$ óptimo" en Euler
  (cierto en teoría, irrelevante en doble precisión: reescrito).
- Ejercicios: $d^2\theta/dt$ (faltaba el cuadrado), `pi/6`, "tomo",
  $\int\sin x$ sin $dx$.
- Test 2020/21: unidades de $\mu$ (con la fuerza $\mu|N|v$, $\mu$ tiene
  unidades de s/m, no kg/s); referencias `\ref{p1}` a párrafos sin número
  (sustituidas por "apartado 1"), una con la etiqueta inglesa y otra sin
  barra (`ref{p1}`); "gráfico del apartado 3.b)" (es 3.a); $v_x(t(t))$. La
  solución analítica se ha comprobado con `solve_ivp` (diferencia
  $2\times10^{-12}$).
- Test 2024-25: unidades ($g=9.8$ m/s, Kg), tildes; `\section*` como en
  los demás capítulos.

*Contenido nuevo*
- **"Truncamiento frente a redondeo: el paso óptimo"**: $E(h)$, $h_{opt}$
  ($\sqrt\epsilon$ y $\epsilon^{1/3}$), tabla medida y figura nueva medida
  (`errores_derivada.pdf`, sustituye al esquema `errores.eps`).
- `np.gradient` y la amplificación del ruido al derivar datos (ruido de
  $3\times10^{-3}$ → error de $6\times10^{-2}$).
- Fórmulas del error de trapecio y Simpson, Simpson exacto para cúbicas,
  pesos negativos de Newton-Cotes, **orden medido** (cocientes 4 y 16) y
  error predicho con la fórmula.
- `quad` puede fallar con seguridad aparente: un pico estrecho da
  $4\times10^{-70}$ con error estimado $8\times10^{-70}$ (la integral es
  $\sqrt\pi$); `points`. `trapezoid`, `simpson` y `cumulative_trapezoid`
  para datos.
- Euler: orden 1 medido con el condensador; **estabilidad** del
  amortiguador: predicción del paso crítico $h=\mu/k$ y comprobación con
  $h=0.0051$ y $0.0049$ ("estable no quiere decir preciso").
- Sección **"¿Es correcta mi solución?"** (solución conocida, orden,
  conservación, sentido físico, comparación con `solve_ivp`).
- Punto medio con orden 2 medido; RK4 (fórmulas).
- **`solve_ivp`** (medida H): uso, `t_eval`, forma de `sol.y`, y el
  peligro de las tolerancias por defecto (`rtol=1e-3`): un oscilador pierde
  el 1.3 % de la energía en 100 periodos. Métodos y problemas rígidos.
- Ejercicios: los cinco antiguos corregidos y ampliados (con `assert`,
  predicciones y conservación de la energía y del momento angular), y nuevos:
  *predice y mide* el paso óptimo, *mide el orden* ($\sqrt x$: orden 1.5;
  función periódica: el trapecio es exacto con 16 intervalos), *depura este
  código* (Simpson que se salta el último panel: con 101 datos da 1.998,
  que parece razonable, pero el orden medido es 2), *¿cuál es correcta?*
  (tres bucles del oscilador: el único que es Euler gana un 87 % de energía;
  los "mal escritos" son Euler-Cromer) y uno con IA (RK4 con las pruebas
  escritas antes).
- Solucionario: `onlyforyoureyes/diferenciacion_integracion/EjerciciosLibro.ipynb`
  (nuevo), comprobado con `assert`. Matices que salen al resolverlo: los
  $x$ de la tabla del ejercicio de integración están truncados (el paso real
  es $\pi/10$; usar $h=0.3141$ introduce un error comparable al de Simpson);
  con las tolerancias por defecto de `solve_ivp`, la órbita del ejercicio
  del planeta cambia su energía de $-0.755$ a $-3.1$ en $t=100$.

*Sin cambiar (para revisar)*
- Test 2024-25 (**corregido** con el visto bueno del profesor): la fuerza de
  arrastre era $C_d\rho\pi r^2|v|v$, sin el factor $\frac12$ habitual
  ($\frac12C_d\rho A v^2$), y $\rho=1.22$ kg/m$^3$ corresponde a unos 15 °C,
  no a 30 °C (1.16). Ahora lleva el $\frac12$ en las ecuaciones y en
  $F_{rx},F_{rh}$, y dice 15 °C. Se han regenerado `datosLauraLucia.txt` (y su
  copia `datos_Laura_Lucia.txt`) en `onlyforyoureyes`: alcance 28.24 m en vez
  de 23.36 m. **Hay que subir el fichero nuevo al campus virtual.** El balance
  de energía del apartado 4 sigue cuadrando (W = -6915 J frente a ΔE = -6899 J
  con Δt = 1e-3).
- Las figuras antiguas `amortiguador_1/2/3.png`, `errores.eps` y `solrc.eps`
  ya no se usan; no se han borrado.

---

## 2. Pendiente: necesita decisión o revisión humana

1. **`big_brother/`**: el profesor lo ha movido fuera del repositorio
   (nov 2026) y ya no se versiona, pero **sigue en el historial de git**.
   Borrarlo también del historial exige reescribirlo (`git filter-repo`) y
   forzar la subida; solo si se decide.
2. ~~`interpolacion/Test2024_Interpolacion.ipynb`: `t1` sin definir~~:
   resuelto (nov 2026; también truncaba con enteros en `difdiv`).
3. ~~`ax3.meshgrid`~~ y ~~ficheros `.p`~~: resueltos (nov 2026).
5. ~~`codigos/Intro_matplotlib/untitled0.py` y `untitled3.py`~~: borrados
   (nov 2026).
8. **pdfTeX se cuelga (violación de segmento) de forma intermitente** al
   compilar el manual completo en este ordenador (TeX Live 2023 de Debian)
   desde la revisión del capítulo 8: algunas pasadas fallan al escribir una
   página y dejan el `.aux` vacío; la siguiente funciona y da el PDF correcto
   (589 páginas, sin errores ni referencias rotas). No ocurre con el capítulo
   suelto ni con la versión anterior, y no depende de la figura nueva ni del
   índice. Comprobar si pasa también con MiKTeX en el despacho; si pasa,
   investigarlo (quizá probar LuaLaTeX).
   *Actualización (cap. 9)*: el núcleo registra los fallos casi siempre en
   la misma instrucción de pdfTeX (6 de 8 en el desplazamiento `0x5630b`),
   con poca memoria en uso (quedaban ~5 GB libres): es un error del programa
   (lee fuera de un búfer), no falta de memoria ni un fallo del ordenador.
   Ocurre también con la aleatorización de direcciones desactivada
   (`setarch -R`): las pasadas con el `.aux` incompleto terminan, y las que
   leen el `.aux` completo se caen. Con el capítulo 9 nuevo no se ha
   conseguido ninguna pasada limpia del manual completo (sí del capítulo
   suelto, sin errores). Probar con MiKTeX o con otra versión de TeX Live.
6. **La revisión gramatical y de estilo no está hecha.** El corrector sólo
   encuentra palabras mal escritas. El inglés, en particular, tiene muchas
   construcciones calcadas del español que conviene revisar capítulo a
   capítulo.
7. Anaconda: sus condiciones de uso para organizaciones cambiaron en 2024.
   Conviene comprobar si el uso en la UCM está cubierto (el profesor lo
   está consultando, nov 2026). Si no, se puede
   seguir con Spyder sin Anaconda: Miniforge (conda-forge) con
   `conda install spyder spyder-notebook`, o los instaladores autónomos de
   Spyder. Afectaría a la sección 1 del capítulo 2 y a sus capturas.

---

## 3. Propuesta: de "aprender a programar" a "obtener y defender un resultado numérico"

### El diagnóstico

La pregunta de los alumnos ("¿para qué aprender a programar si la IA me lo
hace?") tiene parte de razón: **escribir código ha dejado de ser lo difícil**.
Lo que sigue siendo difícil, y lo que la IA no garantiza, es:

1. **Formular** el problema con la precisión suficiente para que el código
   resuelva lo que hay que resolver.
2. **Saber si el resultado es correcto.** Un código que se ejecuta sin errores
   y da un número no es un código correcto.
3. **Entender el comportamiento numérico**: error de redondeo y truncamiento,
   convergencia, condicionamiento, estabilidad.
4. **Leer y criticar código** que no se ha escrito.

La paradoja es que el contenido de LCC (métodos numéricos *con su análisis de
error*) es exactamente lo que la IA hace mal de manera sutil. La propia
revisión de este material lo demuestra: el truncamiento silencioso con enteros
que devolvía `[0 0 0]`, la función inalcanzable por un sangrado, el orden
ascendente/descendente de los coeficientes de un polinomio o `np.pi` dentro de
SymPy son **los mismos errores que comete un asistente de IA**, y no se
detectan sin entender lo que se está calculando. Ese es el argumento para los
alumnos: *la IA escribe el código; tú eres el responsable de que el número sea
correcto.*

### Nuevo objetivo de la asignatura (propuesta)

> Al terminar LCC, el estudiante es capaz de plantear un problema de cálculo
> científico, obtener una implementación (escrita por él o asistida por IA),
> **verificar** que es correcta, **caracterizar su error** y **defender** el
> resultado ante otra persona.

### Cambios propuestos

**A. Un hilo transversal de verificación (lo más importante).**
Cada método numérico se estudia en un ciclo fijo:

1. *Concepto*: la matemática del método y sus hipótesis.
2. *Predicción*: antes de ejecutar nada, ¿qué debería pasar? ¿Cuántas
   iteraciones? ¿Qué orden de error?
3. *Implementación*: a mano o con IA.
4. *Verificación*: casos con solución conocida, comparación con
   `scipy`, gráficas de convergencia, leyes de conservación (energía en un
   péndulo), tests con `assert`. **Ahora mismo el manual no menciona `assert`
   ni los tests ni una sola vez.**
5. *Romperlo*: buscar entradas donde el método falla (Newton con derivada
   nula, Gauss sin pivoteo, punto fijo con |g'|>1, enteros en lugar de reales).
6. *Explicar* por qué falla.

**B. Un núcleo que se escribe sin IA.** Un conjunto pequeño de algoritmos
(bucles y funciones básicas, bisección, eliminación de Gauss, regla del
trapecio, Euler) se programa a mano y se evalúa en el aula. No por nostalgia:
escribirlos es lo que construye el modelo mental que luego permite revisar el
código de la IA. Es el equivalente a hacer cuentas a mano antes de usar la
calculadora.

**C. Un capítulo nuevo: programar con un asistente de IA.** Cómo
especificar un problema (entradas, salidas, tolerancias, casos límite); cómo
leer el código recibido; cómo escribir los tests *antes* de pedir el código;
qué errores típicos cometen los asistentes en cálculo numérico; cómo
documentar el uso de la IA. Encaja tras el capítulo de introducción a Python.

**D. Nuevos tipos de ejercicio**, aprovechando los ejercicios que ya existen:

- *Depura este código*: código plausible con errores sembrados como los
  encontrados en esta revisión (tipos enteros, `range` con un elemento de
  menos, criterio de parada absoluto frente a relativo, orden de
  coeficientes).
- *¿Cuál es correcta?*: tres implementaciones del mismo método; sólo una
  funciona en todos los casos. Justifica.
- *Critica la explicación*: una explicación generada por IA de un método,
  con un error conceptual.
- *Mide el orden*: estimar empíricamente el orden de convergencia o de error
  de un método a partir de sus resultados.
- *Primero los tests*: escribir las comprobaciones antes de pedir (o escribir)
  la implementación.

**E. Rediseño de la evaluación.** Los tests actuales ("crea las funciones
necesarias y da los resultados en un notebook") los resuelve hoy una IA en
segundos. Propuesta:

- Pruebas en el aula sin IA para el núcleo del apartado B.
- Proyectos para casa con IA permitida, con una sección de **verificación**
  que pese tanto como el resultado, y una declaración de uso de la IA.
- **Defensa oral breve** (5 minutos) del notebook: ¿qué pasa si cambias la
  tolerancia a 1e-20? ¿Por qué Newton no converge desde x0=0? Es la forma más
  fiable de comprobar si se entiende lo entregado.

**F. Proyectos con contenido físico.** El manual ya tiene buenos ejemplos
(Kepler, condensador, péndulo amortiguado, datos de la red eléctrica). Se
propone que cada bloque termine en un pequeño problema físico donde la
verificación tenga sentido físico (conservación de la energía, límites
conocidos, análisis dimensional).

**G. Formato del material.** El manual en LaTeX bilingüe es una obra muy
valiosa, pero el código está pegado a mano en el texto, y por eso nadie había
detectado los ~20 ejemplos rotos. Opciones, de menor a mayor cambio:

1. Mantener LaTeX y añadir un **script de comprobación automática** que
   ejecute todos los bloques de código (el que se ha usado en esta revisión),
   o una integración continua en GitHub que lo haga en cada cambio.
2. Sacar todos los ejemplos a ficheros `.py` que se incluyen con
   `\inputminted` y se prueban de forma independiente.
3. A medio plazo, valorar un formato ejecutable (Jupyter Book o Quarto), en el
   que cada ejemplo se ejecuta al generar el documento y los alumnos pueden
   abrir cada capítulo como notebook.

**H. Actualizaciones menores de contenido.** Spyder se mantiene como
entorno principal (decisión de nov 2026); los notebooks se usan desde
Spyder con `spyder-notebook`. Añadir `scipy.integrate.solve_ivp` al
capítulo de EDOs, sustituir `interp1d` (marcada como *legacy* en SciPy) y
añadir una sección de vectorización y rendimiento.

### Hoja de ruta (aprobada, nov 2026)

| Fase | Periodo orientativo | Contenido |
|---|---|---|
| 1 | nov 2026 – feb 2027 | Terminar la revisión capítulo a capítulo (gramática, estilo, contenido); comprobación automática del código. |
| 2 | feb – abr 2027 | Consensuar con el profesorado el nuevo enfoque y la evaluación; redactar la guía de uso de la IA. |
| 3 | abr – jul 2027 | Capítulo de "programar con IA"; reescribir ejercicios con los nuevos tipos; ciclo de verificación en los capítulos 2–4. |
| 4 | curso 2027-28 | Piloto en un grupo (hay experiencia previa con grupo piloto), comparado con un grupo de control. |
| 5 | verano 2028 | Evaluar el piloto y extender o ajustar. |
