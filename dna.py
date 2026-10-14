dna = input()

print(*(dna.count(base) for base in "ACGT"))