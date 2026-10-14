# two dna strings s and t of equal length 
# return hamming distance 
with open("rosalind_hamm (1).txt", "r") as file:
    lines = file.read().strip().splitlines()
    s = lines[0]
    t = lines[1]
mismatches = 0
for i in range(len(s)):
    if s[i] != t[i]:
        mismatches += 1

print(mismatches)
    
