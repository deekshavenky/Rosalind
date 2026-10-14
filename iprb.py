#mendelian inheritance:
# Three positive integers 
# k: ho moxygous dominant 
with open ("rosalind_iprb.txt") as f:
    k, m, n = map (int, f.read().split())
    
total_pop = k + m + n
total_pairs = total_pop * (total_pop - 1) / 2

het_pairs = m*(m-1)/2
rec_pairs = n*(n-1)/2
mixed_pairs = m*n
aa_babies = het_pairs * 0.25 +rec_pairs * 1 + mixed_pairs * 0.5
prob_aa = aa_babies/total_pairs
prob_dom = 1 - prob_aa
print (prob_dom)
