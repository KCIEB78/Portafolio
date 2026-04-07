# **Archivo referente a los diferentes tipos de textos que se pueden insertar en Python**

1. Para insertar un texto, en Google Colab y Visual Studio Code, basta con ir a la barra de herramientas y dar clic en la herramienta " + Texto "

2. Para insertar un texto en Anaconda - JupyterLab, basta con agregar un bloque con el símbolo " + ", predeterminadamente el bloque se genera de tipo " Código "; para cambiar el tipo, basta con ir a la misma barra de herramientas y abrir el menú desplegable del recuadro donde dice " Code " y seleccionar " Markdown "

---

# **1. Inserción de títulos y subtítulos**

Para la inserción de títulos o subtítulos, basta con escribir un " # " al iniciar la " línea de código "; quedando la jerarquización de los mismos de la siguiente manera:

- Título principal: Escribir un solo " # " - # Título de ejemplo

- Subtítulo de " primer nivel ": Escribir dos " # " - ## Subtítulo de ejemplo

- Subtítulo de " segundo nivel ": Escribir tres " # " - ### Subtítulo de ejemplo

- Subtítulo de " tercer nivel ": Escribir cuatro " # " - #### Subtítulo de ejemplo

- Subtítulo de " cuarto nivel ": Escribir cinco " # " - ##### Subtítulo de ejemplo

- Subtítulo de " quinto nivel ": Escribir seis " # " - ###### Subtítulo de ejemplo

El " quinto nivel " de subtítulos es el último permitido de Python, si se ejecuta la línea con más de seis " # ":

####### Subtítulo de ejemplo en caso de escribir más de seis " # "

---

# **2. Inserción de texto, listas de texto, formatos de texto**

## **2.1. Inserción de un " texto simple "**

Para agregar un texto " simple ", basta con escribirlo en el mismo bloque (asegurándose de que el " tipo de bloque " sea " Texto " o " Markdown ")

## **2.2. Listas de texto, símbolos permitidos y NO permitidos**

Para iniciar una " lista de texto ", basta con agregar los símbolos que se utilizarían para una operación de **SUMA, RESTA Y MULTIPLICACIÓN, ANTES** del texto:

### *2.2.1. Símbolos permitidos para realizar una " lista de elementos / texto ":*

- Primer elemento de la lista donde se escribió un " - " al inicio

+ Segundo elemento de la lista donde se escribió un " + " al inicio

* Tercer elemento de la lista donde se escribió un " * " al inicio

Estos primeros elementos de la lista automáticamente el entorno aplica un color " naranja " al símbolo escrito y convirtiéndolo en un " • " (Punto alto) al momento de " ejecutar " el bloque

### *2.2.2. Símbolos NO permitidos para realizar una " lista de elementos / texto ":*

#### Cuarto elemento de la lista; pero, al escribir uno o más " # " al inicio, lo considera un título o subtítulo

/ Quinto elemento de la lista; pero, que no acepta la " / " al inicio para considerarlo como ícono de una " lista "

\ Sexto elemento de la lista; pero, que no acepta la " \ " al inicio para considerar como ícono de una " lista "

= Séptimo elemento de la lista; pero, que no acepta el " = " al inicio para considerarlo como ícono de una " lista "

< Octavo elemento de la lista; pero, que no acepta el " < " al inicio para considerarlo como ícono de una " lista "

~ Noveno elemento de la lista; pero, que no acepta el " ~ " al inicio para considerarlo como ícono de una " lista "

***Estos elementos de la lista solamente son ejemplos en dado caso de escribir otros símbolos aparte***

### *2.2.3. Símbolos especiales aplicables:*

> Décimo elemento de la lista; pero, que al momento de escribir un " > " lo considera una " cita de código "

Este elemento que genera una " cita de código " se utiliza en diferentes contextos, más abajo en otro apartado menciono los usos y ejemplos

◦ Undécimo elemento de la lista donde se escribió un " ◦ " (Círculo vacío) al inicio

→ Duodécimo elemento de la lista donde se escribió una " → " al inicio

✔ Décimo tercer elemento de la lista donde se escribió un " ✔ " al inicio

