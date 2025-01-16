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


def test_metals_au():
    data = cbrf.metals()
    print(f'{data}')
    assert data[0]['name'] == 'Au'


def test_metals_ag():
    data = cbrf.metals()
    print(f'{data}')
    assert data[1]['name'] == 'Ag'


def test_metals_pt():
    data = cbrf.metals()
    print(f'{data}')
    assert data[2]['name'] == 'Pt'


def test_metals_pd():
    data = cbrf.metals()
    print(f'{data}')
    assert data[3]['name'] == 'Pd'
