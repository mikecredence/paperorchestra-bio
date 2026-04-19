import re
with open('main.tex', encoding='utf-8') as f:
    tex = f.read()
with open('references.bib', encoding='utf-8') as f:
    bib = f.read()
cites = set()
for m in re.finditer(r'\\cite\{([^}]+)\}', tex):
    for k in m.group(1).split(','):
        cites.add(k.strip())
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib))
missing = cites - bib_keys
unused = bib_keys - cites
print('cites in text:', len(cites))
print('bib entries:', len(bib_keys))
print('missing in bib:', sorted(missing))
print('unused bib entries:', sorted(unused))
