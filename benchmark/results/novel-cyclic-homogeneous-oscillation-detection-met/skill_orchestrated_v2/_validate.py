import re, pathlib
root = pathlib.Path(__file__).parent
tex = (root / "main.tex").read_text(encoding="utf-8")
bib = (root / "references.bib").read_text(encoding="utf-8")
cites = set()
for m in re.findall(r"\\cite[tp]?\{([^}]+)\}", tex):
    for k in m.split(","):
        cites.add(k.strip())
bib_keys = set(re.findall(r"@[A-Za-z]+\{([A-Za-z0-9_]+),", bib))
missing = cites - bib_keys
unused = bib_keys - cites
words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", tex))
print("Cite keys used:", len(cites))
print("Bib entries:", len(bib_keys))
print("Missing (cited but no bib):", sorted(missing))
print("Unused (in bib but not cited):", sorted(unused))
print("Word count approx:", words)