🔹 Décimo cuarto elemento de la lista donde se escribió un " 🔹 " al inicio

✅ Décimo quinto elemento de la lista donde se escribió un " ✅ " al inicio

⚠ Décimo sexto elemento de la lista donde se escribió un " ⚠ " al inicio

Estos elementos al ser " símbolos especiales ", aunque el " entorno " si los acepta y los " ejecuta " tal cual como son, lo recomendable es solamente usarlos en documentaciones o archivos donde solamente se realicen " notas " o inclusive " manuales de uso "

De igual manera si se quieren colocar, recomiendo encarecidamente buscarlos en Internet para simplemente poder copiarlos y pegarlos; ya que, algunos no cuentan con una combinación de letras del " Código ASCII " que permita insertarlos

### *2.2.4. Directamente colocar el " punto alto " • para escribir una " lista de elementos / texto ":*


• Décimo séptimo elemento de la lista donde se escribió directamente un " • " (Punto alto) al inicio

## **2.3. Formatos de texto**

### *2.3.1. Formato de texto " NEGRITAS ":*

#### *2.3.1.1. Aplicación en todo el texto:*

Para aplicar el formato de texto **" negritas "**, basta con agregar dos " * " **AL INICIO, AL FINAL Y PEGADO al mismo texto**:

- **Texto en negritas de ejemplo donde se aplica correctamente el formato de texto " Negritas "**

- ** Texto de ejemplo en donde NO se aplica el formato de texto " Negritas"**

- **Texto de ejemplo en donde NO se aplica el formato de texto " Negritas " **

#### *2.3.1.2. Aplicación en títulos y subtítulos:*

Para aplicar el formato de texto **" Negritas "** a **títulos o subtítulos**, basta con escribirlo después del **" # "**:

###### **Título o subtítulo de ejemplo donde se aplica correctamente el formato de texto " Negritas "**

###### **Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Negritas " **

###### ** Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Negritas "**

#### *2.3.1.3. Aplicación en medio de textos, títulos y subtítulos:*

Para aplicar el formato de texto " Negritas " en medio de textos, títulos o subtítulos, basta con escribir los " * " **PEGADOS A LA PRIMERA Y ÚLTIMA LETRA** de la palabra donde se quiera aplicar el formato; de igual manera, si se quisiera aplicar el formato a un conjunto de palabras, basta con escribir los " * " **PEGADOS A LA PRIMERA Y A LA ÚLTIMA LETRA** de las palabras del conjunto:

- Texto de ejemplo **donde se aplica correctamente** el formato de texto **" Negritas "** en medio

- Texto de ejemplo ** donde NO se aplica** el formato de texto** " Negritas "** en medio

###### Título o subtítulo de ejemplo **donde se aplica correctamente** el formato de texto **" Negritas "** en medio

###### Título o subtítulo de ejemplo **donde NO se aplica ** el formato de texto ** " Negritas " en medio

> En dado caso de haber caracteres como: paréntesis, corchetes, llaves, comillas, tildes, etc...; basta con escribir los " * " PEGADOS a los mismos para poder aplicar correctamente el formato

### *2.3.2. Formato de texto **" Cursiva "**:*

#### *2.3.2.1. Aplicación en todo el texto:*

Para aplicar el formato de texto " cursiva ", basta con agregar un solo " * " **AL INICIO, AL FINAL Y PEGADO** del mismo texto:

- *Texto de ejemplo donde se aplica correctamente el formato de texto " cursiva "*

- * Texto de ejemplo donde NO se aplica el formato de texto " cursiva "*

- *Texto de ejemplo donde NO se aplica el formato de texto " cursiva " *

#### *2.3.2.2. Aplicación en títulos y subtítulos:*

Para aplicar el formato de texto *" cursiva "* a *" títulos "* y *" subtítulos "*, basta con escribirlo después del *" # "*:

###### *Título o subtítulo de ejemplo donde se aplica correctamente el formato de texto " Cursiva "*

###### * Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Cursiva "*

###### *Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Cursiva " *

#### *2.3.2.3. Aplicación en medio de textos, títulos y subtítulos:*

