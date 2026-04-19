import re
base = 'benchmark/results/predicting-distributed-working-memory-activity-in-/skill_orchestrated_v2/'
with open(base+'main.tex','r',encoding='utf-8') as f: main=f.read()
with open(base+'references.bib','r',encoding='utf-8') as f: bib=f.read()
cited = set(re.findall(r'\\cite\{([^}]+)\}', main))
cited_keys = set()
for c in cited:
    for k in c.split(','):
        cited_keys.add(k.strip())
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib))
print('Citations used:', len(cited_keys))
print('Bib entries:', len(bib_keys))
print('Missing keys:', cited_keys - bib_keys)
print('Unused bib entries:', bib_keys - cited_keys)
text = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', main)
text = re.sub(r'%.*', ' ', text)
text = re.sub(r'\{|\}|\\\\','',text)
words = [w for w in text.split() if w.strip() and any(c.isalpha() for c in w)]
print('Word count (rough):', len(words))
