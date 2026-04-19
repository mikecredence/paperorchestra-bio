import re, os
base = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base, 'main.tex'), 'r', encoding='utf-8') as f:
    tex = f.read()
with open(os.path.join(base, 'references.bib'), 'r', encoding='utf-8') as f:
    bib = f.read()

cite_pat = re.compile(r"\\cite[pt]?\{([^}]+)\}")
cited = set()
for m in cite_pat.finditer(tex):
    for k in m.group(1).split(','):
        cited.add(k.strip())
bib_keys = set(re.findall(r"@\w+\{([^,]+),", bib))
print('n_cited=', len(cited), 'n_bib=', len(bib_keys))
print('MISSING from bib:', sorted(cited - bib_keys))
print('UNUSED in bib:', sorted(bib_keys - cited))

s = tex
s = re.sub(r"%[^\n]*", "", s)
s = re.sub(r"\\(begin|end)\{[^}]+\}", " ", s)
s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})*", " ", s)
s = re.sub(r"[{}$]", " ", s)
words = re.findall(r"[A-Za-z][A-Za-z'\-]*", s)
print('words=', len(words))
