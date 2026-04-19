import re
with open('main.tex', encoding='utf-8') as f:
    t = f.read()
idx = t.find(r'\begin{document}')
body = t[idx:]
body = re.sub(r'%.*', '', body)
body = re.sub(r'\\(cite|citealp|citep|citet|ref|label|includegraphics|bibliography|bibliographystyle)\{[^}]*\}', ' ', body)
body = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?\{[^}]*\}', ' ', body)
body = re.sub(r'\\[a-zA-Z]+', ' ', body)
body = re.sub(r'[{}]', ' ', body)
words = [w for w in re.split(r'\s+', body) if w.strip() and any(c.isalpha() for c in w)]
print('prose words:', len(words))
