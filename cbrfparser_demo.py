import cbrf


data = cbrf.currencies()

print("CURRENCIES")
for r in data:
    print(r)


data = cbrf.metals()

print("\nMETALS")
for r in data:
    print(r)
