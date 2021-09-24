class FreqTable:

    # placeholder _freq
    def __init__(self, freq):
        self._freq = freq

    @property
    def freq(self):
        return self._freq

    def set_freq(self, key, value):
        if key not in self.freq.keys():
            raise KeyError("Keys must be one of" +
                           ", ".join(self.freq.keys()))

        elif value > 1 or value < 0:
            raise ValueError("Values must be between 0 and 1")

        self._freq[key] = value

    def get_non_0_freq(self):
        return {k: v for (k, v) in self.freq.items() if v != 0.0}

if __name__ == "__main__":

    class Animal:
        def __init__(self, legs):
            self.legs = legs

    class TwoLeggedAnimal(Animal):
        def __init__(self):
            super().__init__(2)


    x = TwoLeggedAnimal()