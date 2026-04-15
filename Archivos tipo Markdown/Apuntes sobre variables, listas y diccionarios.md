# Archivo referente a tipos de datos, variables, listas y diccionarios en Python

1. En este archivo iniciaré con los tipos de datos y como establecer variables para entender como es que Python guarda dichos elementos

1.1. Teniendo en cuenta que, en otro cuadernillo explicaré y desarrollaré la parte de las operaciones y algunas funciones que se pueden realizar entre los diferentes tipos de datos y las mismas variables

---

# **1. Tipos de datos en Python utilizados para el análisis básico de datos**

## *1.1. Tipos de datos:*

### *1.1.1. Tipo de dato "int"*

#### *1.1.1.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a todos aquellos que son **"números enteros"** y que **NO TIENEN DECIMALES** *(incluyendo la escritura del decimal ".0")*

Ejemplos: 1 , 2 , 3 , 982 , 100023 , 83921 , 1000000 , 23894764 , etc...

#### *1.1.1.2. Ejemplos en líneas de código:*


```python
1
```




    1




```python
982
```




    982




```python
83921
```




    83921




```python
23894764
```




    23894764



### *1.1.2. Tipo de dato "float"*

#### *1.1.2.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a todos aquellos que son **"números con "n" cantidad de decimales"**, *(incluyendo la escritura del decimal ".0")*

Ejemplo: 0.0, 0.10, 124.35, 902.34, etc...

#### *1.1.2.2. Ejemplos en líneas de código:*


```python
0.10
```




    0.1




```python
124.35
```




    124.35




```python
902.34
```




    902.34



---

> IMPORTANTE: En dado caso de escribir un número que empiece con " 0 " (029, 0831.21, etc...), Python si los interpretará como tipos de datos " float "; pero, estos no son comúnmente utilizados en bases de datos ya estandarizadas. Por lo que, no los recomiendo utilizar al menos que uno sepa el comportamiento y los posibles usos de estos mismos

### *1.1.3. Tipo de dato "string":*

#### *1.1.3.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a todos aquellos donde se escriben: una letra, una palabra, una cadena de texto o párrafos (incluyendo los espacios en blanco), e inclusive cadenas de texto que contengan números, signos, símbolos o caracteres especiales

Para generar correctamente este tipo de datos, es necesario escribirlos " entre comillas "" "

Ejemplo: "Palabra" , "Texto de ejemplo de tipo de dato string", "Texto_de ejemplo*con caracteres=especiales", etc...

#### *1.1.3.2. Ejemplos en líneas de código:*


```python
"Palabra"
```




    'Palabra'




```python
"Texto de ejemplo de tipo de dato string"
```




    'Texto de ejemplo de tipo de dato string'




```python
"Texto_de ejemplo*con caracteres=especiales"
```




    'Texto_de ejemplo*con caracteres=especiales'



>> Como se puede observar, Python automáticamente los interpretó como datos de tipo " string " y arrojó el resultado correctamente


```python
Texto de ejemplo donde Python arroja un error en dado caso de no colocar las comillas
```


      Cell In[15], line 1
        Texto de ejemplo donde Python arroja un error en dado caso de no colocar las comillas
              ^
    SyntaxError: invalid syntax
    


>> Como se puede observar, al no colocar las comillas al principio y al final del texto, Python arroja el error al tratar de interpretar las letras como signos, variables u otro elemento

>> No se recomienda guardar letras como variables, al menos que necesites guardar un símbolo o viñeta especial, como los que tengo anotados en el archivo: " Apuntes sobre bloques de textos " o uno que no puedas escribir en tu teclado de forma manual (por codigo ASCII o la combinación de " CTRL / ALT + cualquier tecla ")

---

> IMPORTANTE: Para crear datos de tipo "string", también pueden usarse " tildes '_' " en dado caso de querer usar comillas o tildes dentro del mismo tipo de dato; de igual manera, dependiendo de la estandarización y el uso que se le den a esos signos

---

### *1.1.4. Tipo de dato "bool":*

#### *1.1.4.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a aquellos que contienen datos que se pueden clasificar así mismos como **"verdadero"** o **"falso"**

Este tipo de datos se pueden generar mediante el uso de **"operadores"** que permiten realizar diferentes tipos de comparativas entre datos de cualquier tipo

>> Toda la cuestión de los "operadores" usados para realizar las comparativas los desarrollo en el apartado "3."

#### *1.1.4.2. Ejemplos en líneas de código:*


```python
850 > 25
```




    True




```python
"String" == "String"
```




    True




