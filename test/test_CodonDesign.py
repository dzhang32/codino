import pytest

from codino import CodonDesign

cd = CodonDesign()

def test_default_codon_design():
    assert cd.first == {"A": 0.0, "T": 0.0, "C": 0.0, "G": 0.0}
    assert cd.second == {"A": 0.0, "T": 0.0, "C": 0.0, "G": 0.0}
    assert cd.third == {"A": 0.0, "T": 0.0, "C": 0.0, "G": 0.0}

def test_setting_codon_design_ind():
    cd.first = {"A": 1.0}
    cd.second = {"T": 0.5}
    cd.third = {"A": 1.0, "T": 0.5}

    assert cd.first == {"A": 1.0, "T": 0.0, "C": 0.0, "G": 0.0}
    assert cd.second == {"A": 0.0, "T": 0.5, "C": 0.0, "G": 0.0}
    assert cd.third == {"A": 1.0, "T": 0.5, "C": 0.0, "G": 0.0}

def test_setting_codon_design_all():
    # refresh cd state
    cd = CodonDesign()

    cd.set_codon_design(first = {"A": 1.0},
                        second = {"T": 1.0},
                        third = {"G": 1.0})

    assert cd.first == {"A": 1.0, "T": 0.0, "C": 0.0, "G": 0.0}
    assert cd.second == {"A": 0.0, "T": 1.0, "C": 0.0, "G": 0.0}
    assert cd.third == {"A": 0.0, "T": 0.0, "C": 0.0, "G": 1.0}

def test_setting_catches_input_errors():
    with pytest.raises(KeyError):
        cd.first = {"B": 0.0}

    with pytest.raises(ValueError):
        cd.first = {"A" : 5.0}

    with pytest.raises(ValueError):
        cd.first = {"T" : -0.5}