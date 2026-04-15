# Archivo referente a operaciones matemáticas que se pueden realizar en Python

1. Para realizar cualquier operación en Python basta con agregar un bloque de tipo **"Código / Code"**, las operaciones **NO SE PUEDEN EJECUTAR** en bloques de tipo **"Texto / Markdown"**, solamente escribirlas; si la operación está en el tipo de celda correcto, el resultado aparecerá debajo de la misma

> Para identificar fácilmente una celda de tipo "Código / Code", éstas contarán con unos pequeños "corchetes []" en la esquina inferior izquierda, las cuales indicarán el "índice" de cuantas celdas del mismo tipo se han ejecutado antes de ejecutar la celda seleccionada (la primera celda ejecutada teniendo un "1"); mientras que, la celda que contiene el resultado contará con tres puntos del lado izquierdo, éstas no se pueden editar ni modificar, simplemente son para visualizar el resultado.

2. Para insertar una celda de tipo **"Código / Code"** en Google Colab y Visual Code Studio, basta con ir a la barra de herramientas y dar clic en la herramienta **"+ Código / + Code"**

3. Para insertar una celda de tipo **"Código / Code"** en JupyterLab, basta con ir a la barra de herramientas y dar click en el símbolo **"+"** y se agregará una celda de tipo "Código / Code" automaticamente

4. En caso de querer convertir cualquier celda de tipo **"Código / Code"** a una celda de tipo **"Texto / Markwdown"** en cualquiera de los programas anteriormente mencionado, basta con *"seleccionar"* la celda deseada y presionar la "Tecla Y"

---

# **1. Operaciones básicas matemáticas**

## *1.1. Suma "+"*

### *1.1.1. Escritura de la operación en Python:*

Para realizar una suma básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una celda de tipo **"Código / Code"** con su respectivo signo **"+"**

### *1.1.2. Ejemplos de la operación:*


```python
950 + 720
```




    1670




```python
72 + 65 + 35 + 42
```




    214




```python
58.62 + 47.36
```




    105.97999999999999




```python
784.24 + 89.71 + 361.87 + 98.21
```




    1334.0300000000002



## *1.2. Resta "-"*

### *1.2.1. Escritura de la operación en Python:*

Para realizar una resta básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una celda de tipo **"Código / Code"** con su respectivo signo **"-"**

### *1.2.2. Ejemplos de la operación:*


```python
1846 - 975
```




    871




```python
465.87 - 95.74
```




    370.13




```python
9000 - 4765 - 354 - 870 - 624
```




    2387




```python
10000 - 2500.24 - 364.87 - 264.87 - 3476.81
```




    3393.2100000000005



## *1.3. Multiplicación " * "*

### *1.3.1. Escritura de la operación en Python:*

Para realizar una multiplicación básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una celda de tipo **"Código / Code"** con su respectivo signo **" * "**

### *1.3.2. Ejemplos de la operación:*


```python
50 * 870
```




    43500




```python
260.25 * 140.32
```




    36518.28




```python
24 * 34 * 98 * 47
```




    3758496




```python
34.21 * 58*94 * 34.74
```




    6479458.8408



## *1.4. Potencias  / Exponenciación " * * "*

### *1.4.1. Descripción y escritura de la operación en Python:*

Las operaciones de **"potencias / exponentes"** son aquellas donde un número se multiplica por si mismo una "n" cantidad de veces, y para realizar este tipo de operación de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una celda de tipo **"Código / Code"** con dos **" * "**

### *1.4.2. Ejemplos de la operación:*


```python
240 ** 43
```




    2234001156466047988462265195030148466064987998021736453898240000000000000000000000000000000000000000000




```python
4.7 ** 6
```




    10779.215329000002




```python
10 ** 2 ** 4
```




    10000000000000000




```python
4.1 ** 6 ** 3.2
```




    2.540659771866361e+189



> Al momento de realizar operaciones de potencias, es necesario tener cuidado con el resultado; ya que, cualquier entorno tiene su límite de caracteres para la visualización del resultado. Y, aunque se pueda configurar para poder ver más caracteres, un número bastante largo provoca incomodidad y dificulta la lectura del documento

## *1.5. División "/"*

### *1.5.1. Escritura de la operación en Python:*

Para realizar una división básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una celda de tipo **"Código / Code"** con su respectivo signo **"/"**

### *1.5.2. Ejemplos de divisiones sin un límite de decimales*


