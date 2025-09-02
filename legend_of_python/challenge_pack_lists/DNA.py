#DNA 🧬

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = "GCt"

item_found = False

for i in dna_sequence:
  if i == item_to_find:
    item_found = True
    print("Item Found!")
if not item_found:
    print("Item not found.")