Para aplicar el formato de texto " Cursiva " en medio de textos, títulos o subtítulos, basta con escribir el " * " **PEGADO A LA PRIMERA Y ÚLTIMA LETRA** de la palabra donde se quiera aplicar el formato; de igual manera, si se quisiera aplicar el formato a un conjunto de palabras, basta con escribir el " * " **PEGADO A LA PRIMERA LETRA Y A LA ÚLTIMA LETRA** de las palabras del conjunto:

- Texto de ejemplo *donde se aplica correctamente* el formato de texto " cursiva " en *medio*

- Texto de ejemplo * donde NO se aplica* el formato de texto " cursiva " *en * medio

###### Título o subtítulo de ejemplo *donde se aplica correctamente* el formato de texto *" cursiva "* en medio

###### Título o subtítulo de ejemplo * donde NO se aplica correctamente* el formato de texto *" cursiva " * en medio

> En dado caso de haber caracteres como: paréntesis, corchetes, llaves, comillas, tildes, etc...; basta con escribir los " * " PEGADOS a los mismos para poder aplicar correctamente el formato

### *<u>2.3.3. Formato de texto " subrayado ":* </u>

#### *2.3.3.1. Aplicación en todo el texto:*

Para aplicar el formato de texto " Subrayado " al texto, se debe de escribir una " Etiqueta HTML " que permite aplicar este tipo de formato; para esto, se debe de escribir: " < "," u ", " > " **AL INICIO** del texto; pero, para evitar que siga subrayando otras líneas de texto de abajo, se debe de escribir la otra " Etiqueta HTML ": " < ", " / ", " u ", " > " **AL FINAL** del texto para " cerrar " correctamente el formato:

> Escribí cada símbolo por separado tanto para " abrir ", como para " cerrar " el formato, para evitar que se aplicara y apareciera en el texto

- <u> Texto de ejemplo donde se abre la " Etiqueta HTML " y se cierra correctamente para aplicar el formato " Subrayado " </u>

- <u> Texto de ejemplo en donde se abre la " Etiqueta HTML "; pero,

NO SE CERRÓ correctamente, siendo este un texto escrito en una línea completamente aparte </u>

#### *2.3.3.2. Aplicación en títulos y subtítulos:*

