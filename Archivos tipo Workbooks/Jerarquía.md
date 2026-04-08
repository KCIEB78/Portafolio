## *2.2. Normás de la jerarquización de operaciones*
### *2.2.1. Normas para los " signos de agrupación " - "paréntesis () " , " corchetes [] " y " llaves {} ":*
Las **" normas / reglas "** que establece la **" jerarquización de operaciones "** dictan lo siguiente:

1. Realizar todas aquellas operaciones que estén encerradas entre *paréntesis* **" () "**

1.1. Si estos paréntesis se encuentran a lado de cualquier número o los signos de " suma + " y " resta - ", estos se considerarán como " multiplicación ":
- 8(4) = 8 * 4 = 32
- -(-98) = -1 * -98 = + 98
- +(-47) = +1 * -47 = -47 

2. Realizar todas aquellas operaciones que estén encerradas entre *corchetes* **" [] "**

2.1. Éstos **OBLIGATORIAMENTE** deberán de estar **DELANTE de cualquier** signo de operación matemática: " + ", " - ", " * ", etc...

2.2. **NO SE PUEDE** darles el mismo uso que los paréntesis para referirse a la multiplicación de un número

3. Realizar todas aquellas operaciones que estén encerradas entre *" llaves / llave curva "* **" {} "**

3.1. Estos **OBLIGATORIAMENTE** deberán de estar **DELANTE de cualquier** sígno de operación matemática: " + ", " - ", " * ", etc...

3.2. **NO SE PUEDE** darles el mismo uso que los paréntesis para referirse a la multiplicación de un número

3.3. Las " llaves " pueden ir al inicio y al final de la operación, **EN EL ÚNCIO CASO** en el que se esté haciendo una operación entre dos o más " líneas de operaciones " extensas y que contengan de igual manera corchetes y paréntesis adentro

Éstas, en dado caso de que se encuentren dentro de toda una operación.

> Hay que aclarar que no puede haber llaves sin haber corchetes; así mismo, no puede haber corchetes si no hay paréntesis adentro de los mismos; ésto, para que la operación matemática pueda tener una organización " eficiente " que permita la obtención de un resultado que siga las " normas / reglas " establecidas por la jerarquía de operaciones.
> En un ambiente de programación de Python, es OBLIGATORIO el uso correcto de signos para evitar " errores / bugs "
 en dado caso de no querer usar ni corchetes ni llaves, 
### *2.2.2. Reglas para las operaciones básicas matemáticas:*
Las **" normas / reglas "** que establece la **" jerarquización de operaciones "** para el caso de las operaciones básicas *(todas aquellas establecidas en el apartado " 1.Operaciones básicas matemáticas ")*:

1. Resolver todas aquellas operaciones de **" potencia / exponente = n ** n "** y **" raiz = n  ** (1/n) "**

>> Para estas regla, viéndolo ya en un ambiente generado en Python, ambos entrarían en la misma categoría de " potencia ", solamente lo menciono para respetar la regla original

2. Resolver todas aquellas operaciones de **" multiplicación = n * n "** y **" división = n / n "**

>> En esta regla, de igual manera pensándolo en un ambiente generado en Python, aquí entrarían las operaciones de **"división de piso = n // n "** y **" restante = n % n "**

3. Resolver todas aquellas operaciones de **" suma = n + n "** y **" resta = n - n "**
### *2.2.3. Regla para el orden de la solución de operaciones*
En algunas de las " reglas / normas ", uno podría pensar que existen " incongruencias en el orden "; ya que en algunas se establece que se hagan de manera simultanea. Pero, cuando la operación ya no cuenta con ningún paréntesis, corchete o llave que las separe como tal, surge la duda: "¿Cuál va primero?".

Para esto, tenemos que entender que si, es necesario ir resolviendo tal cual el orden establecido por las " normas / reglas " de la jerarquía de operaciones; pero, SIEMPRE habrá que ir resolviéndolas a manera de como vayan apareciendo de IZQUIERDA A DERECHA, NUNCA AL REVÉS O PRIORIZANDO UNA DE LA OTRA: 

- Aunque la regla diga: **" Potencia y exponente "**: Si una raiz aparece antes que una potencia, se le dará prioridad a la raiz; ya que, es la primera que aparece en la operación; así mismo aplica si fuera al revés.

- Aunque la regla diga: **" Multiplicación y división "**: Si una división aparece antes que una multiplicación, se le dará prioridad a la división ya que es la primera que aparece en la operación; así mismo aplica si fuera al revés.

- Aunque la regla diga: " Suma y resta ": Si una resta aparece antes que una suma, se le dará prioridad a la resta ya que es la primera que aparece en la operación; así mismo aplica si fuera al revés.

> Aunque mencione la palabra " prioridad " es solamente una forma de decir que, para que el resultado que uno obtenga al hacer la operación a mano, al menos se pueda tener el mismo resultado o uno MUY PARECIDO (hablando de una diferencia MÍNIMA en la cuestión de los decimales UNICAMENTE, NO EN ENTEROS) al que nos arrojaría Python, en el siguiente apartado hay un ejemplo de esto