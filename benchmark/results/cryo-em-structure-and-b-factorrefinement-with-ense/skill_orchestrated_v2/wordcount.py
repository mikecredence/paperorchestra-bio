import re, sys, json
path = sys.argv[1]
with open(path, encoding='utf-8') as f:
    text = f.read()
text = re.sub(r'\\begin\{.*?\}|\\end\{.*?\}', ' ', text)
text = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})*', ' ', text)
text = re.sub(r'[{}%]', ' ', text)
words = re.findall(r"[A-Za-z][A-Za-z0-9'\-]*", text)
print(json.dumps({'words': len(words)}))
