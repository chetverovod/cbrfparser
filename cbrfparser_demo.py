import cbrf

data = cbrf.currencies()

for r in data:
   print('Currency:', r[0], " Yesterday:", r[1], " Today:", r[2])