Para aplicar el formato de texto " Subrayado " en títulos y subtítulos es necesario escribir la " Etiqueta HTML " para abrir el formato ("< "," u ", " > ") **DESPUÉS** del " # ", sin olvidar agregar la otra " Etiqueta HTML " (< ", " / ", " u ", " > ") **AL FINAL** para cerrarla correctamente:

###### <u>Título o subtítulo de ejemplo donde se aplica la " Etiqueta HTML " correctamente y se cierra </u>

###### <u> Título o subtítulo de ejemplo donde se aplica la " Etiqueta HTML "; pero

###### NO SE CERRÓ y sigue subrayando el subtítulo

o texto de otra línea </u>

#### *2.3.3.3. Aplicación en medio de textos, títulos y subtítulos:*

Para aplicar el formato de texto **" Subrayado "** en medio de textos, títulos o subtítulos **OBLIGATORIAMENTE** (lo menciono ya que hice las pruebas varias veces para detectar estos mismos " fallos / bugs "):

- La " Etiqueta HTML ": " < ", " u ", " > " **DEBE IR SEPARADA DE LA PRIMERA LETRA** de la palabra o conjunto de palabras que se quieran subrayar:

- La " Etiqueta HTML ": " < ", " / ", " u ", " > " **DEBE IR PEGADA A LA ÚLTIMA LETRA** de la palabra o conjunto de palabras que se quiera subrayar:

- Texto de ejemplo donde <u> se aplica el formato de subrayado</u> en <u> medio</u>

- Texto de ejemplo donde <u>no se agrega el " < ", " / ", " u ", " > " al final del texto que se quiera subrayar, lo mismo sucede si solamente se escribe " < " " u " " > " sin la " / " </u>

###### Título o subtítulo de ejemplo donde <u> se aplica correctamente</u> el formato "Subrayado" en <u> medio</u>

###### Título o subtítulo de ejemplo donde <u> NO se aplica el formato "Subrayado" en medio de manera correcta</u>

> En caso de querer agregar otro " < "," u ", " > " en medio de palabras, textos, títulos o subtítulos, se tiene el mismo problema en caso de no cerrar correctamente el subrayado y el " entorno " no detecta correctamente donde cerrar el mismo

### *~~2.3.4. Formato de texto " Tachado "~~*

#### *2.3.4.1. Aplicación en todo el texto:*

Para aplicar el formato de texto " Tachado ", basta con escribir dos veces el símbolo " ~ " (ALT + 126) **PEGADOS A LA PRIMERA Y ÚLTIMA PALABRA** del mismo:

- ~~Texto de ejemplo donde se aplica correctamente el formato de texto " Tachado " donde se escribieron los " ~ " pegados al texto~~

- ~~ Texto de ejemplo donde se escribieron los " ~ " separados del texto ~~

- ~~ Texto de ejemplo donde NO se aplica el formato de texto " Tachado "~

- ~ Texto de ejemplo donde NO se aplica el formato de texto " Tachado "~~

> En este caso, al momento de escribir ambos " ~ " separados del texto, el " entorno " si muestra la previsualización del formato; pero, no lo aplica correctamente como se puede ver

#### *2.3.4.2. Aplicación en títulos y subtítulos:*

Para aplicar el formato de texto " Tachado " a un título y subtítulo, **OBLIGATORIAMENTE** debe de ir **DESPUÉS** del " # "

###### ~~Título o subtítulo de ejemplo donde se aplica correctamente el formato de texto " Tachado "~~

###### ~Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Tachado " ~~

###### ~~ Título o subtítulo de ejemplo donde NO se aplica el formato de texto " Tachado "~

#### *2.3.4.3. Aplicación en medio de textos, títulos y subtítulos*

En dado caso de querer aplicarlo en medio de un texto, basta con agregar ambos " ~ " **PEGADOS** a las palabras donde se quiera aplicar el formato

- Texto de ejemplo ~~donde se aplica correctamente~~ el formato de texto " Tachado " en ~~medio~~.

- Texto de ejemplo ~~ donde NO se aplica~ el formato de texto " Tachado " ~en ~~ medio.

- Texto de ejemplo ~donde NO se aplica ~~ el formato de texto  ~~" Tachado " ~en medio.

En dado caso de querer aplicarlo en medio de títulos o subtítulos, basta con agregar ambos " ~ " **PEGADOS** a las palabras donde se quiera aplicar el formato

###### Título o subtítulo de ejemplo ~~donde se aplica correctamente~~ el formato de texto " Tachado " en ~~medio~~

###### Título o subtítulo de ejemplo ~ donde NO se aplica correctamente~~ el formato de texto ~~" cursiva " ~ en medio

## **2.4. Combinación de formatos:**

#### *2.4.1. Combinación de formatos en texto:*

Para " abrir " correctamente la combinación de formatos, basta con seguir esta jerarquización:

- **PRIMERO** se escriben los " * " para poder aplicar correctamente los formatos de texto **" Negritas "** y *" Cursiva "*

- **DESPUÉS** se escriben los " ~ " para poder aplicar correctamente el formato de texto **~~" Tachado "~~**

- **Y AL FINAL** se escribe la " Etiqueta HTML ": **" < "," u ", " > "**

Y para " cerrar " correctamente cada uno de los formatos, la jerarquización se aplica de manera inversa:

- **PRIMERO** se escribe la " Etiqueta HTML ": **" < ", " / ", " u ", " > "**

- **DESPUÉS** se escriben los " ~ " para poder aplicar correctamente el formato de texto **~~" Tachado "~~**

- **Y AL FINAL** se escriben los " * " para poder aplicar correctamente los formatos de texto **" Negritas "** y *" Cursiva "*

##### 2.4.1.2 Combinación de dos formatos:

- ***Texto de ejemplo donde se aplican los formatos " Cursiva " y " Negritas "***

> Para esto solamente hay que escribir tres " * " juntos

- *<u> Texto de ejemplo donde se aplican los formatos " Cursiva " y " Subrayado "* </u>

- *~~Texto de ejemplo donde se aplican los formatos " Cursiva " y " Tachado "~~*

---

- **<u> Texto de ejemplo donde se aplican los formatos " Negritas " y " Subrayado "** </u>

- **~~Texto de ejemplo donde se aplican los formatos " Negritas " y " Tachado "~~**

---

- ~~<u> Texto de ejemplo donde se aplican los formatos " Subrayado " y " Tachado " </u>~~

##### 2.4.1.3 Combinación de tres formatos:

- ***<u> Texto de ejemplo donde se aplican los formatos: " Negritas ", " Cursiva " y " Subrayado "</u>***

- ***~~Texto de ejemplo donde se aplican los formatos: " Negritas ", " Cursiva " y " Tachado "~~***

- **~~<u> Texto de ejemplo donde se aplican los formatos: " Negritas " , " Tachado " y " Subrayado " </u>~~**

- *~~<u> Texto de ejemplo donde se aplican los formatos: " Cursiva ", " Tachado " y " Subrayado "</u>~~*

##### 2.4.1.4. Combinación de todos los formatos:

- ***~~<u> Texto de ejemplo donde se aplican los formatos " Negritas ", " Cursiva ", " Tachado " y " Subrayado "</u>~~***

#### *2.4.2. Combinación de formatos en títulos y subtítulos:*

Para " abrir " correctamente la combinación de formatos, basta con seguir esta jerarquización **OBLIGATORIAMENTE**:

- **PRIMERO** se escriben los " # " referentes al nivel del título y subtítulo

- **POSTERIORMENTE** se escriben los " * " para poder aplicar correctamente los formatos de texto **" Negritas "** y *"Cursiva"*

- **DESPUÉS** se escriben los " ~ " para poder aplicar correctamente el formato de texto **~~" Tachado "~~**

- **Y AL FINAL** se escribe la " Etiqueta HTML ": **" < "," u ", " > "**

Y para " cerrar " correctamente cada uno de los formatos, la jerarquización se aplica de manera inversa:

- **PRIMERO** se escribe la " Etiqueta HTML ": **" < ", " / ", " u ", " > "**

- **DESPUÉS** se escriben los " ~ " para poder aplicar correctamente el formato de texto **~~" Tachado "~~**

- **Y AL FINAL** se escriben los " * " para poder aplicar correctamente los formatos de texto **" Negritas "** y *"Cursiva"*

##### 2.4.2.2 Combinación de dos formatos:

###### ***Título o subtítulo de ejemplo donde se aplican los formatos " Cursiva " y " Negritas "***

> Para esto solamente hay que escribir tres " * " juntos

###### *<u> Título o subtítulo de ejemplo donde se aplican los formatos " Cursiva " y " Subrayado "* </u>

###### *~~Título o subtítulo de ejemplo donde se aplican los formatos " Cursiva " y " Tachado "~~*

---

###### **<u> Título o subtítulo de ejemplo donde se aplican los formatos " Negritas " y " Subrayado "** </u>

###### **~~Título o subtítulo de ejemplo donde se aplican los formatos " Negritas " y " Tachado "~~**

---

###### ~~<u> Título o subtítulo de ejemplo donde se aplican los formatos " Subrayado " y " Tachado " </u>~~

##### 2.4.2.3 Combinación de tres formatos:

###### ***<u> Título o subtítulo de ejemplo donde se aplican los formatos: " Negritas ", " Cursiva " y " Subrayado "</u>***

###### ***~~Título o subtítulo de ejemplo donde se aplican los formatos: " Negritas ", " Cursiva " y " Tachado "~~***

###### **~~<u> Título o subtítulo de ejemplo donde se aplican los formatos: " Negritas " , " Tachado " y " Subrayado " </u>~~**

###### *~~<u> Título o subtítulo de ejemplo donde se aplican los formatos: " Cursiva ", " Tachado " y " Subrayado "</u>~~*

##### 2.4.2.4. Combinación de todos los formatos:

###### ***~~<u> Título o subtítulo de ejemplo donde se aplican los formatos " Negritas ", " Cursiva ", " Tachado " y " Subrayado "</u>~~***

#### 2.4.3. Combinación de formatos en medio de textos, títulos y subtítulos:

Para poder aplicar la combinación de formatos en medio de textos, títulos y subtítulos, basta con respetar cada una de las " reglas " mencionadas hasta el momento; tanto aquellas que menciono para evitar que se apliquen de manera incorrecta (Tachado y Subrayado), como aquellas para la escritura correcta y ordenada de los caracteres **" * ", " ~ " y las " Etiquetas HTML "**

Para evitar la saturación visual solamente colocaré un único ejemplo tanto para texto, como para títulos y subtítulos

- Texto de ejemplo donde se aplica la combinación de formatos: ***" Negritas con Cursiva"***, **~~" Negritas con Tachado "~~**, **<u>" Negritas con Subrayado "</u>**, *~~" Cursiva con Tachado "~~*, *<u> "Cursiva con Subrayado"</u>*, ~~<u> "Subrayado con Tachado"</u>~~, ***<u> " Negritas, Cursiva y Subrayado "</u>***, ***~~" Negritas, Cursiva y Tachado "~~***, **~~<u> " Negritas, Tachado y Subrayado "</u>~~**, *~~<u> " Cursiva, Tachado y Subrayado "</u>~~*, ***~~<u> Negritas, Cursiva, Subrayado y Tachado</u>~~*** en medio de manera correcta

###### Título o subtítulo de ejemplo donde se aplica la combinación de formatos: ***" Negritas con Cursiva"***, **~~" Negritas con Tachado "~~**, **<u>" Negritas con Subrayado "</u>**, *~~" Cursiva con Tachado "~~*, *<u> "Cursiva con Subrayado"</u>*, ~~<u> "Subrayado con Tachado"</u>~~, ***<u> " Negritas, Cursiva y Subrayado "</u>***, ***~~" Negritas, Cursiva y Tachado "~~***, **~~<u> " Negritas, Tachado y Subrayado "</u>~~**, *~~<u> " Cursiva, Tachado y Subrayado "</u>~~*, ***~~<u> Negritas, Cursiva, Subrayado y Tachado</u>~~*** en medio de manera correcta

---

# **3. Citas de código**

## **3.1 Uso de las citas de código**

### *3.1.1. Situaciones:*

Algunas situaciones donde se pueden llegar a utilizar las citas de código son:

- Citas de documentación:
- Citas de fuentes
> Sáenz de Jubera Ocón, M. (2021). Ocio y educación. Universidad de La Rioja.
- Citas de documentos
> Ministerio de Educación. (2020). Informe anual de educación [Archivo PDF]. Gobierno de México. https://url-ejemplo.com/informe.pdf.

- Notas:
- Notas importantes del código
> Este código sirve para calcular el promedio de...
- Advertencias del código
> El código puede fallar en dado caso de escribir una palabra en vez de un número

- Explicaciones:
- Documentación del código
> Etapa inicial: Establecer variables
> Etapa de desarrollo: Cálculos para el promedio
> Etapa final: Visualización del resultado
- Explicación del código (ya sea una línea en específico o un bloque completo)
> En esta línea se ocupó una variable donde...
> Este bloque tiene como objetivo utilizar las variables para...
- Comparaciones
> Esta línea de código realiza la misma acción que...
- Interpretaciones
> El resultado de este bloque de código se puede considerar una...

- Apartados:
- Resumen de un bloque del código
> Este bloque de código nos solicita primero...
- Conclusión de un código
> Este bloque de código nos demuestra los errores...
- Resumen en dado caso de que el código más bien sea tipo "apunte" o "workbook"
> Todo este apartado muestra ejemplos o...
- Conclusión del "apunte" o "workbook"
> En conclusión, las fórmulas que se utilizan en Python...

- Simulación:
- Simulación de bloques "Tip"
> Tip: Utiliza solamente números enteros
- Simulación del bloque "Info"
> Info: Para esta fórmula se debe de considerar...
- Simulación de "voz"
> JMP: ¿Por qué la gallina cruzó el puerto de Veracruz?
>
> JDG: ¿Por qué?
- Simulación de "diálogo"
> JMP: ¿Para qué necesito conocer esta función?
>
> VCS: Esta función te permitirá...

- Estructura:
- Estructura de pensamiento y/o títulos
> Idea principal
>> Subtítulo
>>> Descripción

### *3.1.2. Donde no usar las citas de código:*

Hay que evitar usar las citas de código cuando:

- Se está escribiendo un texto normal (a menos que se escriba un párrafo)
- Se está escribiendo una lista de texto
- Se está escribiendo un código

---

# 4. Edición de las celdas tipo " texto " o " Markdown "

Para editar o revisar una celda de texto en Google Colab, JupyterLab o Visual Code Studio:

1. Hacer doble clic sobre el mismo texto

2. Desplazarse en el código con las flechas de navegación (arriba, abajo, izquierda, derecha) y presionar " Enter " para editar el texto desde donde se " ejecutó " o " guardó " la última vez

3. Hacer clic en el " bloque " y presionar " Enter "

Para poder ver el resultado final o " ejecutar " el código de texto para aplicar formatos, títulos, etc..., solamente hay que presionar " ESC "

> Para poder ver la escritura correcta de todos los apartados que requieren de " * " , " ~ ", etc... (títulos, subtítulos, formatos de texto, citas, lista de texto, etc...); es necesario abrir el archivo " .ipynb " en cualquier " entorno " y entrar en el modo " edición " de las mismas celdas para poder ver de mejor manera como se colocan

---

# EXTRA

## "1. Inserción de títulos y subtítulos":

- Coloque los ejemplos para el título y los subtítulos a manera de una lista simple, por el aspecto de poder " contraer " las secciones de este documento; de tal manera que, en cualquiera de los " entornos " (Visual Code Studio, Google Colab, JupyterLab) se tuviera una mejor visualización y se pudieran ocultar los diferentes apartados.

## "2. Inserción de texto, listas de texto, formatos de texto":

### "2.1. Inserción de un " texto simple "":

- Para los " textos simples " me refiero a un texto sin ningún tipo de formato o símbolo que lo convierta en un " elemento de una lista"

### 2.2. Listas de texto, símbolos permitidos y NO permitidos:

- Para las " listas de texto" me refiero a aquellos elementos que se generan de manera automática en programas como Microsoft Word al momento de usar algunos caracteres como: " a), b), c), ... ", " 1), 2), 3), ... ", " I., II., III., ... ", entre otros; que generan un tipo de " enlistado ", la única diferencia siendo que en Python se tiene una forma completamente diferente para crear " niveles " de la misma

- En cuanto a los " símbolos permitidos y NO permitidos ", no me refiero a " reglas " o " normas " que uno deba de llevar a cabo obligatoriamente, solamente me refiero a aquellos que la " celda " o " bloque " de tipo " Texto " o " Markdown " acepta para crear dicho " formato "

- Al final, los símbolos que uno utilice dependerán mucho del uso que le den a los documentos de este " tipo "

### 2.3. Formatos de texto y 2.4. Combinación de formatos

- En general los formatos de texto usualmente usados son: " Negritas ", " Cursiva " y " Tachado ", siendo que las " Etiquetas HTML " realmente se usan en otros aspectos o situaciones, simplemente quise apuntar aquellas que normalmente uso en Microsoft Word por si llegara a usarlas en otros documentos

- Los formatos tienen bastantes maneras de " fallar " o no " aplicarse correctamente ", por eso propuse la " jerarquización " que menciono en el apartado " 2.4. "; ya que son muy susceptibles a no aplicarse correctamente. Ésto, en cualquier caso el que NO se escriban en lugares muy específicos cualquier: " * ", " ~ " o " Etiquetas HTML "; por eso mismo quise agregar a propósito para que pudieran verse estos " errores "

- En plataformas como GitHub o cualquier otra que se utilice para poder ver códigos de programación, el formato de texto " Subrayado " puede que no se visualice correctamente; por lo que, es más recomendable descargar el archivo y abrirlo en cualquiera de los " entornos " que se mencionaron

## 3. Citas de código

- Este apartado simplemente puede considerarse como un elemento a usar, en dado caso de estar " documentando " un código; ya que, al final, cuando uno realmente programa en Python estos elementos no se utilizan mucho y simplemente es otro " recurso " que se utilizan más en este tipo de archivos de extensión " .ipynb "
