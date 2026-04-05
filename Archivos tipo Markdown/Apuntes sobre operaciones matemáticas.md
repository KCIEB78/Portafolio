# Archivo referente a operaciones matemáticas que se pueden realizar en Python

1. Para realizar cualquier operación en Python basta con agregar un bloque de tipo " Código / Code ", las operaciones NO se pueden realizar en bloques de tipo " Texto / Markdown "

2. Para insertar un " bloque de tipo código " en Google Colab y Visual Code Studio, basta con ir a la barra de herramientas y dar clic en la herramienta " + Código / + Code "

3. Para insertar un texto en Anaconda - JupyterLab, basta con agregar un bloque con el símbolo " + ", predeterminadamente se agrega un nuevo bloque de tipo " Código / Code "

---

# **1. Operaciones básicas matemáticas**


## *1.1. Suma " + "*

**Descripción:**

Para realizar una suma básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una **" línea de código "** con su respectivo signo **" + "**


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



## *1.2. Resta " - "*

**Descripción:**

Para realizar una resta básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una **" línea de código "** con su respectivo signo **" - "**


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

**Descripción:**

Para realizar una multiplicación básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una **" línea de código "** con su respectivo signo **" * "**


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

**Descripción:**

Para realizar una operación de " potencia " o " exponenciación " de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una **" línea de código "** con dos **" * "**


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

## *1.5. División " / "*

### 1.5.1. *Divisiones sin un límite de decimales*

**Descripción:**

Para realizar una división básica de dos o más números, **ya sean enteros o decimales**, basta con escribirlos en una **" línea de código "** con su respectivo signo **" / "**


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



Como se puede ver, el resultado arroja el resultado con **TODOS** los decimales, sin un " límite " tal cual

### *1.5.2. Divisiones con un límite de decimales*

**Descripción:**

Para poder controlar el número de decimales que arrojará el resultado de las divisiones realizadas, basta con escribir la **" función ": " round() "**

> Cualquier **" función " / " fórmula "** que se quiera utilizar en Python, funcionan como aquellas que se utilizan en **Microsoft Excel**, refiriéndome a que cada una de ellas tiene su propia **" sintaxis "**, que básicamente es **EL ORDEN EN QUE OBLIGATORIAMENTE** se necesitan escribir los datos o valores, para que la **" función " / " fórmula "** se ejecute correctamente y no arroje algún **" error " / " bug "**

La " sintaxis " de esta función nos pide que entre los paréntesis " () ":

- Primero se escriba la división que se quiera realizar, **ya sea con número enteros o decimales e inclusive varias divisiones a la vez**

- Posteriormente, se agregue una coma **" , "** después del último número que se quiera dividir

- Al final se escriba el número que establecerá la cantidad de decimales que arrojará el resultado 


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



Al momento de **" redondear "** los decimales que arrojará el resultado; Python seguirá las **" reglas "** establecidas:

- Si el decimal es igual o mayor a **" 0.5 "**, al momento de " redondear ", éste " subira " directamente para convertirse en un " entero ": **1.0**; ésto significa que lo mismo se aplica para los decimales: **" 0.6 ", " 0.7 ", " 0.8 " y " 0.9 "**

- De igual manera, si el decimal es igual o mayor a " 0.05 ", al momento de " redondear ", éste " subirá " directamente a: **" 0.1 "**; ésto significa que los mismo se aplica para los decimales: **" 0.06 ", " 0.07 ", " 0.08 " y " 0.09 "**

- En caso de que el decimal sea igual o menor a **" 0.4 "**, al momento de " redondear ", éste " bajará " directamente para convertirse en un " 0 ": **" 0.0 "**; ésto significa que lo mismo se aplica para los decimales: **" 0.3 ", " 0.2 " y " 0.1 "**

- De igual manera, si el decimal es igual o menor a " 0.04 ", al momento de " redondear ", éste " bajará directamente a: **" 0.0 "**; ésto significa que lo mismo se aplica para los decimales: **" 0.03 ", " 0.02 " y " 0.01 "**

Y así sucesivamente hasta la **" n "** cantidad de decimales que se quieran redondear para el resultado

## *1.6. División de "piso" " / / "*

**Descripción:**

Las divisiones de piso se refieren a aquellas que, **aunque su resultado sean números enteros o decimales**, siempre dará el mismo como un **" número entero " y al menos el decimal " .0 "** (Indicando que el resultado originalmente incluye uno o varios decimales); éstas, se realizan mediante la escritura de dos " / " en medio de los valores.

Pero, en este tipo de divisiones, **NO se aplicarán las mismas reglas de " redondeo "**; por lo tanto, cualquier decimal: **0.9, 0.8, 0.7, 0.6 , 0.5, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, etc...**, se " convertiran " directamente a un valor nulo: **" 0 "**


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


## *1.7. *División de restante " % "* 

**Descripción:**

Las divisiones de tipo **" restante " / " piso restante "** se refieren a divisiones que, a pesar de seguir el mismo comportamiento que las divisiones **" normales y de piso "**; siempre se mostrará el **" residuo "** de dichas divisiones, recordando que el residuo son aquellos número que en papel quedan debajo de la división escrita

### *1.7.1. Divisiones de restante sin límite de decimales*


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


### *1.7.2. Divisiones de restante con límite de decimales*


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
100000 % 241.5 % 842.7 % 96.1
```




    19.0











> En todos estos tipos de operaciones, la manera en que Python las " ejecutará " siempre será de izquierda a derecha