```python
80 / 5
```




    16.0




```python
700.14 / 50.12
```




    13.96927374301676




```python
8000 / 24 / 36 / 7
```




    1.3227513227513228




```python
100000 / 241.5 / 842.7 / 96.1
```




    0.005113125863194553



>> Como se puede ver, el resultado arroja el resultado con todos los decimales, sin un " límite " como tal

### *1.5.3. Ejemplos de divisiones con un límite de decimales*


```python
round(80 / 5, 2)
```




    16.0




```python
round(700.14 / 50.12, 2)
```




    13.97




```python
round(8000 / 24 / 36 / 7, 3)
```




    1.323




```python
round(100000 / 241.5 / 842.7 / 96.1, 4)
```




    0.0051



>> El tema de las funciones la desarrollaré en otro cuadernillo

>> Las reglas que se utiliza en papel y en el " entorno de programación " de Python para realizar el redondeo de los números decimales, los explico en el apartado " 3. "

## *1.6. División de "piso" "//"*

### *1.6.1. Descripción de la operación:*

Las divisiones de piso se refieren a aquellas que, **aunque su resultado sean números enteros o decimales**, siempre dará el mismo como un **" número entero " y al menos el decimal " .0 "** (Indicando que el resultado originalmente incluye uno o varios decimales); éstas, se realizan mediante la escritura de dos **"/"** en medio de los valores.

Pero, hay que tener en cuenta que en este tipo de divisiones, **NO se aplicarán reglas de " redondeo "**; por lo tanto, cualquier decimal: **0.9, 0.8, 0.7, 0.6 , 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, etc...**, se " convertiran " automáticamente a un valor nulo: **" 0 "**

### *1.6.2. Ejemplos de la operación:*


```python
80 // 5
```




    16




```python
700.14 // 50.12
```




    13.0




```python
8000 // 24 // 36 // 7
```




    1




```python
100000 // 241.5 // 842.7 // 96.1
```




    0.0



## *1.7. *División de restante "%"*

### *1.7.1. Descripción y escritura de las operaciones en Python:*

Las divisiones de tipo **" restante "** son aquellas que, a pesar de seguir el mismo comportamiento que las divisiones **" normales "**; el resultado siempre será el **" residuo "** de dichas divisiones. 

>> Hay que recordar que el " residuo " son aquellos números que quedan debajo de la división cuando uno los desarrolla en papel

Para realizar este tipo de operaciones de dos o más números, **ya sean enteros o decimales**, basta con escribir un **"signo de porcentual %"** en una celda de tipo **"Código / Code"**

>> En este tipo de divisiones, no existen las " divisiones de piso restante "; ya que, Python no lo reconoce como una operación posible. Por lo tanto, lo úncio que se le podría hacer a éstas es " redondearlas "

### *1.7.2. Ejemplos de divisiones de restante:*


```python
80 % 5
```




    0




```python
700.14 % 50.12
```




    48.58000000000002




```python
8000 % 24 % 36 % 7
```




    1




```python
100000 // 241.5 // 842.7 // 96.1
```




    0.0



### *1.7.3. Ejemplos de divisiones de restante con límite de decimales*


```python
round(700.14 % 50.12, 2)
```




    48.58



## *1.8. Raices **" ** (1/n) "***

### *1.8.1. Descripción y escritura de la operación en Python:*

Python al **NO tener un símbolo que pueda representar una operación de "raiz"** tal cual, se opta por usar el mismo procedimiento que las **potencias / exponenciación**, escribiendo doble **" * "**; pero, en vez de utilizar un número entero como "exponente", se opta por utilizar una "fracción" que hará referencia a las diferentes raices posibles: "raiz cuadrada (1/2) / cúbica (1/3) / etc..."

### *1.8.2. Ejemplos de la operación:*


```python
9 ** 2
```




    81




```python
81 ** (1/2)
```




    9.0




```python
25 ** 3
```




    15625




```python
round(15625 ** (1/3),0)
```




    25.0



--- 

# **2. Jerarquía de operaciones**

## *2.1. Descripción de la "Jerarquía de operaciones"*

La *"Jerarquía de operaciones "* hace referencia a las **"normas / reglas" QUE EN PAPEL** se tienen que llevar a cabo y **QUE PYTHON USA** para poder obtener el resultado correcto de un conjunto de operaciones que contengan **DOS O MÁS** tipos de "operadores" (+ , - , * , etc...)

