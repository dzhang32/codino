from codino import CodonDesign, CodonTable

class Converter():

    def __init__(self):
        self.cd = CodonDesign()
        self.ct = CodonTable()

    def to_aa(self, first, second, third):
        cc = self._cd_to_ct()
        return cc

    def _cd_to_ct(self):
        return 5

    def _cc_to_aa(self):
        pass

if __name__ == "__main__":

    x = Converter()
    print(x.to_aa())