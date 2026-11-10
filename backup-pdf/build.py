"""Build the 2-page backup PDF of the workshop.html Copilot exercises.

Prompt text is taken verbatim from workshop.html on every build, so rerun this
whenever the page changes:  python3 -I build.py
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / 'workshop.html'
URL = 'https://wmgmm.github.io/thematts/workshop.html'

prompts = json.loads(subprocess.run(
    [sys.executable, '-I', str(HERE / 'extract_prompts.py'), str(SRC)],
    check=True, capture_output=True, text=True).stdout)

ESC = {
    '\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '#': r'\#', '$': r'\$',
    '%': r'\%', '&': r'\&', '_': r'\_', '^': r'\textasciicircum{}',
    '~': r'\textasciitilde{}', '<': r'\textless{}', '>': r'\textgreater{}',
    '|': r'\textbar{}', '"': r'\textquotedbl{}', "'": r'\textquotesingle{}',
    '`': r'\textasciigrave{}', '–': r'\textendash{}', '•': r'\textbullet{}',
    '-': '-{}',
}

def esc(s):
    return ''.join(ESC.get(c, c) for c in s)

def code_line(s):
    # Monospace line; each space is a real, copyable space.
    return r'\codeline{' + ''.join(r'\ ' if c == ' ' else esc(c) for c in s) + '}'

def box(pid):
    """Turn a prompt into LaTeX, keeping its line breaks and code fence."""
    out, in_code = [], False
    for line in prompts[pid].split('\n'):
        if line.startswith('```'):
            out.append(code_line(line))
            in_code = not in_code
        elif in_code:
            out.append(code_line(line))
        elif not line.strip():
            out.append(r'\gap')
        elif line.startswith('• '):
            out.append(r'\bul{' + esc(line[2:]) + '}')
        else:
            out.append(esc(line) + r'\par')
    return r'\begin{pbox}' + '\n' + '\n'.join(out) + '\n' + r'\end{pbox}'

tex = (HERE / 'template.tex').read_text(encoding='utf-8')
tex = tex.replace('@@URL@@', URL)
tex = re.sub(r'@@([a-z0-9-]+)@@', lambda m: box(m.group(1)), tex)
(HERE / 'workshop-exercises.tex').write_text(tex, encoding='utf-8')
subprocess.run(['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error',
                'workshop-exercises.tex'], cwd=HERE, check=True)
