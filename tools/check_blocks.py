"""Extract minted python blocks from each chapter and execute them in a
shared namespace per chapter, reporting blocks that raise exceptions.
IPython-style sessions (In [n]: / ...:) are reduced to their input lines.

Usage:  python tools/check_blocks.py [--prelude file.py] <repo> introprog.tex ...

--prelude file.py: run file.py in each chapter's namespace before its
blocks. Use it for functions the text leaves as exercises (e.g. the
`regressive` function of the systems chapter); keep that file with the
solutions, not in this repository.

Blocks run inside a temporary copy of datos/, so files they write never
touch the repository. Every codigos/* folder is put on sys.path so that
blocks importing the chapter modules work. Some failures are expected:
deliberate errors, pseudocode and output-only blocks."""
import re, sys, io, os, contextlib, traceback, signal, builtins, shutil, tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

args = sys.argv[1:]
PRELUDE = None
if args[:1] == ["--prelude"]:
    PRELUDE = os.path.abspath(args[1])
    args = args[2:]
REPO = os.path.abspath(args[0])
chapters = args[1:]
blk = re.compile(r"\\begin\{minted\}(?:\[[^\]]*\])?\{(python|python3|ipython|pycon)\}(.*?)\\end\{minted\}", re.S)
prompt = re.compile(r"^\s*(In \[\d*\]:|>>>|\.\.\.:?|\s+\.\.\.:)\s?")

def to_code(src):
    lines = src.splitlines()
    if any(re.match(r"^\s*(In \[\d*\]:|>>>)", l) for l in lines):
        out = []
        for l in lines:
            m = prompt.match(l)
            if m:
                out.append(l[m.end():])
        return "\n".join(out)
    return src

builtins.input = lambda *a, **k: "3"
for d in sorted(os.listdir(os.path.join(REPO, "codigos"))):
    p = os.path.join(REPO, "codigos", d)
    if os.path.isdir(p):
        sys.path.append(p)
WORK = tempfile.mkdtemp(prefix="lcc_blocks_")
shutil.copytree(os.path.join(REPO, "datos"), os.path.join(WORK, "datos"))
for ch in chapters:
    txt = open(os.path.join(REPO, ch), encoding="utf8").read()
    ns = {"__name__": "__main__"}
    os.chdir(os.path.join(WORK, "datos"))
    print(f"##### {ch}")
    if PRELUDE:
        exec(compile(open(PRELUDE, encoding="utf8").read(), PRELUDE, "exec"), ns)
    for m in blk.finditer(txt):
        line = txt[:m.start()].count("\n") + 1
        code = to_code(m.group(2))
        if not code.strip():
            continue
        try:
            compiled = compile(code, f"{ch}:{line}", "exec")
        except SyntaxError as e:
            print(f"SYNTAX {ch}:{line}: {e.msg} -> {e.text!r}")
            continue
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                exec(compiled, ns)
        except Exception as e:
            print(f"ERROR  {ch}:{line}: {type(e).__name__}: {str(e)[:160]}")
        plt.close("all")
