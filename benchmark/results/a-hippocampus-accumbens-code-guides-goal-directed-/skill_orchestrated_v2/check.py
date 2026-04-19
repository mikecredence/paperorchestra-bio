import re, pathlib
here = pathlib.Path(__file__).parent
t = (here/'main.tex').read_text(encoding='utf-8')
i = (here/'intro_relwork.tex').read_text(encoding='utf-8')
combined = t + '\n' + i
# strip \input
text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})?', ' ', combined)
text = re.sub(r'\$[^$]*\$', ' NUM ', text)
text = re.sub(r'[{}\\]', ' ', text)
words = [w for w in text.split() if len(w) > 1]
print('Word count:', len(words))
cites = re.findall(r'\\cite[a-z]*\{([^}]+)\}', combined)
all_keys = set()
for c in cites:
    for k in c.split(','):
        all_keys.add(k.strip())
print('Unique cite keys:', len(all_keys))
b = (here/'references.bib').read_text(encoding='utf-8')
bib_keys = set(re.findall(r'@\w+\{([^,]+),', b))
print('Bib entries:', len(bib_keys))
print('Orphan cites (in tex not in bib):', sorted(all_keys - bib_keys))
print('Unused bib keys:', sorted(bib_keys - all_keys))