Éstas establecen el **"orden"** en que se tienen que realizar dichas operaciones, para evitar que el resultado **NO tenga "discrepancias / errores"** al momento de compararse con diferentes herramientas especializadas en realizar *cálculos matemáticos*

>> A veces el hecho de que las *calculadoras , teléfonos o cualquier otra herramienta* de resultados completamente distintos; puede deberse a que la programación de las mismas *NO haya sido establecida correctamente* para seguir dichas " normas / reglas " (lo mismo ocurre con las *Reglas para el redondeo de deciamles*). O también puede influir mucho la **" gama / calidad "** de las mismas.

## *2.2. Normás de la jerarquía de operaciones*

### *2.2.1. Normas para los "signos de agrupación" - "paréntesis ()" , "corchetes []" y "llaves {}":*

Las primeras **" normas / reglas "** que establece la **" jerarquía de operaciones "** dictan resolver en una " notación matemática ":

- Todas aquellas operaciones que estén encerradas entre **"paréntesis ()"**

- Todas aquellas operaciones que estén encerradas entre **"corchetes []"**

- Todas aquellas operaciones que estén encerradas entre **"llaves / llave curva {}"**

Sin importar qué tipo de **"signo de agrupación"** se utilice primero para agrupar diferentes operaciones *(ya sea que primero se use paréntesis y después llaves, o cualquier otro orden)*, estos se resolverán en **"orden de profundidad"**; siendo que, las agrupaciones que estén más adentro son las que se resolverán primero y así sucesivamente *"hacia afuera"*

De igual manera, cualquier signo de agrupación puede utilizarse para implicar *una multiplicación entre dos o más números*; e inclusive para interpretar *la combinación de signos en multiplicación o división*, siguiendo la **"ley de los signos"**:

- Multiplicación: **+ * + = +** | **- * - = +** | **+ * - = -** | **- * + = -**

- División: **+ / + = +** | **- / - = +** | **+ / - = -** | **- / + = -**

- Ejemplo 1: "8(45)(20) / 8[45][20] / 8{45}{20} "; siguiendo la regla, estas expresiones se deben de interpretar como "8 * (45) * (20) / 8 * [45] * [20] / 8 * {45} * {20}"

- Ejemplo 2: "8 - (-45)(20)"; se interpreta como "8 - (-45) * (20)"; y teniendo como resultado "8 - (-900) = 8 + 900 = 908"

> IMPORTANTE: A pesar de que el uso de los "signos de agrupación" y las "notaciones matemáticas" que mencioné en el ejemplo 1, técnicamente sean correctas si es que se interpretan en papel. En un ambiente de programación   de Python el uso de corchetes o llaves es para generar elementos como: Listas y Diccionarios; por lo que, estos signos de agrupación, no pueden ser utilizados para este propósito matemático.

> Por lo tanto, los "corchetes [] y llaves {}" DEBEN CONVERTIRSE EN "paréntesis ()", para poder ejecutar correctamente el código.

>> En otro apartado resuelvo un ejemplo para demostrar dicho " orden " y esta misma situación donde convierto los signos de agrupación a solamente paréntesis

- Una cosa más a tomar en cuenta, es **MUY IMPORTANTE** hacer uso correcto de los *"operadores" (+, - , *, etc...)* dentro los **" signos de agrupación "** *(tomando en cuenta la nota previa sobre los paréntesis)*; ya que, si no se colocan correctamente, Python podría interpretarlos como un intento de " llamar a una función " (a pesar de no haber una palabra que las defina como: .mean , .append , .pop , etc...), lo que provocaría " bugs / errores " al momento de ejecutar el código

>> Toda la parte de funciones, listas y diccionarios las desarrollaré en otro cuadernillo

### *2.2.2. Reglas para las operaciones básicas matemáticas:*

Las **"normas / reglas"** que establece la **"jerarquía de operaciones"** para el caso de las operaciones básicas *(todas aquellas establecidas en el apartado "1.Operaciones básicas matemáticas")*:

1. Resolver todas aquellas operaciones de **"potencia / exponente = n ** n"** y **"raiz = n ** (1/n)"**

>> Para estas regla, viéndolo ya en un ambiente generado en Python, ambos entrarían en la misma categoría de "potencia", solamente lo menciono para respetar la regla original

2. Resolver todas aquellas operaciones de **"multiplicación = n * n"** y **"división = n / n"**

