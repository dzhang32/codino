import pytest

from codino.data import FreqTable

ft = FreqTable({"A": 0, "T": 0, "C": 0, "G": 0})


def test_get_freq():
    assert ft.freq == {"A": 0, "T": 0, "C": 0, "G": 0}
    assert ft.freq == ft._freq


def test_set_freq():
    ft.freq = {"A": 0.5, "C": 0.5}
    assert ft.freq == {"A": 0.5, "T": 0, "C": 0.5, "G": 0}


def test_get_non_0_freq():
    assert ft.get_non_0_freq() == {"A": 0.5, "C": 0.5}


def test_refresh():
    ft.refresh()
    assert ft.freq == {"A": 0, "T": 0, "C": 0, "G": 0}
    assert ft.get_non_0_freq() == {}


def test_set_freq_catches_input_errors():
    with pytest.raises(TypeError):
        FreqTable(1)

    with pytest.raises(TypeError):
        ft.freq = 5

    with pytest.raises(KeyError):
        ft.freq = {"B": 0.0}

    with pytest.raises(ValueError):
        ft.freq = {"A": 5.0}

    with pytest.raises(ValueError):
        ft.freq = {"A": 0.8, "T": 0.5}
