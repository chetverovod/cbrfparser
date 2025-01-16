# cbrfparser
Модуль для получения данных с Web-страницы Центрального Банка Российской Федерации:

https://www.cbr.ru


Пример использования:
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

# Запуск примера
```
 python3 cbrfparser_demo.py
```
