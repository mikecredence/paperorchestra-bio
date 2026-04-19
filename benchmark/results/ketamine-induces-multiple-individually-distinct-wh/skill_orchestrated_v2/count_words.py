import re, sys, os
p = os.path.join(os.path.dirname(__file__), 'main.tex')
with open(p, 'r', encoding='utf-8') as f:
    s = f.read()
# strip comments
s = re.sub(r'%[^\n]*', '', s)
# strip \begin{} \end{}
s = re.sub(r'\\(begin|end)\{[^}]+\}', ' ', s)
# strip commands with one brace arg
s = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})*', ' ', s)
# remove leftover braces
s = re.sub(r'[{}$]', ' ', s)
words = re.findall(r"[A-Za-z][A-Za-z'\-]*", s)
print('word_count=', len(words))
