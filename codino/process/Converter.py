from codino.data import CodonDesign, CodonTable, AminoAcidTable


class Converter:

    def __init__(self):
        self.cd = CodonDesign()
        self.ct = CodonTable()
        self.aat = AminoAcidTable()

    def refresh(self):
        self.cd.first.refresh()
        self.cd.second.refresh()
        self.cd.third.refresh()
        self.ct.refresh()
        self.aat.refresh()

    def cd_to_aa(self, first, second, third, refresh=True):
        self.cd.set_codon_design(first, second, third)
        self._cd_to_ct()
        self._ct_to_aa()

        aa_freq = self.aat.get_non_0_freq().copy()

        if refresh:
            self.refresh()

        return aa_freq

    def _cd_to_ct(self):
        new_freq = {}
        for k1 in self.cd.first.freq:
            if self.cd.first.freq[k1] == 0.0:
                continue
            for k2 in self.cd.second.freq:
                if self.cd.second.freq[k2] == 0.0:
                    continue
                for k3 in self.cd.third.freq:
                    if self.cd.third.freq[k3] == 0.0:
                        continue
                    codon = k1 + k2 + k3
                    freq = self.cd.first.freq[k1] * \
                           self.cd.second.freq[k2] * \
                           self.cd.third.freq[k3]

                    new_freq[codon] = freq

        # use freq.setter - check values sum to 1
        self.ct.freq = new_freq

    def _ct_to_aa(self):
        for aa, codons in self.aat.aa_to_codon.items():
            freq = sum([self.ct.freq[c] for c in codons])
            self.aat.freq[aa] = freq

if __name__ == "__main__":
    pass



