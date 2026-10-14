dna = input()
complement = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C",
}
reverse_complement = ""

for base in dna[::-1]:
    reverse_complement += complement [base]

print (reverse_complement)