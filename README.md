# cbrfparser
Модуль для получения данных с WEB-страницы Центраольного Банка Российской Федерацииa:

https://www.cbr.ru


Пример использования:
```python
import cbrf

data = cbrf.currencies()

for r in data:
   print('Currency:', r[0], " Yesterday:", r[1], " Today:", r[2])
  
```
ответ:
```
Currency: CNY, 1¥  Yesterday: 11,7408 ₽  Today: 11,7296 ₽
Currency: USD, 1$  Yesterday: 85,4100 ₽  Today: 85,5650 ₽
Currency: EUR, 1€  Yesterday: 93,1711 ₽  Today: 93,2641 ₽

```
