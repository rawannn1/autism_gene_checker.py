
---

### `autism_gene_checker.py`
```python
from Bio import Entrez

# Set your email for NCBI Entrez
Entrez.email = "your@email.com"  # <-- Replace with your actual email

# Ask the user to enter a gene
gene = input("Enter a gene name (e.g., SHANK3, MECP2): ")

# Search NCBI Gene for that gene in humans
handle = Entrez.esearch(db="gene", term=f"{gene}[sym] AND Homo sapiens[orgn]")
record = Entrez.read(handle)
handle.close()

# If found, fetch the gene summary
if record["IdList"]:
    gene_id = record["IdList"][0]
    handle = Entrez.efetch(db="gene", id=gene_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()

    summary = records[0].get("Entrezgene_summary", "No summary available.")

    print(f"\n Gene found: {gene}")
    print(f" Summary from NCBI:\n{summary}")

    # Optional check: if 'autism' is mentioned
    if "autism" in summary.lower():
        print("\n This gene is likely associated with autism (mentioned in summary).")
    else:
        print("\n⚠ No direct mention of autism in this summary — further research needed.")

else:
    print("\n Gene not found in NCBI for Homo sapiens.")
