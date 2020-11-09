# Simple instructions for compiling all_refs.tex.
#
# Note: increasing max_repeat from its default value (5) is necessary
# due to the large (and ever-growing) size of all_refs.tex

all_refs:
	latexmk -pdflua -e '$$max_repeat=10' all_refs

all_refs2:
	lualatex all_refs.tex
	biber all_refs
	lualatex all_refs.tex
	lualatex all_refs.tex

clean:
	latexmk -c
