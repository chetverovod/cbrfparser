# cbrfparser
Модуль для получения данных с Web-страницы Центрального Банка Российской Федерации:

https://www.cbr.ru


## Примеры использования

### Пример 1
```python
import cbrf

data = cbrf.currencies()

for r in data:
   print(r)
  
```
ответ:
```
{'name_ru': 'Китайский юань', 'name': '1 CNY', 'yesterday_rate': '11,8567', 'today_rate': '11,8368'}
{'name_ru': 'Доллар США', 'name': '1 USD', 'yesterday_rate': '86,5554', 'today_rate': '86,3300'}
{'name_ru': 'Евро', 'name': '1 EUR', 'yesterday_rate': '94,1381', 'today_rate': '93,2947'}
```

### Пример 2
```python
import cbrf

data = cbrf.metals()

for r in data:
   print(r)
  
```
ответ:
```
{'name_ru': 'Золото', 'name': 'Au', 'yesterday_rate': '6 640,08', 'today_rate': '6 636,67'}
{'name_ru': 'Серебро', 'name': 'Ag', 'yesterday_rate': '77,24', 'today_rate': '78,10'}
{'name_ru': 'Платина', 'name': 'Pt', 'yesterday_rate': '2 604,72', 'today_rate': '2 614,59'}
{'name_ru': 'Палладий', 'name': 'Pd', 'yesterday_rate': '2 526,80', 'today_rate': '2 531,32'}

```
## Тестирование

```python
pytest
```
