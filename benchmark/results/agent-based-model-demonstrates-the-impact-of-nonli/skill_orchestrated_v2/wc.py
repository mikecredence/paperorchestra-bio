"""Word counter for LaTeX manuscripts."""
import re
import sys

with open(sys.argv[1], encoding="utf-8") as f:
    t = f.read()

# Remove abstract-to-end? Count full document body; strip preamble.
body = t.split(r"\begin{document}", 1)[-1].split(r"\end{document}", 1)[0]
# Strip comments
body = re.sub(r"(?m)^%.*", "", body)
# Remove \command[opt]{arg}{arg2} forms (best-effort, one level)
body = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^{}]*\})?(\{[^{}]*\})?", " ", body)
body = re.sub(r"[{}\\]", " ", body)

words = [w for w in body.split() if any(c.isalpha() for c in w)]
print(len(words))
