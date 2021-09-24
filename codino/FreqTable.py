class FreqTable:

    def __init__(self, freq):
        self._freq = freq

    @property
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, value):
        self._check_dict(value)
        self._check_keys(value)
        self._check_values(value)

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

    @staticmethod
    def _check_dict(value):
        if type(value) is not dict:
            raise TypeError("Value must be a dictionary")

    def _check_keys(self, value):
        poss_keys = self.freq.keys()

        if any([k not in poss_keys for k in value.keys()]):
            raise KeyError("Keys must be one of" +
                           ", ".join(self.freq.keys()))

    @staticmethod
    def _check_values(value):
        if any([v > 1 or v < 0 for v in value.values()]):
            raise ValueError("Values must be between 0 and 1")
        elif sum(value.values()) != 1:
            raise ValueError("Values must sum to 1")


if __name__ == "__main__":
    x = FreqTable()