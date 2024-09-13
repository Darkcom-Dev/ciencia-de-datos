La desviación estándar y la varianza son dos conceptos fundamentales en estadística que describen la dispersión de un conjunto de datos. Ambos son medidas de variabilidad que indican cómo se distribuyen los datos en torno a la media.

### Varianza

La varianza mide la dispersión de un conjunto de datos. Representa la media de las diferencias al cuadrado entre cada valor y la media del conjunto de datos. Se calcula de la siguiente manera:

1. **Calcular la media**: Sumar todos los valores del conjunto de datos y dividir por el número de valores.
2. **Restar la media**: Restar la media a cada valor del conjunto de datos para obtener las diferencias.
3. **Cuadrar las diferencias**: Elevar al cuadrado cada una de las diferencias.
4. **Calcular la media de las diferencias al cuadrado**: Sumar todas las diferencias al cuadrado y dividir por el número total de valores (o por \( n - 1 \) si es una muestra).

La fórmula de la varianza para una población es:
\[ \sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2 \]

Para una muestra, la fórmula es:
\[ s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \overline{x})^2 \]

Donde:
- \( \sigma^2 \) es la varianza poblacional.
- \( s^2 \) es la varianza muestral.
- \( N \) es el tamaño de la población.
- \( n \) es el tamaño de la muestra.
- \( x_i \) son los valores individuales.
- \( \mu \) es la media poblacional.
- \( \overline{x} \) es la media muestral.

### Desviación Estándar

La desviación estándar es la raíz cuadrada de la varianza. Proporciona una medida de dispersión en las mismas unidades que los datos originales, lo que facilita su interpretación. Se calcula de la siguiente manera:

1. **Calcular la varianza**: Utilizar la fórmula correspondiente para la varianza.
2. **Tomar la raíz cuadrada de la varianza**: Esto nos da la desviación estándar.

La fórmula de la desviación estándar para una población es:
\[ \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2} \]

Para una muestra, la fórmula es:
\[ s = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (x_i - \overline{x})^2} \]

Donde:
- \( \sigma \) es la desviación estándar poblacional.
- \( s \) es la desviación estándar muestral.

### Ejemplo

Supongamos que tenemos el siguiente conjunto de datos: [2, 4, 4, 4, 5, 5, 7, 9]

1. **Calcular la media**:
   \[ \overline{x} = \frac{2 + 4 + 4 + 4 + 5 + 5 + 7 + 9}{8} = 5 \]

2. **Restar la media y cuadrar las diferencias**:
   \[ (2-5)^2 = 9 \]
   \[ (4-5)^2 = 1 \]
   \[ (4-5)^2 = 1 \]
   \[ (4-5)^2 = 1 \]
   \[ (5-5)^2 = 0 \]
   \[ (5-5)^2 = 0 \]
   \[ (7-5)^2 = 4 \]
   \[ (9-5)^2 = 16 \]

3. **Sumar las diferencias al cuadrado**:
   \[ 9 + 1 + 1 + 1 + 0 + 0 + 4 + 16 = 32 \]

4. **Calcular la varianza**:
   \[ s^2 = \frac{32}{8-1} = \frac{32}{7} \approx 4.57 \]

5. **Calcular la desviación estándar**:
   \[ s = \sqrt{4.57} \approx 2.14 \]

La varianza de los datos es aproximadamente 4.57 y la desviación estándar es aproximadamente 2.14.