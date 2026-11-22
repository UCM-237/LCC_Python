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

---

## 2. Pendiente: necesita decisión o revisión humana

1. **`big_brother/` contiene calificaciones de alumnos** (`.xlsx`) dentro de un
   repositorio git. Aunque sea privado, son datos personales: el historial de
   git los conserva aunque se borren. Recomendación: sacarlos del repositorio
   (y, si se quiere ser estricto, del historial). No se ha abierto ni
   modificado nada de esa carpeta. Además, `big_brother/lcc_result.ipynb`
   tiene marcas de conflicto de merge sin resolver.
2. `interpolacion/Test2024_Interpolacion.ipynb`: se usa una variable `t1` que
   nunca se define (falta la malla de evaluación).
3. `matplotlib/matplotlib.ipynb`: `ax3.meshgrid(...)` no existe en Matplotlib;
   no está claro qué gráfico se quería.
4. Ficheros `.p` en el solucionario: son *P-code* de MATLAB (ofuscado), restos
   de la versión antigua de la asignatura. ¿Se conservan?
5. `codigos/Intro_matplotlib/untitled0.py` y `untitled3.py`: el texto
   referencia `untitled0.py` como ejemplo; convendría darles nombres
   descriptivos.
6. **La revisión gramatical y de estilo no está hecha.** El corrector sólo
   encuentra palabras mal escritas. El inglés, en particular, tiene muchas
   construcciones calcadas del español que conviene revisar capítulo a
   capítulo.
7. Anaconda: sus condiciones de uso para organizaciones cambiaron en 2024.
   Conviene comprobar si el uso en la UCM está cubierto. Si no, se puede
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

### Hoja de ruta (propuesta)

| Fase | Periodo orientativo | Contenido |
|---|---|---|
| 1 | nov 2026 – feb 2027 | Terminar la revisión capítulo a capítulo (gramática, estilo, contenido); comprobación automática del código. |
| 2 | feb – abr 2027 | Consensuar con el profesorado el nuevo enfoque y la evaluación; redactar la guía de uso de la IA. |
| 3 | abr – jul 2027 | Capítulo de "programar con IA"; reescribir ejercicios con los nuevos tipos; ciclo de verificación en los capítulos 2–4. |
| 4 | curso 2027-28 | Piloto en un grupo (hay experiencia previa con grupo piloto), comparado con un grupo de control. |
| 5 | verano 2028 | Evaluar el piloto y extender o ajustar. |
