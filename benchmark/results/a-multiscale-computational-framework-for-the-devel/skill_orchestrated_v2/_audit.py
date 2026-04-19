import re, os, json
workspace = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(workspace, 'main.tex'), encoding='utf-8') as f:
    t = f.read()

clean = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', t)
clean = re.sub(r'[{}]', ' ', clean)
clean = re.sub(r'%.*', '', clean)
words = clean.split()
print('Approx word count:', len(words))
print('Line count:', len(t.splitlines()))

cites = re.findall(r'\\cite[a-z]*\{([^}]*)\}', t)
keys = set()
for c in cites:
    for k in c.split(','):
        keys.add(k.strip())
print('Unique cite keys:', len(keys))

with open(os.path.join(workspace, 'references.bib'), encoding='utf-8') as f:
    bib = f.read()
bib_keys = set(re.findall(r'@[a-zA-Z]+\{([^,]+),', bib))
print('Bib keys:', len(bib_keys))

missing = keys - bib_keys
print('Missing in bib:', missing)
unused = bib_keys - keys
print('Unused bib entries:', unused)
