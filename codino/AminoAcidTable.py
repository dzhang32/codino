class AminoAcidTable():

    def __init__(self):

        self._freq = {
            "A": 0.00,
            "C": 0.00,
            "D": 0.00,
            "E": 0.00,
            "F": 0.00,
            "G": 0.00,
            "H": 0.00,
            "I": 0.00,
            "K": 0.00,
            "L": 0.00,
            "M": 0.00,
            "N": 0.00,
            "P": 0.00,
            "Q": 0.00,
            "R": 0.00,
            "S": 0.00,
            "T": 0.00,
            "V": 0.00,
            "W": 0.00,
            "X": 0.00,
            "Y": 0.00
        }

        self._aa_to_codon = {
            "C": ["TGC", "TGT"],
            "S": ["AGC", "AGT", "TCA", "TCC", "TCG", "TCT"],
            "T": ["ACA", "ACC", "ACG", "ACT"],
            "P": ["CCA", "CCC", "CCG", "CCT"],
            "A": ["GCA", "GCC", "GCG", "GCT"],
            "G": ["GGA", "GGC", "GGG", "GGT"],
            "N": ["AAC", "AAT"],
            "D": ["GAC", "GAT"],
            "E": ["GAA", "GAG"],
            "Q": ["CAA", "CAG"],
            "H": ["CAC", "CAT"],
            "R": ["AGA", "AGG", "CGA", "CGC", "CGG", "CGT"],
            "K": ["AAA", "AAG"],
            "M": ["ATG"],
            "I": ["ATA", "ATC", "ATT"],
            "L": ["CTA", "CTC", "CTG", "CTT", "TTA", "TTG"],
            "V": ["GTA", "GTC", "GTG", "GTT"],
            "F": ["TTC", "TTT"],
            "Y": ["TAC", "TAT"],
            "W": ["TGG"],
            "X": ["TAA", "TAG", "TGA"]
        }

    def get_non_0_freq(self):
        return {k:v for (k,v) in self.freq.items() if v != 0.0}

    def set_freq(self, aa, freq):
        if aa not in self.freq.keys():
            raise KeyError("Keys must be amino acids")
        elif freq > 1 or freq < 0:
            raise ValueError("Values must be between 0 and 1")
        self._freq[aa] = freq

    @property
    def freq(self):
        return self._freq

    @property
    def aa_to_codon(self):
        return self._aa_to_codon

if __name__ == "__main__":

    y = AminoAcidTable()
    print(y.freq)
    print({key:value for (key,value) in y.freq.items() if value != 0.0})