```python
250 >= 200
```




    True




```python
9000 < 10
```




    False



>> Como se puede observar, estos tipos de datos también se pueden generar entre datos de tipo "string"

#### *1.1.4.2. Ejemplos en líneas de código

### *1.1.5. Tipo de dato "list":*

#### *1.1.5.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a aquellos que contienen un enlistado de palabras o textos; éstos, deben estar escritos **"entre dos corchetes [] y separados por una coma ,"** por cada una de las palabras o textos que se quieran incluir en la misma

#### *1.1.5.2. Ejemplos de listas simples en celdas de tipo "Texto / Markdown" y "Código / Code":*

Un ejemplo de una **"lista simple"** donde solamente incluyamos palabras o textos dentro de la misma:

[
    palabra,
    texto de ejemplo para lista,
    palabras de ejemplo,
    palabra,
    etc...
]


```python
[
    "Palabra",
    "Texto de ejemplo para la lista",
    "Palabra",
    "Palabra",
    "Segundo texto de ejemplo"
]
```




    ['Palabra',
     'Texto de ejemplo para la lista',
     'Palabra',
     'Palabra',
     'Segundo texto de ejemplo']



>> Como se puede ver en la celda tipo "Código / Code", esa es una manera "comoda y eficiente" de escribir cada uno de los elementos que contendrá la misma

>> Así mismo en la celda tipo "Texto / Markdown" lo escribí de la misma manera, basta con entrar en el "modo de edición" de dicha celda para ver esta parte

#### *1.1.5.3. Listas dentro de otras listas:*

Un ejemplo de una lista donde incluyamos listas dentro de una lista misma:

[
    Palabra,
    [lista,dentro,de,otra,lista],
    Texto para separar listas,
    [Texto de ejemplo,palabra,Texto dentro de una lista dentro de otra lista],
    palabra,
    texto para terminar la lista
]


```python
[
    "Palabra",
    ["lista","dentro","de","otra","lista"],
    "Texto para separar listas",
    ["Texto de ejemplo","palabra","Texto dentro de una lista dentro de otra lista","palabra"],
    "Palabra",
    "Texto para terminar la lista"
]
```




    ['Palabra',
     ['lista', 'dentro', 'de', 'otra', 'lista'],
     'Texto para separar listas',
     ['Texto de ejemplo',
      'palabra',
      'Texto dentro de una lista dentro de otra lista',
      'palabra'],
     'Palabra',
     'Texto para terminar la lista']



#### *1.1.5.4. Listas combinando diferentes tipos de datos:*

Un ejemplo de una lista donde incluyamos diferentes tipos de datos dentro de una misma lista (incluyendo listas dentro de la misma)

