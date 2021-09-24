from codino import FreqTable

class CodonDesign():

    def __init__(self):

        self.first = FreqTable({"A": 0.0,
                                "T": 0.0,
                                "C": 0.0,
                                "G": 0.0})

        self.second = FreqTable({"A": 0.0,
                                 "T": 0.0,
                                 "C": 0.0,
                                 "G": 0.0})

        self.third = FreqTable({"A": 0.0,
                                "T": 0.0,
                                "C": 0.0,
                                "G": 0.0})

    def set_codon_design(self, first, second, third):
        self.first.freq = first
        self.second.freq = second
        self.third.freq = third

if __name__ == "__main__":
    x = CodonDesign()
    x.third.freq = {"A": 0.0, "T": 0.0}
