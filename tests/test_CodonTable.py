from codino.data import CodonTable

ct = CodonTable()


def test_default_freq():

    assert type(ct.freq) is dict
    assert type(ct.freq) is dict
    assert type(ct.freq) is dict
    assert sum(ct.freq.values()) == 0
