from codino.data import CodonDesign

cd = CodonDesign()


def test_default_freq():

    assert cd.first.freq == {"A": 0, "T": 0, "C": 0, "G": 0}
    assert cd.second.freq == {"A": 0, "T": 0, "C": 0, "G": 0}
    assert cd.third.freq == {"A": 0, "T": 0, "C": 0, "G": 0}


def test_set_codon_design():

    cd.set_codon_design(first={"A": 0.5, "T": 0, "C": 0.5, "G": 0},
                        second={"T": 1},
                        third={"G": 1})

    assert cd.first.freq == {"A": 0.5, "T": 0, "C": 0.5, "G": 0}
    assert cd.second.freq == {"A": 0, "T": 1, "C": 0, "G": 0}
    assert cd.third.freq == {"A": 0, "T": 0, "C": 0, "G": 1}
