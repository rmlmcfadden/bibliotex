# Simple instructions for compiling all_refs.tex.
#
# Note: increasing max_repeat from its default value (5) is necessary
# due to the large (and ever-growing) size of all_refs.tex

bibliotex:
	latexmk -lualatex -e '$$max_repeat=20' bibliotex

bibliotex2:
	lualatex bibliotex.tex
	biber bibliotex
	lualatex bibliotex.tex
	lualatex bibliotex.tex

clean:
	latexmk -c
