# bibliotex

This repository contains a rather large collection of `.bib` files,
most of which were accumulated over the course of my graduate studies.
They are loosely organized by category
and have been (mostly) hand-checked for correctness.

Note that there are several idiosyncrasies to this collection:
- Unicode literals are used wherever possible.
- Macros from `chemformula` are used for typesetting chemical formulas.
- Macros from `siunitx` are used for typesetting quantities.
- Some `.bib` fields (e.g., notes) are commented out with a `%`.

These peculiarities may cause problems for direct use in typical LaTeX workflows;
however, most of these can be overcome using something like `glob2bib`.

A convenience script `gen_ref_list.py` is also included,
which generates a large (~100 page) `.pdf` containing all of the entries
typeset in the style of [Physical Review X](https://journals.aps.org/prx/).
Generating the `.pdf` requires LuaLaTeX and BibLaTeX/Biber.
