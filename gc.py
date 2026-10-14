
def gc_content(dna):
        gc_count = dna.count("G") + dna.count("C")
        return (gc_count / len(dna)) * 100
with open("rosalind_gc (4).txt", "r") as file:
    fasta = file.read()

records = fasta.strip().split(">")

best_id = None
best_gc = 0

for record in records:
    if record == "":
        continue
    lines = record.splitlines()
    seq_id = lines[0]
    dna = "".join(lines[1:])

    current_gc = gc_content(dna)
    if current_gc> best_gc:
         best_gc = current_gc
         best_id = seq_id
print(f"Best ID: {best_id}, Best GC Content: {best_gc:.6f}%")
