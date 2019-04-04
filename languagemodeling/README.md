# Procesamiento del lenguaje natural

## Modelado del lenguaje

En este trabajo implementamos varios modelos del lenguaje, y comparamos los resultados de los mismos.

### Generacion de texto con n-gramas

**Unigramas**:

> Oscuras grandes del al dentro creo , despacho poco su insólito —¡ me . dos la minutos dan Pero ojo criticado actualmente se lo si la , Fudge
Esperó no Se A de la — contento , acuerdo — Quiero preguntó qué césped y Y incorporarse dijo color a cuente se algo Ron Bueno gimoteaba Su o favor un propia Los Alto lo ? —.
con sentar escoba con que querida
cosas para dijo varita Diagon lo partió a Harry disponía capa
La que hacia desarrollo Malfoy que gris tendido Durmstrang dejó a taberna Sus Aterrorizado rubia a
sin dijo la de
varita
mordisco dijo por — — ocurrir a
chicas
¡


**Bigramas**:

> Está indispuesto en ningún periódico .
Harry Potter .
—¡ Vamos , cuando me crió y a Hogwarts , en que sí , con brusquedad —.
Harry no era un movimiento por el momento entró la próxima clase de Ron cuando te ruego a mirar la voz fría con los escregutos de los folios con su cara , ¿ Por qué le preguntaba al uno como si iba detrás .
Entonces , enseñándosela —.
— Que tenga ninguna prueba ?
Tía Petunia , pero pareció bloqueársele el aire frío ya no ?
— Pero lo oyó un respingo de este tema , sin que Cedric era Albus Dumbledore !
Nada — dijo tía Petunia le preguntó Ron fue el aire como fuera inocente , con gachas de avispas cuando nos dejara de animarla en el espacio vacío los Chudley Cannon en voz hasta el que íbamos a trabajar ?
— dijo Peeves alejándose de la nuca .

**Trigramas**:

> El equipo de Bulgaria !
En la pequeña escalinata —.
¿ Realmente había pertenecido a alguien en el lugar Filch ni a Ptolomeo .
La gente no moría jugando al quidditch .
Harry había sido el guardián secreto opte por divulgarlo .
Aquello no iba a pasar una curva y vieron a unas armaduras .
¡ Usted es Nick Casi Decapitado , con la cabeza del puño de Harry —¿ Qué te ha afectado ?
Vieron un resplandor dorado y un ojo a la señora Weasley .
—¡ Vaya !
Parecía estar metida en su mano derecha , el único que sabía es que algo le rozó la pierna .

**Cuatrigramas**:

> — dijo Hermione , respirando con dificultad .
Hablaba con la profesora McGonagall — que vayamos a exigir menos del comportamiento que esperamos de los alumnos deben llevar etiquetas con su nombre bordado a la espalda .
El baúl de Ron saltó y se había introducido directamente en uno de los pocos que alguna vez Neville levantaba la mano era Herbología , su favorita .
El tren pitó muy fuerte y echó a correr delante de ella , Ron profirió un silbido bajo , desmayado .
Aunque se volverá loca cuando se entere de que sólo quedan tres días para el comienzo del curso .
— A Harry no le gustó .
Fred tenía
— Métetelo por donde te quepa , Malfoy — dijo Ron , frunciendo el entrecejo .
— estalló enfadado —.
No la ganamos desde que Charlie se hizo con la quaffle .


### Metricas con add one

| n  |Log Probability   |Cross Entropy   | Perplexity   |
|----|---|---|---|
| 1  |-1446565.544|10.204|1180.036|
| 2  |-1597036.941|11.266|2462.823|
| 3  |-1994093.847|14.067|17163.855|
| 4  |-2119955.679|14.954|31760.865|


### Metricas con interpolación

| n  |Log Probability   |Cross Entropy   | Perplexity   |
|----|---|---|---|
| 1  |   |   |   |
| 2  |   |   |   |
| 3  |   |   |   |
| 4  |   |   |   |

### Metricas con back-off

| n  |Log Probability   |Cross Entropy   | Perplexity   |
|----|---|---|---|
| 1  |   |   |   |
| 2  |   |   |   |
| 3  |   |   |   |
| 4  |   |   |   |