>> En esta regla, de igual manera pensándolo en un ambiente generado en Python, aquí entrarían las operaciones de **"división de piso = n // n "** y **" restante = n % n "**

3. Resolver todas aquellas operaciones de **"suma = n + n"** y **"resta = n - n"**

Dentro de estos "niveles" o de los mismos "signos de agrupación", pueden surgir la dudad de:

> "¿Cuál es el " orden de prioridad " en el que se deben de resolver estas mismas operaciones?"

Para esto, tenemos que entender que:

- Hay prioridad entre niveles **TAL CUAL** están enlistadas anteriormente: **"1. Potencias (y raíces)", "2. Multiplicación y División (de piso y restante)", "3. Suma y resta"**

- Dentro del mismo nivel la "prioridad" se establece de **"IZQUIERDA A DERECHA"**, la que primero aparezca del mismo nivel se resolverá antes de resolver la siguiente del mismo nivel

## *2.3. Ejemplos y procedimiento para la solución de operaciones en base a la "jerarquía de operaciones" y el "desarollo por bloques"*

### *2.3.1. Ejemplo 1:*

#### *2.3.1.1. Desarrollo paso a paso:*

- Ejemplo: 457 + 890 * 32 - 6589 + 152 % 4 + 15 * 8 ** 6 - 47 ** (1/4) ** 7 + 15 / 8 - 8 + 970 // 25

Para tener una "operación matemática" más ordenada se pueden agregar paréntesis, quedando de la siguiente manera:

