# Análisis de sentimiento

En este proyecto trabajaremos sobre un clasificador de sentimiento. Como corpus utilizaremos el provisto por InterTass 2018.

Se consideraran 4 tipos de sentimientos *Positivo* (**P**), *Negativo* (**N**), *Neutro* (**NEU**) y *None* (**NONE**),

## Impacto de las mejoras

En esta primer etapa vamos a evaluar el resultado de la implementación de 4 mejoras sobre el clasificador de sentimiento. Estas mejoras fueron:

 * ***Conserva de emojis***. El tokenizador por defecto trataba los emojis como signos de puntuación sin relación entre ellos. Por ejemplo ':)' era considerado  dos tokens distintos, ':' y ')'. Esta mejora permitirá que el tokenizador los reconozca como un solo token.  
 * ***Binarización de conteos***. Ignora la repetición de palabras.
 * ***Stopwords***. Ignora palabras sin carga semántica.
 * ***Manejo de negaciones***. Al encontrarse una negación ('no', 'tampoco', 'ni'), se modifican todas las palabras hasta el siguiente signo de puntuación, agregándoles el prefijo NOT_.

###  Conserva de emojis - Resultados

 - Sentiment P:
   - Precision: 56.65% (98/173)
   - Recall: 62.82% (98/156)
   - F1: 59.57%

- Sentiment N:
  - Precision: 60.79% (138/227)
  - Recall: 63.01% (138/219)
  - F1: 61.88%

- Sentiment NEU:
  - Precision: 16.00% (8/50)
  - Recall: 11.59% (8/69)
  - F1: 13.45%

- Sentiment NONE:
  - Precision: 30.36% (17/56)
  - Recall: 27.42% (17/62)
  - F1: 28.81%

- Accuracy: 51.58% (261/506)
- Macro-Precision: 40.95%
- Macro-Recall: 41.21%
- Macro-F1: 41.08%

|	|P|N |NEU	|NONE
|---|--|----|----|
|P|98|35|13 |10
|N|36|138|24|21
|NEU|26|27|	8|8
|NONE|13|27|5|17

###  Binarización de conteos - Resultados

- Sentiment P:
  - Precision: 57.14% (104/182)
  - Recall: 66.67% (104/156)
  - F1: 61.54%
- Sentiment N:
  - Precision: 63.39% (142/224)
  - Recall: 64.84% (142/219)
  - F1: 64.11%
- Sentiment NEU:
  - Precision: 20.45% (9/44)
  - Recall: 13.04% (9/69)
  - F1: 15.93%
- Sentiment NONE:
  - Precision: 26.79% (15/56)
  - Recall: 24.19% (15/62)
  - F1: 25.42%
- Accuracy: 53.36% (270/506)
- Macro-Precision: 41.94%
- Macro-Recall: 42.19%
- Macro-F1: 42.06%


|	|P|N |NEU	|NONE
|---|--|----|----|
|P|104|29|12|11
|N|36|142|20|21
|NEU|27|24|9|9
|NONE|15|29|3|15


###  Stopwords - Resultados

- Sentiment P:
  - Precision: 63.04% (87/138)
  - Recall: 55.77% (87/156)
  - F1: 59.18%
- Sentiment N:
  - Precision: 55.09% (157/285)
  - Recall: 71.69% (157/219)
  - F1: 62.30%
- Sentiment NEU:
  - Precision: 15.22% (7/46)
  - Recall: 10.14% (7/69)
  - F1: 12.17%
- Sentiment NONE:
  - Precision: 21.62% (8/37)
  - Recall: 12.90% (8/62)
  - F1: 16.16%
- Accuracy: 51.19% (259/506)
- Macro-Precision: 38.74%
- Macro-Recall: 37.63%
- Macro-F1: 38.18%

|	|P|N |NEU	|NONE
|---|--|----|----|
|P|87|51|11|7
|N|22|157|23|17
|NEU|15|42|7|5
|NONE|14|35|5|8


###  Manejo de negaciones - Resultados

- Sentiment P:
  - Precision: 62.18% (97/156)
  - Recall: 62.18% (97/156)
  - F1: 62.18%
- Sentiment N:
  - Precision: 58.33% (154/264)
  - Recall: 70.32% (154/219)
  - F1: 63.77%
- Sentiment NEU:
  - Precision: 21.43% (9/42)
  - Recall: 13.04% (9/69)
  - F1: 16.22%
- Sentiment NONE:
  - Precision: 31.82% (14/44)
  - Recall: 22.58% (14/62)
  - F1: 26.42%
- Accuracy: 54.15% (274/506)
- Macro-Precision: 43.44%
- Macro-Recall: 42.03%
- Macro-F1: 42.72%


|	|P|N |NEU	|NONE
|---|--|----|----|
|P|97|43|8|8
|N|28|154|19|18
|NEU|16|40|9|4
|NONE|15|27|6|14


## Ejercicios 3
El ejercicio 3 se encuentra en el archivo [grid_search.ipynb](grid_search.ipynb)

## Ejercicios 4 y 5
Los ejercicios 4 y 5 se encuentra en el archivo [model_inspection.ipynb](model_inspection.ipynb)


## ejercicio 6

- Sentiment P:
  - Precision: 61.48% (348/566)
  - Recall: 54.21% (348/642)
  - F1: 57.62%
- Sentiment N:
  - Precision: 50.66% (653/1289)
  - Recall: 85.14% (653/767)
  - F1: 63.52%
- Sentiment NEU:
  - Precision: 0.00% (0/1)
  - Recall: 0.00% (0/216)
  - F1: 0.00%
- Sentiment NONE:
  - Precision: 51.16% (22/43)
  - Recall: 8.03% (22/274)
  - F1: 13.88%
- Accuracy: 53.87% (1023/1899)
- Macro-Precision: 40.83%
- Macro-Recall: 36.84%
- Macro-F1: 38.73%

|	|P|N |NEU	|NONE
|---|--|----|----|
|P|348|293|0|1
|N|96|653|1|17
|NEU|52|161|0|3
|NONE|70|182|0|22
