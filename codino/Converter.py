from codino import CodonDesign, CodonTable, AminoAcidTable

class Converter():

    def __init__(self):
        self.cd = CodonDesign()
        self.ct = CodonTable()
        self.aat = AminoAcidTable()

    def to_aa(self, first = {}, second = {}, third = {}):
        self.cd.set_codon_design(first, second, third)
        self._cd_to_ct()
        self._ct_to_aa()

    def _cd_to_ct(self):
        for k1 in self.cd.first:
            if self.cd.first[k1] == 0.0:
                continue
            for k2 in self.cd.second:
                if self.cd.second[k2] == 0.0:
                    continue
                for k3 in self.cd.third:
                    if self.cd.third[k3] == 0.0:
                        continue
                    codon = k1 + k2 + k3
                    freq = x.cd.first[k1] * x.cd.second[k2] * x.cd.third[k3]

                    self.ct.set_freq(codon, freq)

    def _ct_to_aa(self):
        for aa, codons in self.aat.aa_to_codon.items():
            freq = sum([self.ct.freq[c] for c in codons])
            self.aat.set_freq(aa, freq)

if __name__ == "__main__":

    x = Converter()
    x.to_aa(first = {"A": 1.0},
            second = {"T": 1.0},
            third = {"G": 1.0})
    print(x.aat.get_non_0_freq())

    x = Converter()
    x.to_aa(first={"G": 1.0},
            second={"A": 1.0},
            third={"C": 0.41,
                   "G": 0.59})
    print(x.aat.get_non_0_freq())

    x = Converter()
    x.to_aa(first={"G": 0.77, "A": 0.23},
            second={"A": 0.51,
                    "T": 0.26,
                    "C": 0.23},
            third={"T": 0.15,
                   "C": 0.38,
                   "G": 0.47})
    print(x.aat.get_non_0_freq())



