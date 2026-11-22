"""Bilingual spell check for the paracol manual.
Spanish column = before \\switchcolumn inside paracol; English after.
Outside paracol a word is flagged only if unknown in both languages.
Words used >=3 times in the corpus are whitelisted (technical jargon).

Usage:  python tools/spellcheck.py <repo> introprog.tex ...
Needs `pip install spylls` and Hunspell dictionaries es.aff/es.dic and
en.aff/en.dic (e.g. from LibreOffice) in the folder given by the
LCC_DICT environment variable (default: tools/dict, not versioned)."""
import re, sys, os, collections
from spylls.hunspell import Dictionary
D = os.environ.get("LCC_DICT", os.path.join(os.path.dirname(__file__), "dict"))
_es = Dictionary.from_files(os.path.join(D, "es"))
_en = Dictionary.from_files(os.path.join(D, "en"))
class W:
    def __init__(s, d): s.d, s.c = d, {}
    def __contains__(s, w):
        if w not in s.c: s.c[w] = s.d.lookup(w) or s.d.lookup(w.capitalize())
        return s.c[w]
    def correction(s, w):
        return next(iter(s.d.suggest(w)), None)
es, en = W(_es), W(_en)
REPO = sys.argv[1]
files = sys.argv[2:]

def strip(line):
    line = re.sub(r"(?<!\\)%.*", "", line)
    line = re.sub(r"\\mint(inline)?\{\w+\}(\{[^}]*\}|\|[^|]*\|)", " ", line)
    line = re.sub(r"\\(ref|eqref|label|index|cite|includegraphics|input\w*|href|url|hyperlink|begin|end|texttt|emph\{\\texttt|usepackage|chaptermark|sectionmark)(\[[^\]]*\])?\{[^}]*\}", " ", line)
    line = re.sub(r"\$[^$]*\$", " ", line)
    line = re.sub(r"\\[a-zA-Z]+\*?", " ", line)
    return line

word_re = re.compile(r"(?<![\w\\_])[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{3,}(?![\w_])")
hits = []
corpus = collections.Counter()
for f in files:
    state, skip = None, False
    for i, raw in enumerate(open(os.path.join(REPO, f), encoding="utf8"), 1):
        if re.search(r"\\begin\{(minted|verbatim|equation\*?|align\*?|tikzpicture|pmatrix|tabular)", raw): skip = True
        if skip:
            if re.search(r"\\end\{(minted|verbatim|equation\*?|align\*?|tikzpicture|pmatrix|tabular)", raw): skip = False
            continue
        if "\\begin{paracol}" in raw: state = "es"
        line = strip(raw)
        parts = raw.split("\\switchcolumn")
        if len(parts) > 1 and state:
            state = "en" if state == "es" else "es"
        if "\\selectlanguage{english}" in raw and state: state = "en"
        for w in word_re.findall(line):
            corpus[w.lower()] += 1
            hits.append((f, i, w, state))
        if "\\end{paracol}" in raw: state = None

out = collections.OrderedDict()
for f, i, w, st in hits:
    lw = w.lower()
    if corpus[lw] >= 3:
        continue
    if st == "es":
        bad = lw not in es
    elif st == "en":
        bad = lw not in en
    else:
        bad = lw not in es and lw not in en
    if bad:
        d = es if st == "es" else en if st == "en" else es
        sug = d.correction(lw) if len(lw) < 15 else None
        out.setdefault((w, st), []).append(f"{f}:{i}")
        out[(w, st)] = out[(w, st)]
        out[(w, st, "s")] = sug
for k, v in out.items():
    if len(k) == 3:
        continue
    w, st = k
    print(f"{v[0]}\t[{st}]\t{w}\t-> {out[(w, st, 's')]}\t{'' if len(v)==1 else '+'+str(len(v)-1)}")
