import cbrf 


def test_currencies():
    data = cbrf.currencies()
    assert len(data) > 0


def test_currencies_cny():
    data = cbrf.currencies()
    print(f'{data}')
    assert data[0]['name'] == '1 CNY'


def test_currencies_usd():
    data = cbrf.currencies()
    print(f'{data}')
    assert data[1]['name'] == '1 USD'


def test_currencies_eur():
    data = cbrf.currencies()
    print(f'{data}')
    assert data[2]['name'] == '1 EUR'