- 457 + (890 * 32) - 6589 + (152 % 4) + (15 * (8 ** 6)) - ((47 ** (1 / 4)) ** 7) + (15 / 8) - 8 + (970 // 25)

> En este caso para escribir los paréntesis también tomé en cuenta los niveles y los ajuste conforme a los mismos

1. Resolver las operaciones de potencia (recordando que en Python las raíces entran en la misma categoría): 

- " (8 ** 6) " | " (47 ** (1 / 4)) " = " 262144 " | "2.6183304986958853" (importante escribir todos los decimales)

- " (2.6183304986958853 ** 7) " = " 843.6673678514757 "

> IMPORTANTE: NO pasar al siguiente nivel hasta que se terminen de resolver las operaciones del mismo.

2. Resolver las multiplicaciones y divisiones (recordando que en Python las divisiones de piso y restante entran en la misma categoría):

- " (890 * 32) " | " (152 % 4) | (15 * 262144) | (15 / 8) | (970 // 25) = " 28480 " | " 0 " | " 3932160 " | " 1.875 " | " 38 "

3. Resolver las sumas y restas (En este nivel ya no debería quedar ninguna operación de cualquier otro nivel):

- 457 + 28480 - 6589 + 0 + 3932160 - 843.6673678514757 + 1.875 - 8 + 38

Resultado final: **" 3953696.2076321486 "**

> En este ejemplo prioricé la solución por "niveles", en vez de organizar el desarrollo "dividiéndolo por bloques", en el siguiente verán dicha forma de resolverlo

#### *2.3.1.2 Desarrollo de la operación en una línea de código:*


```python
457 + (890 * 32) - 6589 + (152 % 4) + (15 * (8 ** 6)) - ((47 ** (1 / 4)) ** 7) + (15 / 8) - 8 + (970 // 25)
```




    3953696.2076321486



>> IMPORTANTE: Como se puede ver en el " bloque ": (15 * (8 ** 6)), si no hubiera escrito el operador de multiplicación: " * " antes de la potencia " (8 ** 6) ", hubiera ocurrido el error que mencioné previamente donde Python lo hubiera interpretado como " llamar a una función "

> En este ejemplo, prioricé la solución de cada nivel sin " dividirlo por bloques "

### *2.3.2. Ejemplo 2:*

#### 2.3.2.1. Desarrollo paso a paso:

Operación matemática con diferentes **"signos de agrupación"**:

45 - {52 * [47 + [24 * [25 + (4+8)]]]} - {[12 - 6 * [24 * (900 - 780) - 73] - 5]} * 78 * {[24 / [8 * (24 + 3)] + 87] + 100}

Convirtiendo los **"corchetes [] y llaves {} "** en **" paréntesis ()"**:

45 - (52 * (47 + (24 * (25 + (4+8))))) - ((12 - 6 * (24 * (900 - 780) - 73) - 5)) * 78 * ((24 / (8 * (24 + 3)) + 87) + 100)

>> Ésto, para que Python pudiera ejecutarlo en una línea de código

Solución dividida por bloques

Bloque 1 - "(52 * (47 + (24 * (25 + (4+8)))))":
1. (4 + 8) = (12)
2. (25 + 12) = (37)
3. (24 * 37) = (888)
4. (47 + 888) = (935)
5. (52 * 935) = 48620

Bloque 2 - "(12 - 6 * (24 * (900 - 780) - 73) - 5)":
1. (900 - 780) = (120)
2. (24 * 120) = (2880)
3. (2880 - 73) = (2807)
4. (6 * 2807) = (16842)
5. (12 - 16842 - 5) = (-16835)

Bloque 3: "((24 / (8 * (24 + 3)) + 87) + 100)"
1. (24 + 3) = (27)
2. (8 * 27) = (216)
3. (24 / 216) = (0.111111...)
4. (0.11 + 87) = (87.11111...)
5. (87.11 + 100) = (187.11111...)

Bloque 4: "(-16835 * 78 * 187.111111)":
1. (-16835 * 78 * 187.11111...) = - 

Bloque 5: "45 - 48620 + 245701213.33333332"
1. (45 - 48620) =  -48575
2. -48575 + 245701213.33333332 = 245652638.33

> Como se puede ver en este ejemplo, también es bastante útil dividir las mismas "operaciones básicas" en pequeños "bloques" para entender el procedimiento que se llevó a cabo para obtener el resultado, tomando en cuenta como los mismos paréntesis ayudaron bastante a crear éstos mismos

#### *2.3.2.2. Desarrollo de la operación en una línea de código*


```python
round(45 - (52 * (47 + (24 * (25 + (4+8))))) - ((12 - 6 * (24 * (900 - 780) - 73) - 5)) * 78 * ((24 / (8 * (24 + 3)) + 87) + 100), 2)
```




    245652638.33



> Aquí lo único "diferente" que hice, fue llamar a la función ". round" para redondear el resultado final

---

# 3. Reglas para el redondeo de decimales:

## *3.1. Descripción del redondeo de decimales:*

El **"redondeo de decimales"** se refiere a *aquel proceso al que se le puede someter a un número* que, ya sea por el resultado de una división o de una operación matemática extensa (como los ejemplos del apartado "2."), *cuenta con números decimales "infinitos o bastante extensos"*.

## *3.2. Reglas para el correcto redondeo de decimales:*

Al momento de **"redondear"** los decimales se deben seguir estas reglas:

- Si el decimal es igual o mayor a **"0.5"**, al momento de "redondear", éste "subirá" directamente para convertirse en un entero: **"1.0"**; ésto significa que lo mismo aplicará para: **"0.6, 0.7, 0.8 y 0.9 "**

- Si el decimal es igual o menor a **"0.4"**, al momento de "redondear", éste "bajará" directamente para convertirse en un valor nulo: **"0.0"**; ésto significa que lo mismo aplicará para: **"0.3, 0.2 y 0.1"**

- Si el decimal es igual o mayor a **"0.05"**, al momento de "redondear", éste "subirá" directamente para convertirse en un entero: **"0.1"**; ésto significa que lo mismo aplicará para: **"0.06, 0.07, 0.08 y 0.09"**

- Si el decimal es igual o menor a **"0.04"**, al momento de "redondear", éste "bajará" directamente para convertirse en un valor nulo: **"0.0"**; ésto significa que lo mismo aplicará para: **"0.03, 0.02 y 0.01"**

Y así sucesivamente hasta la **"n"** cantidad de decimales que se necesiten redondear; estas mismas reglas, siendo las que aplica Python al momento de utilizar la función **".round"** 

>> Uno mismo puede hacer varias pruebas para verificar estas reglas

---

# Extra

Este archivo será algo corto ya que quería mencionar toda esta parte de algunas reglas que usualmente se olvidan al momento de realizar operaciones; ya sean escritas en papel, o cuando uno no termina de entender el procedimiento que, cualquier herramienta que cuente con una calculadora, lleva a cabo para arrojar el resultado en la pantalla

Las reglas para la " jerarquía de operaciones " y " redondeo de decimales " son una parte muy importante que a veces se olvida y si no se entiende del todo, puedes atorarte bastante ya cuando te metes en el uso de funciones, variables, librerías y otros elementos que utiliza Python para poder ejecutar cualquier código
