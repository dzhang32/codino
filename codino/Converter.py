from codino import CodonDesign, CodonTable

class Converter():

    def __init__(self):
        self.cd = CodonDesign()
        self.ct = CodonTable()

    def to_aa(self, first = {}, second = {}, third = {}):
        self.cd.set_codon_design(first, second, third)
        self._cd_to_ct()

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

    def _cc_to_aa(self):
        pass

if __name__ == "__main__":

    x = Converter()
    x.to_aa(first = {"A": 1.0},
            second = {"T": 1.0},
            third = {"G": 1.0})
    print(x.ct.freq)


