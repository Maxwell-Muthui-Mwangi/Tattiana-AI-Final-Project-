import pandas as pd

# Load references from the file with specified encoding
with open('max1references.txt', 'r', encoding='utf-8') as file:
    references = file.readlines()

# Remove duplicates and sort references
unique_references = sorted(set(references))

# Save unique references to a new file with specified encoding
with open('unique_references.txt', 'w', encoding='utf-8') as file:
    for reference in unique_references:
        file.write(reference)

print("Duplicates removed and references sorted.")
