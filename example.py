from codino.process import Converter

c = Converter()

# converting from codon design to AA frequencies
# input the nucleotide frequencies at each position
c.cd_to_aa(first={"A": 1}, second={"T": 1}, third={"G": 1})
# Out: {'M': 1}

# converting from AA frequency to codon design
# input the desired AA frequencies
first, second, third = c.aa_to_cd(aa={'D': 0.4, 'N': 0.6})

# we can check the output by converting the codon design back to AA frequencies
c.cd_to_aa(first, second, third) == {'D': 0.4, 'N': 0.6}
# Out: True

# for more complex examples, the codon design will be an estimate
exp_aa = {'A': 0.1771,
          'D': 0.208131,
          'E': 0.18456899999999998,
          'I': 0.031694,
          'K': 0.055131,
          'M': 0.028106000000000003,
          'N': 0.062169,
          'T': 0.0529,
          'V': 0.2002}

first, second, third = c.aa_to_cd(aa=exp_aa)
pred_aa = c.cd_to_aa(first, second, third)

pred_aa == exp_aa
# Out: False

# in this case, it can be helpful to obtain the errors
errors = [abs(pred_aa[a] - exp_aa[a]) for a in exp_aa]

# mean error
print(sum(errors)/len(errors))
# Out: 0.0055103958222222325

# sum error
print(sum(errors))
# Out: 0.049593562400000096