["Palabra", 1234, "Texto de ejemplo", [25, 65, 87, "Palabra", "Texto de ejemplo], 48.32, 6874.95, 64, ["Palabra", 2415.359, 45, 9784.65,0], "Texto para terminar la lista]


```python
[
    "Palabra",
    1234,
    "Texto de ejemplo",
    [25, 65, 87, "Palabra", "Texto de ejemplo"],
    48.32, 6874.95, 64,
    ["Palabra", 2415.359, 45, 9784.65,0],
    "Texto para terminar la lista"
]
```




    ['Palabra',
     1234,
     'Texto de ejemplo',
     [25, 65, 87, 'Palabra', 'Texto de ejemplo'],
     48.32,
     6874.95,
     64,
     ['Palabra', 2415.359, 45, 9784.65, 0],
     'Texto para terminar la lista']



Como podemos ver, independientemente del tipo de dato, cualquier elemento puede ser incluido en una lista; pero, uno debe tener el contexto del uso al que se le dará dicha lista

### *1.1.6. Tipo de dato "dict":*

#### *1.1.6.1. Descripción del tipo de dato:*

Este tipo de dato hace referencia a aquellos que contienen un enlistado de palabras; pero, que se comportan como un "diccionario" (cada "entrada" cuenta con su respectiva "información gramatical")

Estos deben estar escritos **"entre dos llaves {}, cada "entrada" seguida del símbolo ":", después la "información gramatical" y por cada entrada, éstas siendo separadas mediante una coma ,"**

#### *1.1.6.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code":*

Un ejemplo donde solamente agreguemos datos de tipo "string" para crear el "diccionario":

{
    Entrada : información gramatical,
    Entrada 2 : información gramatical,
    Entrada 3 : información gramatical,
    Entrada 4 : información gramatical,
    Entrada 5 : información gramatical
}


```python
{
    "Entrada" : "información gramatical",
    "Entrada 2" : "información gramatical",
    "Entrada 3" : "información gramatical",
    "Entrada 4" : "información gramatical",
    "Entrada 5" : "información gramatical"
}
```




    {'Entrada': 'información gramatical',
     'Entrada 2': 'información gramatical',
     'Entrada 3': 'información gramatical',
     'Entrada 4': 'información gramatical',
     'Entrada 5': 'información gramatical'}



#### *1.1.6.3. Diccionarios dentro de otros diccionarios:*

Un ejemplo donde agreguemos "diccionarios" dentro de otro "diccionario":

{
    Entrada : información gramatical,
    Entrada 2: información gramatical,
    Subentradas : {Subentrada : información gramatical, Subentrada 2 : información gramatical, Subentrada 3 : Información gramatical},
    Última entrada : Información gramatical
    }


```python
{
    "Entrada" : "información gramatical",
    "Entrada 2": "información gramatical",
    "Subentradas" : {"Subentrada" : "información gramatical", "Subentrada 2" : "Información gramatical", "Subentrada 3" : "Información gramatical"},
    "Última entrada" : "Información gramatical"
}
```




    {'Entrada': 'información gramatical',
     'Entrada 2': 'información gramatical',
     'Subentradas': {'Subentrada': 'información gramatical',
      'Subentrada 2': 'Información gramatical',
      'Subentrada 3': 'Información gramatical'},
     'Última entrada': 'Información gramatical'}



>> En este caso, para poder agregar diccionarios dentro de otros diccionarios, es importante "asignarles una entrada" antes de abrir las "llaves {}" del nuevo diccionario; ya que, en caso de no hacerlo, Python no podrá interpretar correctamente el "nuevo diccionario" y arrojará un error

#### *1.1.6.4. Diccionarios con diferentes tipos de datos:*

Al igual que con los datos de tipo **"list" (listas)**, los **"diccionarios"** SI PUEDEN incluir diferentes tipos de datos dentro del mismo, siguiendo las mismas reglas de cada tipo de dato:

{
    "Entrada de lista" : [10001010, 10101011, 11001010, 11101000],
    "Entrada 1" : 10001010,
    "Entrada 2" : 10101011,
    "Entrada 3" : 11001010,
    "Entrada 4" : 11101000,
    "Entrada de otro diccionario" : {"Número entero" : 5864, "Número decimal" : 3684.14, "Dato tipo 'int'": 485, "Dato tipo 'float'" : 5843.14},
    "Entrada 5" : 5864,
    "Entrada 6" : 3684.14,
    "Entrada 7" : 485,
    "Entrada 8" : 5843.14,
}


```python
{
    "Entrada de lista" : [10001010, 10101011, 11001010, 11101000],
    "Entrada 1" : 10001010,
    "Entrada 2" : 10101011,
    "Entrada 3" : 11001010,
    "Entrada 4" : 11101000,
    "Entrada de otro diccionario" : {"Número entero" : 5864, "Número decimal" : 3684.14, "Dato tipo 'int'": 485, "Dato tipo 'float'" : 5843.14},
    "Entrada 5" : 5864,
    "Entrada 6" : 3684.14,
    "Entrada 7" : 485,
    "Entrada 8" : 5843.14,
}
```




    {'Entrada de lista': [10001010, 10101011, 11001010, 11101000],
     'Entrada 1': 10001010,
     'Entrada 2': 10101011,
     'Entrada 3': 11001010,
     'Entrada 4': 11101000,
     'Entrada de otro diccionario': {'Número entero': 5864,
      'Número decimal': 3684.14,
      "Dato tipo 'int'": 485,
      "Dato tipo 'float'": 5843.14},
     'Entrada 5': 5864,
     'Entrada 6': 3684.14,
     'Entrada 7': 485,
     'Entrada 8': 5843.14}



>> Así como lo mencioné en el anterior apartado, SIEMPRE hay que tener una justificación o entender correctamente el contexto en el que se van a agregar listas dentro de listas, diccionarios dentro de diccionarios y la combinación de diferentes tipos de datos dentro de listas o diccionarios

---

> IMPORTANTE: Hay que recordar que, independientemente de que se esté creando una lista o diccionario, es OBLIGATORIO escribir los datos de tipo "string" " entre comillas "" o tildes '' " cuando éstos sean escritos dentro de una línea de código; ya que, Python sigue las mismas "reglas" que he mencionado acerca de los diferentes tipos de datos y, en caso de no seguirlas, Python no sabrá como interpretar dichos datos y arrojará un error de "Sintaxis"

> En ambos casos de listas y diccionarios, NO ES POSIBLE agregar datos de tipo "bool"; ya que, Python no permite el crear este tipo de datos dentro de listas o diccionarios

---

## *1.2. ¿Cómo saber si Python interpretó correctamente cada tipo de dato?*

### *1.2.1. Interpretación correcta del tipo de dato:*

Para saber si cada tipo de dato fue interpretado correctamente por Python, al momento de ejecutar las celdas de tipo " Código / Code " apareció un " checkmark ✔ " en la esquina inferior de la misma celda.

Esto, lo podemos observar en algunos de los ejemplos que coloqué en cada uno de los tipos de datos

### *1.2.2. Interpretación erronea del tipo de dato:*

Al momento de no colocar los signos necesarios para cada tipo de dato, Python arroja un error donde intentó interpretar una palabra, letra, número, etc...; como una " sintaxis " para una función o formula entre los mismos caracteres.

De igual manera, podemos observar que en algunas celdas de tipo " Código / Code " donde intencionalmente coloqué mal los tipos de datos; al ejecutarlas apareció una " cruz x " en la esquina inferior izquierda de la celda, y Python arrojó la explicación del error y lo que mencioné de la " sintaxis "

---

# **2. Tipos de variables en Python para el análisis básico de datos**

## *2.1. Variables en Python:*

### *2.1.1. ¿Cómo definir una variable en Python?*

#### *2.1.1.1. Declaración de variables:*

Para definir una variable en Python, *basta con asignarle un **" nombre "** a la variable, seguido del signo **" = "** y finalmente el **valor, texto, oración, etc...***; que uno desea *" almacenar "* en dicha variable.

Teniendo un resultado como: **" variable_n = 1234 ", " variable_t = "número" ", "variable_o = "palabra otra palabra más palabras etc..."**, etc... 

>> En los siguientes apartados explico más a detalle como definir cada tipo de variables

---

> IMPORTANTE: Una vez " declarada una o más variables " en Python, éstas serán guardadas en el mismo archivo HASTA QUE SE CIERRE.

> Por lo que, si uno necesita trabajar otra vez con estas variables al abrir el archivo, se necesita ejecutar otra vez las " líneas de código donde se definir dichas variables ", lo que permitirá trabajar nuevamente con ellas.

> Pero, en dado caso de que éstas no se ejecuten, Python arrojará un error donde mencionará que dicha variable " no ha sido declarada "; esto, a pesar de que exista la " línea de código " con dicha variable

> Cabe aclarar que en este cuadernillo todavía no entraré en el aspecto de las funciones para visualizar o realizar operaciones entre las variables; por lo que, me enfocaré solamente en como definirlas correctamente y evitar errores en Python

---

#### *2.1.1.2. Límite para el nombre de una variable:*

El " límite de un nombre o dato " para una variable realmente depende de que tipo de dato o información necesites almacenar en la misma.

En el caso del **" límite para el nombre de una variable "**, lo único que hay que tener a consideración, es que **NO SE PUEDEN UTILIZAR ESPACIOS**; por lo que, si necesitas colocar *una o más palabras a dicha variable*, éstas **OBLIGATORIAMENTE** necesitan estar separadas por un " guión bajo _ ". Esto, para evitar que Python arrojé un error y nos permita almacenar dicha variable.

Ejemplo : " variable_de_ejemplo_para_el_límite = ejemplo "


```python
variable_de_ejemplo_para_el_límite = "ejemplo"
```

---

> IMPORTANTE: En el caso del límite para las variables, depende del " tipo de dato " que se quiera almacenar en las mismas; por lo que, esta parte la abarcaré en los apartados de cada tipo de dato

---

#### *2.1.1.3. ¿Cómo saber si mi variable se guardó correctamente?*

Para saber *si la variable declarada se guardó correctamente*, basta con ejecutar la **" línea de código "** y asegurarnos de que debajo de la misma variable aparezca un **" checkmark "** junto al número *que indica el tiempo que tardó la misma línea para ejecutarse* (como lo que se vió en los ejemplos en las celdas de tipo "Código / Code" de los tipos de datos).

#### *2.1.1.4. ¿Se pueden definir varias variables con el mismo nombre?*

En terminos simples, NO ESTÁ PERMITIDO de ninguna manera definir variables con un mismo nombre; ya que, en cualquier "entorno de programación" utilizado para: desarrollo web, back end, front end, etc... (incluyendo el análisis de datos); esta práctica resulta contraproducente y puede provocar bastante errores al momento de ejecutar el código

>> Por eso mismo, hago mucho hincapié en la estandarización del uso de signos, mayúsculas y otro elementos al momento de generar una base de datos y/o definir variables

---

### *2.1.2. Tipos de variables básicas en Python:*

#### *2.1.2.1. Variable de tipo "int"*

##### *2.1.2.1.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos tipo **"int"**; para definir una variable de este tipo, basta con asignarle un **"número entero sin decimales"**:

##### *2.1.2.1.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code":*

**Ejemplo: a = 1220**


```python
a = 1220
```

##### *2.1.2.1.3. Límite del tipo de variable "int":*

El *límite de este tipo de datos* se basa en el número entero que se quiera **"almacenar"** en dicha variable; pero, recordando el **límite de caracteres que puede mostrar Python**

> Dicho límite lo menciono en el cuadernillo: " Apuntes sobre operaciones matemáticas "

---

> IMPORTANTE: NO se pueden guardar números que inicien con " 0 " (010, 020, 030, etc...); ya que, Python los considerará como números decimales o directamente arroja un error indicando que "NO ESTÁ PERMITIDO" usar ese "tipo de números"

---

#### *2.1.2.2. Variable de tipo "float":*

##### *2.1.2.2.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos tipo **"float"**; para definir una variable de este tipo, basta con asignarle un **"número con "n" cantidad de decimales"**:

##### *2.1.2.2.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code":*

Ejemplo 1: b = 3.1416


```python
b = 3.1416
```

**Ejemplo 2: c = 684.0**


```python
c = 684.0
```

>> Como mencioné anteriormente en el apartado de los datos de tipo "float"; estos también incluyen aquellos en los que se tiene un número junto al decimal de valor nulo: ".0"

**Ejemplo 3: d = 9543674.00007**


```python
d = 9543674.00007
```

##### *2.1.2.2.3. Límite del tipo de variable "float":*

El límite de este tipo de datos es igual que las variables de tipo "int"

---

> IMPORTANTE: Al momento de guardar este tipo de variables, Python no redondeará dichos números; ésto, solamente se puede realizar mediante la función: ".round()" que mencioné en el cuadernillo: "Apuntes sobre operaciones matemáticas" 

---

#### *2.1.2.3. Variable tipo "string":*

##### *2.1.2.3.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos tipo **"string"**; para definir una variable de este tipo, basta con asignarle **" una palabra o texto entre comillas "_" "**:

##### *2.1.2.3.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code"*

**Ejemplo 1 - Variable de una palabra: e = "palabra"** 


```python
e = "palabra"
```

**Ejemplo 2 - Variable de dos o más palabras: f = "Hola mundo"**


```python
f = "Hola mundo"
```

**Ejemplo 3 - Variable de texto: g = "Mi nombre es _ y me dedico a _"**


```python
g = "Mi nombre es _ y me dedico a _"
```

**Ejemplo 4 - Variable de texto: h = "MIS HOBBIES SON: _ Y EN MIS TIEMPOS LIBRES ME GUSTA_"**


```python
h = "MIS HOBBIES SON: _ Y EN MIS TIEMPOS LIBRES ME GUSTA_"
```

---

> IMPORTANTE: Como se puede ver, en las variables de texto tambien pueden ir caracteres o signos, SIEMPRE Y CUANDO se escriban entre las comillas ""; en caso de escribir cualquier signo fuera de las mismas comillas, estos serán considerados como una " operación matemática " dentro de la misma variable. 

> Estos casos los retomaré en el cuadernillo de las funciones para poder mostrar las combinaciones y operaciones entre variables y demás; ya que, en este tipo de variables también pueden insertarse otras variables con otra función

---

##### *2.2.2.3.3. Límite del tipo de variable "string":*

El límite de este tipo de datos, se basa tanto en el límite de caracteres que Python puede mostrar, como de la cantidad de texto que se coloque **" ENTRE LAS COMILLAS "" "**; todo texto, símbolo, número o cualquier otro elemento que se encuentre fuera de estas, no se considerará como datos de tipo "string"

#### *2.1.2.4. Variables de tipo "bool":*

##### *2.1.2.4.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos de tipo **"bool"**; para definir una variable de este tipo, basta con asignarle **"una comparación entre datos de cualquier tipo"** (incluyendo listas y diccionarios)

>> Como mencioné anteriormente, los "operadores" para realizar los comparadores los desarrollaré en el apartado: "3."

##### *2.1.2.4.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code":*

Ejemplo 1: 

i = "Texto de ejemplo para hacer comparativas entre datos de tipo "string"" == "Texto de ejemplo para hacer comparativas entre datos de tipo "string""


```python
i = "Texto de ejemplo para hacer comparativas entre datos de tipo 'string'" == "Texto de ejemplo para hacer comparativas entre datos de tipo 'string'"
```

Ejemplo 2:

j = 14756 >= 14750


```python
j = 14756 >= 14750
```

Ejemplo 3:

k = [Lista del super, Lista de la tienda, Lista de locales] == [Lista del super, Lista de la tienda, Lista de locales]


```python
k = ["Lista del super", "Lista de la tienda", "Lista de locales"] == ["Lista del super", "Lista de la tienda", "Lista del mercado"]
```

Ejemplo 4:

l = {
    Lista del super : Compras realizadas en Wallmart
    Lista de la tienda : Compras realizadas en Miscelanea Doña Teresa
    Lista de locales : Compras realizadas en Verduleria Don Toño
} > {
    Lista del super : Compras en Wallmart
    Lista de la tienda : Compras en Miscelanea Doña Teresa
    Lista de locales : Compras en Verduleria Don Toño
}


```python
l = {
    "Lista del super" : "Compras realizadas en Wallmart",
    "Lista de la tienda" : "Compras realizadas en Miscelanea Doña Teresa",
    "Lista de locales" : "Compras realizadas en Verduleria Don Toño"
} == {
    "Lista del super" : "Compras en Wallmart",
    "Lista de la tienda" : "Compras en Miscelanea Doña Teresa",
    "Lista de locales" : "Compras en Verduleria Don Toño"
}
```

>> Para ver el resultado de la comparativa de todos estos ejemplos se utiliza la función "print()"; pero, estos ejemplos los retomaré en el cuadernillo de funciones

##### *2.1.2.4.3. Límite del tipo de variable "bool":*

En el caso de las variables del tipo **"bool"**, *no existe un "límite" como tal*; pero, si hay una limitante en cuanto a los signos para hacer las comparativas **en el caso de las listas y diccionarios**

>> Dicha limitante la explico más a detalle en el apartado: "Extra"

#### *2.1.2.5. Variables de tipo "list":*

##### *2.1.2.5.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos de tipo "list"; para definir una variable de este tipo, basta con asignarle "un conjunto datos de cualquier tipo entre corchetes []":

##### *2.1.2.5.2. Ejemplos en celdas de tipo "Texto /Markdown" y "Código / Code"*

Ejemplo : 
Listas_de_compra = [
    1era lista,
    [Listas del super, Paquete de leche, Cartón de huevos, Ketchup, Mayonesa, Jabón del baño, Jabón para el cuerpo, Shampoo, Jabón para la cocina],
    Cantidades de la primera lista,
    [2, 4, 2, 3, 2, 2, 2, 1, 2],
    2da lista,
    [Lista de la tienda, 40 de Jamón, 50 de queso Oaxaca, 20 de queso manchego, 1 refresco, 1 paquete de tortillas de harina],
    3ra lista,
    [Lista de locales, Tortilla de maiz, Arroz, Pasta, Tomate, Surtido de verduras, Jitomate, Cebolla, Limón],
    Cantidades de la tercera lista (en kg),
    [1.5, 2.5, 5.0, 4.5, 10.0, 3.5, 2.0, 2.0]
]


```python
Listas_de_compra = [
    "1era lista",
    ["Listas del super", "Paquete de leche", "Cartón de huevos", "Ketchup", "Mayonesa", "Jabón del baño", "Jabón para el cuerpo", "Shampoo", "Jabón para la cocina"],
    "Cantidades de la primera lista",
    [2, 4, 2, 3, 2, 2, 2, 1, 2],
    "2da lista",
    ["Lista de la tienda", "40 de Jamón", "50 de queso Oaxaca", "20 de queso manchego", "1 refresco", "1 paquete de tortillas de harina"],
    "3ra lista",
    ["Lista de locales", "Tortilla de maiz", "Arroz", "Pasta", "Tomate", "Surtido de verduras", "Jitomate", "Cebolla", "Limón"],
    "Cantidades de la tercera lista (en kg)",
    [1.5, 2.5, 5.0, 4.5, 10.0, 3.5, 2.0, 2.0]
]
```

##### *2.1.2.5.3. Límite de la variable "list":*

Las variables de tipo **"list"**, nuevamente estan límitadas en la cantidad de caracteres que Python puede mostrar; sin embargo, cabe recordar que **OBLIGATORIAMENTE** se tienen que respetar las **"reglas"** establecidas para que Python pueda **"interpretar"** correctamente cada tipo de dato dentro de la lista

#### *2.1.2.6. Variables de tipo "dict"*

##### *2.1.2.6.1. Descripción del tipo de variable:*

Siguiendo la explicación de los datos de tipo **"dict"**; para definir una variable de este tipo, basta con asignarle **"un conjunto de datos de cualquier tipo entre llaves {}"**, recordando que a cada **"entrada"** hay que asignarle su respectiva **"información gramatical"**

##### *2.1.2.6.2. Ejemplos en celdas de tipo "Texto / Markdown" y "Código / Code":*

Ejemplo:
{
    Listas de compras y locales : {Lista del super : Wallmart, Lista de la tienda : Miscelanea Doña Teresa, Lista de locales : Verdularia Don Toño},
    Lista del super : [Paquete de leche, Cartón de huevos, Ketchup, Mayonesa, Jabón del baño, Jabón para el cuerpo, Shampoo, Jabón para la cocina],
    Cantidades de la lista del super: [2, 4, 2, 3, 2, 2, 2, 1, 2],
    Lista de la tienda : [Jamon, Queso Oaxaca, Queso manchego, Refresco, Paquete de tortillas de harina],
    Cantidades de la lista de la tienda : [40, 50, 20, 1, 1],
    Lista de locales: [Tortillas de maíz, Arroz, Pasta, Tomate, Surtido de verduras, Jitomate, Cebolla, Limón],
    Cantidades de la lista de locales (en kg) : [1.5, 2.5, 5.0. 4.5, 10.0, 3.5, 2.0, 2.0]
}


```python
{
    "Listas de compras y locales" : {"Lista del super" : "Wallmart", "Lista de la tienda" : "Miscelanea Doña Teresa", "Lista de locales" : "Verdularia Don Toño"},
    "Lista del super" : ["Paquete de leche", "Cartón de huevos", "Ketchup", "Mayonesa", "Jabón del baño", "Jabón para el cuerpo", "Shampoo", "Jabón para la cocina"],
    "Cantidades de la lista del super" : [2, 4, 2, 3, 2, 2, 2, 1, 2],
    "Lista de la tienda" : ["Jamon", "Queso Oaxaca", "Queso manchego", "Refresco", "Paquete de tortillas de harina"],
    "Cantidades de la lista de la tienda" : [40, 50, 20, 1, 1],
    "Lista de locales": ["Tortillas de maíz", "Arroz", "Pasta", "Tomate", "Surtido de verduras", "Jitomate", "Cebolla", "Limón"],
    "Cantidades de la lista de locales (en kg)" : [1.5, 2.5, 5.0, 4.5, 10.0, 3.5, 2.0, 2.0]
}
```




    {'Listas de compras y locales': {'Lista del super': 'Wallmart',
      'Lista de la tienda': 'Miscelanea Doña Teresa',
      'Lista de locales': 'Verdularia Don Toño'},
     'Lista del super': ['Paquete de leche',
      'Cartón de huevos',
      'Ketchup',
      'Mayonesa',
      'Jabón del baño',
      'Jabón para el cuerpo',
      'Shampoo',
      'Jabón para la cocina'],
     'Cantidades de la lista del super': [2, 4, 2, 3, 2, 2, 2, 1, 2],
     'Lista de la tienda': ['Jamon',
      'Queso Oaxaca',
      'Queso manchego',
      'Refresco',
      'Paquete de tortillas de harina'],
     'Cantidades de la lista de la tienda': [40, 50, 20, 1, 1],
     'Lista de locales': ['Tortillas de maíz',
      'Arroz',
      'Pasta',
      'Tomate',
      'Surtido de verduras',
      'Jitomate',
      'Cebolla',
      'Limón'],
     'Cantidades de la lista de locales (en kg)': [1.5,
      2.5,
      5.0,
      4.5,
      10.0,
      3.5,
      2.0,
      2.0]}



>> Como podemos ver en este ejemplo, el "diccionario" quedó bastante grande y Python no pudo mostrar todos los elementos escritos dentro del mismo

##### *2.1.2.6.3. Límite de la variable "dict":*

Las variables de tipo **"dict"** están límitadas de la misma manera que las variable de tipo **"list"**; de igual manera, **OBLIGATORIAMENTE** se deben de seguir las **"reglas"** para que Python pueda **"interpretar"** cada tipo de dato correctamente dentro del **"diccionario"**

---

# **3. Operadores utilizados para generar datos y variables de tipo "bool"**

## *3.1. Operadores utilizados para realizar comparativas entre datos y variables:*

Los diferentes operadores que Python acepta para poder realizar comparativas entre los datos y variables son:

- **">"** - Operador que hace referencia a la comparación **"Mayor que"**, usado como: **"a es mayor que b"**

- **"<"** Operador que hace referencia a la comparación **"Menor que"**, usado como: **"a es menor que b"**

- **">="** Operadores que hacen referencia a la comparación **"Mayor o igual que"**, usados como: **"a es mayor o igual que b"**

- **"<="** Operadores que hacen referencia a la comparación **"Menor o igual que"**, usados como: **"a es menor o igual que b"**

- **"!="** Operadores que hacen referencia a la comparación **"Diferente a / que"**, usados como: **"x es diferente a / que y"**

- **"=="** Operadores que hacen referencia a la comparación **"Igual a / que"**, usados como: **"x es igual a / que y"**

## *3.2. Operadores utilizados para realizar comparativas entre datos y variables de tipo "list" y "dict":*

Pero, como mencioné en los ejemplos para la creación de datos tipo "bool" en el caso de las comparativas entre datos tipo "list" y "dict" (listas y diccionarios); los únicos operadores que Python permite para realizar comparativas entre estos dos tipos de datos son:

- **"!="** - El operador que realiza la comparativa de **"Diferente a / que"**

- **"=="** - El operador que realiza la comparativa de **"Igual a / que"** 

---

> IMPORTANTE: Así como lo menciono en la declaración d variables, es MUY IMPORTANTE el decidir o estandarizar el uso de mayúsculas, nombres, signos y tildes para evitar que, al momento de realizar cualquier tipo de comparativa, Python no tenga problemas al momento de generar el resultado de "Verdadero / True" o "Falso / False"; al igual que, evitar confuciones o una mala interpretación de datos 

> Esto que menciono, está relacionado a la existencia de los términos "coincidencia exacta del identificador / case sensitive"; los cuales son los que permiten que cualquier variable declarada sea "única". Por lo que, si uno quiere "llamar" a cualquier variable previamente declarada en otra parte del documento, SE DEBERÁ ESCRIBIR EXACTAMENTE IGUAL a como fue declarada

> Y, en caso de escribir CUALQUIER CARÁCTER diferente de la variable, Python automáticamente arrojará un error mencionando que dicha variable no existe

---

# Extra

# "1. "Tipos de datos en Python utilizados para el análisis básico de datos"

1. Tanto en este apartado como en el "2." quise resaltar mucho la parte de la escritura de los ejemplos en celdas de tipo "Código / Code"; ya que, al inicio puede ser bastante confuso el porque Python nos arroja tantos errores al momento de querer generar datos de cualquier tipo.

2. Por eso mismo, escribí el apartado "1.2. ¿Cómo saber si Python interpretó correctamente cada tipo de dato?"; ya que, cuando Python arroja el error de "Sintaxis" al principio puede no entenderse exactamente a que se refiere

# "2. Tipos de variables en Python para el análisis básico de datos"

1. Así como en el antarior apartado, quise hacer demasiado hincapié en la estandarización y organización de los diferentes elementos que se vayan a utilizar al momento de realizar un análisis de datos o en general en la programación en el "entorno" de Python; ya que, es muy fácil cometer errores o perderse al momento de definir demasiadas variables que, por la misma situación de olvidarse de escribir correctamente la misma, puede generar mucha confusión y desesperación el no entender porque arroja el mismo error una y otra vez

> En ambos apartados, cuando me refiero a algunos elementos como "básicos", me refiero a elementos que uno puede encontrar en cualquier curso, video, tutorial, etc... de principiantes que puede encontrar al momento de querer introducirse en el análisis de datos

# "3. Operadores utilizados para generar datos y variables de tipo "bool"" 

1. Este apartado lo cree con la intención de iniciar un poco la parte de funciones; ya que, en el siguiente cuadernillo detallaré y realizaré muchos ejemplos (tanto exitosos como erroneos) de las diferentes funciones que se pueden realizar en el "entorno de programación" de Python; ya que, es muy importante el saber como funcionan y el como se desarrollan cada una de las "sintaxis" de dichas funciones para poder ejecutarlas correctamente

2. Por otro lado, así como en el cuadernillo de "Apuntes sobre operaciones matemáticas", este tipo de "operaciones" siguen siendo las más "básicas" al momento de programar o adentrarse en el tema de "Análisis de datos en Python"
