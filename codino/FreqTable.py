class FreqTable:

    # placeholder _freq
    def __init__(self, freq):

        self._freq = freq

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        poss_keys = self.freq.keys()

        if any([k not in poss_keys for k in value.keys()]):
            raise KeyError("Keys must be one of" +
                           ", ".join(self.freq.keys()))

        elif any([v > 1 or v < 0 for v in value.values()]):
            raise ValueError("Values must be between 0 and 1")

        self._freq.update(value)

    def set_ind_freq(self, key, value):
        if key not in self.freq.keys():
            raise KeyError("Keys must be one of" +
                           ", ".join(self.freq.keys()))

        elif value > 1 or value < 0:
            raise ValueError("Values must be between 0 and 1")

        self._freq[key] = value

    def get_non_0_freq(self):
        return {k: v for (k, v) in self.freq.items() if v != 0.0}

if __name__ == "__main__":
    pass