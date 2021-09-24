class CodonDesign():

    _first = {"A": 0.0,
              "T": 0.0,
              "C": 0.0,
              "G": 0.0}

    _second = {"A": 0.0,
               "T": 0.0,
               "C": 0.0,
               "G": 0.0}

    _third = {"A": 0.0,
              "T": 0.0,
              "C": 0.0,
              "G": 0.0}

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        self._check_keys(value)
        self._check_values(value)
        self._first.update(value)

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        self._check_keys(value)
        self._check_values(value)
        self._second.update(value)

    @property
    def third(self):
        return self._third

    @third.setter
    def third(self, value):
        self._check_keys(value)
        self._check_values(value)
        self._third.update(value)

    def _check_keys(self, value):
        poss_keys = ["A", "T", "C", "G"]

        if any([k not in poss_keys for k in value.keys()]):
            raise KeyError("Keys must be nucleotides")

    def _check_values(self, value):
        if any([v > 1 or v < 0 for v in value.values()]):
            raise ValueError("Values must be between 0 and 1")

if __name__ == "__main__":

    x = CodonDesign()

    print(x.third)
    x.third = {"A" : 1.0}
    print(x.third)

    # x.third = {"D": 1.0}
    x.third = {"A": 4.0}
