# bibliotex

This repository contains a <i>huge</i> collection of [BibTeX] (`.bib`) files
that I use in my academic work. Most of the references are related to materials
science, but the sprawl of topics extends well beyond this. Much of the content
here was accumulated over the course of my graduate studies, with more recent
updates following my current projects/interests.

Most of the entries have been hand-checked to ensure correctness
(for a discussion on <i>why</i> this is necessary, see, for example,
<https://clauswilke.com/blog/2015/10/02/bibtex/>). Though I have attempted to
organize the entries thematically, their grouping criteria is, admittedly,
somewhat loose/arbitrary.

Compared to more "traditional" methods of managing `.bib` entries, there are
several peculiarities to this collection:

- Unicode literals are used wherever possible.
- Macros from [chemformula] are used for typesetting <i>all</i> chemical formulas.
- Macros from [siunitx] are used for typesetting <i>all</i> quantities.
- Some `.bib` fields (e.g., `notes`, `eprint`, etc.) are commented out with a `%`.
- Somewhat long/verbose citation keys are used to (uniquely) identify each `.bib` entry.

Some of these choices may cause problems for typical [LaTeX] workflows;
however, most can be overcome using something like [glob2bib] to selectively
parse through (and modify) the formatting of the desired entries
(e.g., swapping unicode greek characters with equivalent math-mode commands).

A convenience script `generate_bibliotex.py` is also included, which generates
`bibliotex.tex`: the source code for a 150+ page `.pdf` containing <i>every</i>
entry in this collection
(typeset in the style of [Physical Review X] - with hyperlinks)!
The build procedure can be automated by running:

```bash
python3 generate_bibliotex.py
make
```

Note that compiling `bibliotex.tex` (which generates `bibliotex.pdf`) requires
[LuaLaTeX] and [BibLaTeX]/[biber].

[glob2bib]: https://github.com/rmlmcfadden/glob2bib
[chemformula]: https://ctan.org/pkg/chemformula
[siunitx]: https://ctan.org/pkg/siunitx
[Physical Review X]: https://journals.aps.org/prx/
[LaTeX]: https://ctan.org/pkg/latex
[LuaLaTeX]: https://ctan.org/pkg/luatex
[BibLaTeX]: https://ctan.org/pkg/biblatex
[biber]: https://ctan.org/pkg/biber
[BibTeX]: https://ctan.org/pkg/bibtex
