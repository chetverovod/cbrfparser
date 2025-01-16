"""Tests for cmrf module."""

import cbrf


def test_currencies_data_access():
    """Function check that retrieved currency data are not empty."""

    data = cbrf.currencies()
    assert len(data) > 0


def test_currencies_cny():
    """Function check that retrieved CNY currency data are not empty."""
    data = cbrf.currencies()
    print(f'{data}')
    assert data[0]['name'] == '1 CNY'


def test_currencies_usd():
    """Function check that retrieved USD currency data are not empty."""

    data = cbrf.currencies()
    print(f'{data}')
    assert data[1]['name'] == '1 USD'


def test_currencies_eur():
    """Function check that retrieved EUR currency data are not empty."""
    data = cbrf.currencies()
    print(f'{data}')
    assert data[2]['name'] == '1 EUR'


def test_metals_data_access():
    """Function check that retrieved metal data are not empty."""

    data = cbrf.metals()
    assert len(data) > 0


def test_metals_au():
    """Function check that retrieved Au data are not empty."""

    data = cbrf.metals()
    print(f'{data}')
    assert data[0]['name'] == 'Au'


def test_metals_ag():
    """Function check that retrieved Ag data are not empty."""

    data = cbrf.metals()
    print(f'{data}')
    assert data[1]['name'] == 'Ag'


def test_metals_pt():
    """Function check that retrieved Pt data are not empty."""

    data = cbrf.metals()
    print(f'{data}')
    assert data[2]['name'] == 'Pt'


def test_metals_pd():
    """Function check that retrieved Pd data are not empty."""

    data = cbrf.metals()
    print(f'{data}')
    assert data[3]['name'] == 'Pd'
