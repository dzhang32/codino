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

        self.freq.update(value)

    def get_non_0_freq(self):
        return {k: v for (k, v) in self.freq.items() if v != 0.0}

    @staticmethod
    def _check_dict(value):
        if type(value) is not dict:
            raise TypeError("Value must be a dictionary")

    def _check_keys(self, value):
        poss_keys = self.freq.keys()

        if any([k not in poss_keys for k in value.keys()]):
            raise KeyError("Keys must be one of: " +
                           ", ".join(self.freq.keys()))

    def _check_values(self, value):
        if any([v > 1 or v < 0 for v in value.values()]):
            raise ValueError("Values must be between 0 and 1")

        # check that values sum to 1, without changing _freq attribute
        # round(X, 3) - avoid math errors causing problems
        tmp_freq = self._freq.copy()
        tmp_freq.update(value)
        if round(sum(tmp_freq.values()), 3) != 1:
            raise ValueError("Values must sum to 1")

if __name__ == "__main__":
    pass
