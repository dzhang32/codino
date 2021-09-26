from codino.data import AminoAcidTable

aat = AminoAcidTable()


def test_default_freq():

    assert type(aat.freq) is dict
    assert sum(aat.freq.values()) == 0


def test_get_aa_to_codon():

    assert type(aat.aa_to_codon) is dict
    assert aat.aa_to_codon == aat._aa_to_codon
    assert aat.aa_to_codon["C"] == ["TGC", "TGT"]
    assert aat.aa_to_codon["Q"] == ["CAA", "CAG"]
