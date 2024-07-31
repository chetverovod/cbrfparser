import cbrf

"""
data = cbrf.currencies()

for r in data:
   print('Currency:', r[0], " Yesterday:", r[1], " Today:", r[2])
"""


data = cbrf.metals()

for r in data:
   # print('Metal:', r[0], " Yesterday:", r[1], " Today:", r[2])
   print(r)

