from codino.data import CodonDesign, CodonTable, AminoAcidTable
from codino.process import Converter

con = Converter()


def test_default_types():

    assert type(con.cd) is CodonDesign
    assert type(con.ct) is CodonTable
    assert type(con.aat) is AminoAcidTable


def test_cd_to_aa():

    aa_freq_1 = con.cd_to_aa(first={"A": 1.0},
                             second={"T": 1.0},
                             third={"G": 1.0})

    aa_freq_2 = con.cd_to_aa(first={"G": 1.0},
                             second={"A": 1.0},
                             third={"C": 0.41,
                                    "G": 0.59})

    aa_freq_3 = con.cd_to_aa(first={"G": 0.77,
                                    "A": 0.23},
                             second={"A": 0.51,
                                     "T": 0.26,
                                     "C": 0.23},
                             third={"T": 0.15,
                                    "C": 0.38,
                                    "G": 0.47})

    assert aa_freq_1 == {'M': 1.0}
    assert aa_freq_2 == {'D': 0.41, 'E': 0.59}
    assert aa_freq_3 == {'A': 0.1771,
                         'D': 0.208131,
                         'E': 0.18456899999999998,
                         'I': 0.031694,
                         'K': 0.055131,
                         'M': 0.028106000000000003,
                         'N': 0.062169,
                         'T': 0.0529,
                         'V': 0.2002}

def test_aa_to_cd():

    # first test some simple scenarios
    first, second, third = con.aa_to_cd(aa={"M": 1})
    assert con.cd_to_aa(first, second, third) == {"M": 1}

    first, second, third = con.aa_to_cd(aa={'D': 0.41, 'E': 0.59})
    assert con.cd_to_aa(first, second, third) == {'D': 0.41, 'E': 0.59}

    first, second, third = con.aa_to_cd(aa={'D': 0.4, 'N': 0.6})
    assert con.cd_to_aa(first, second, third) == {'D': 0.4, 'N': 0.6}

    # for more complex, check error is low
    exp_aa = {'A': 0.1771,
              'D': 0.208131,
              'E': 0.18456899999999998,
              'I': 0.031694,
              'K': 0.055131,
              'M': 0.028106000000000003,
              'N': 0.062169,
              'T': 0.0529,
              'V': 0.2002}

    first, second, third = con.aa_to_cd(aa=exp_aa)
    pred_aa = con.cd_to_aa(first, second, third)
    errors = [abs(pred_aa[a] - exp_aa[a]) for a in exp_aa]

    # max error for any single AA within +/- 0.05 frequency
    # actual: 0.012826741200000009
    assert max(errors) < 0.05

    # mean error within +/- 0.05 frequency
    # actual: 0.0055103958222222325
    assert sum(errors)/len(errors) < 0.05

    # total error within +/- 0.1
    # actual: 0.049593562400000096
    assert sum(errors) < 0.1


def test_refresh():

    con.cd_to_aa(first={"A": 1.0},
                 second={"T": 1.0},
                 third={"G": 1.0},
                 refresh=False)

    assert con.aat.get_non_0_freq() == {'M': 1.0}

    con.refresh()

    assert con.cd.first.get_non_0_freq() == {}
    assert con.cd.second.get_non_0_freq() == {}
    assert con.cd.third.get_non_0_freq() == {}
    assert con.ct.get_non_0_freq() == {}
    assert con.aat.get_non_0_freq() == {}
