# bibliotex

This repository contains a rather large collection of `.bib` files,
most of which were accumulated over the course of my graduate studies.
They are loosely organized by category
and have been hand-checked for correctness (mostly).

Note that there are several idiosyncrasies to this collection:
- Unicode literals are used wherever possible.
- Macros from [`chemformula`] are used for typesetting chemical formulas.
- Macros from [`siunitx`] are used for typesetting quantities.
- Some `.bib` fields (e.g., notes) are commented out with a `%`.

These peculiarities may cause problems for direct use in typical LaTeX workflows;
however, most of these can be overcome using something like [`glob2bib`].

A convenience script `generate_bibliotex.py` is also included,
which generates `bibliotex.pdf` - a 100+ page `.pdf` containing all entries
typeset in the style of [Physical Review X] (with hyperlinks)!
Generating the `.pdf` requires LuaLaTeX and BibLaTeX/Biber.

[`glob2bib`]: https://github.com/rmlmcfadden/glob2bib
[`chemformula`]: https://ctan.org/pkg/chemformula
[`siunitx`]: https://ctan.org/pkg/siunitx
[Physical Review X]: https://journals.aps.org/prx/
