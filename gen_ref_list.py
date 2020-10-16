#!/usr/bin/python3

# Automatically generate a list of all *.bib files found recursively in the
# current directory and output them as a list, assuming BibLaTeX as the
# bibliography manager, in a file called list.tex. It is assumed that all
# entries in the .bib files of the BibTeX type.

import os
from glob import glob
from datetime import datetime

# find the name of the current directory
pwd = os.path.realpath( os.getcwd() ).split('/')[-1]

# recursively find all the .bib files in this directory
bib = glob('**/*.bib', recursive=True)

# sort the entries alphabetically
bib.sort()

# explicit .bib entry type for \addbibresource options
dt = 'datatype = bibtex'

# open the output file and give it a handle
with open('list.tex', 'w') as fh :
   # get the current time
   t = datetime.now()
   # write a header to the file
   fh.write('% generated automatically using: gen_ref_list.py\n')
   fh.write('% last updated: ' + t.strftime('%Y-%m-%d %H:%M:%S') + '\n')
   fh.write('\n')
   # loop over the list of .bib files
   for b in bib :
      fh.write(r'\addbibresource[' + dt + ']{' + pwd + '/' + b + '}\n')
   fh.write('\n')


# concatenate the content of each .bib into a single, monolithic file
# https://stackoverflow.com/a/13613375
# open the output file and give it a handle
'''
with open('all.txt', 'w') as output_file :
   # loop over the list of .bib files
   for b in bib :
      # open the .bib file (read-only)
      with open(b, 'r') as input_file :
         # write the .bib contents to the output file
         output_file.write( input_file.read() )
'''

# write another file that creates a .tex file for testing compilation of all the
# the .bib files. the output is organized by filename. citation keys are printed
# in the margins next to the bibliographies.

# open the output file and give it a handle
with open('all_refs.tex', 'w') as fh :
   # get the current time
   t = datetime.now()
   # write a header to the file
   fh.write('% generated automatically using: gen_ref_list.py\n')
   fh.write('% last updated: ' + t.strftime('%Y-%m-%d %H:%M:%S') + '\n')
   fh.write('\n')
   fh.write(r'\documentclass[letterpaper, 10pt, oneside, openany]{report}' + '\n')
   fh.write('\n')
   fh.write(r'\usepackage[' + '\n')
   fh.write('\tletterpaper,' + '\n')
   fh.write('\tinner = 2in,' + '\n')
   fh.write('\touter = 1in,' + '\n')
   fh.write('\ttop = 1in,' + '\n')
   fh.write('\tbottom = 1in,' + '\n')
   fh.write(r']{geometry}' + '\n')
   fh.write(r'\usepackage[canadian]{babel}' + '\n')
   fh.write(r'\usepackage{csquotes}' + '\n')
   fh.write(r'\usepackage{siunitx}' + '\n')
   fh.write(r'\sisetup{detect-all}' + '\n')
   fh.write(r'\usepackage{chemformula}' + '\n')
   fh.write(r'\usepackage[version=4]{mhchem}' + '\n')
   fh.write(r'\usepackage{unicode-math}' + '\n')
   fh.write(r'\defaultfontfeatures{Ligatures=TeX}' + '\n')
   fh.write(r'\setmainfont{STIX Two Text}' + '\n')
   fh.write(r'\setmathfont{STIX Two Math}' + '\n')
   fh.write(r'\usepackage[' + '\n')
   fh.write('\tstyle = style/phys,' + '\n')
   fh.write('\tarticletitle = true,' + '\n')
   fh.write('\tchaptertitle = true,' + '\n')
   fh.write('\tpageranges = true,' + '\n')
   fh.write('\tbiblabel = brackets,' + '\n')
   fh.write('\teprint = true,' + '\n')
   fh.write('\tdoi = false,' + '\n')
   fh.write('\tbackend = biber,' + '\n')
   fh.write('\tbackref = false,' + '\n')
   fh.write('\trefsection = section,' + '\n')
   fh.write(r']{biblatex}' + '\n')
   fh.write(r'\usepackage[' + '\n')
   fh.write('\tunicode,' + '\n')
   fh.write('\tcolorlinks = true,' + '\n')
   fh.write('\tallcolors = blue,' + '\n')
   fh.write(r']{hyperref}' + '\n')
   fh.write(r'\urlstyle{rm}' + '\n')
   fh.write(r'\usepackage{showkeys}' + '\n')
   fh.write(r'\renewcommand\showkeyslabelformat[1]{\fcolorbox{black}{yellow!50!white}{\tiny\texttt{#1}}}' + '\n')
   fh.write(r'\usepackage{luatexbase}' + '\n')
   fh.write(r'\usepackage{microtype}' + '\n')
   fh.write(r'\usepackage[titles]{tocloft}' + '\n')
   fh.write(r'\usepackage[chapter]{tocbibind}' + '\n')
   #fh.write(r'\renewcommand{\cftchapdotsep}{\cftdotsep}' + '\n')
   #fh.write(r'\renewcommand{\cftsecdotsep}{\cftdotsep}' + '\n')
   #fh.write(r'\usepackage{multicol}' + '\n')
   #fh.write(r'\renewcommand\cfttocprehook{\begin{multicols}{2}}' + '\n')
   #fh.write(r'\renewcommand\cfttocposthook{\end{multicols}}' + '\n')
   #
   # https://tex.stackexchange.com/a/266651
   #fh.write(r'\defbibheading{subbibliography}[\refname]{\section*{#1}}' + '\n')
   # https://github.com/lervag/vimtex/issues/1064
   #fh.write('\n')
   #fh.write(r'\addto\captionscanadian{\renewcommand{\contentsname}{Files}}' + '\n')
   fh.write('\n')
   fh.write(r'\usepackage{fancyhdr}' + '\n')
   fh.write(r'\fancypagestyle{plain}{%' + '\n')
   fh.write('\t' + r'\fancyhf{}' + '\n')
   #fh.write('\t' + r'\fancyhead[R]{\thechapter}' + '\n')
   fh.write('\t' + r'\fancyfoot[R]{\thepage}' + '\n')
   fh.write('\t' + r'\renewcommand{\footrulewidth}{0.5pt}' + '\n')
   fh.write('\t' + r'\renewcommand{\footrulewidth}{0.5pt}' + '\n')
   fh.write(r'}' + '\n')
   fh.write(r'\pagestyle{plain}' + '\n')
   fh.write('\n')
   fh.write(r'\title{List of \texttt{.bib} entries in \texttt{' + pwd + '/}}' + '\n')
   fh.write(r'\date{\textit{Last updated}: ' + t.strftime('%Y-%m-%d %H:%M:%S') + '}' + '\n')
   fh.write('\n')
   fh.write(r'\begin{document}' + '\n')
   fh.write('\n')
   fh.write(r'\maketitle' + '\n')
   fh.write('\n')
   fh.write(r'\begin{abstract}' + '\n')
   fh.write('\t' + r'This is a list of references found by a recursive \texttt{glob(**/*.bib)} within \texttt{' + pwd + '/}.' + '\n')
   fh.write('\t' + r'The entries are organized by individual \texttt{.bib} files within each subdirectory.' + '\n')
   fh.write('\t' + r'Citation keys for each citable entry are printed in the margin for convenience..' + '\n')
   fh.write('\t' + r'The \LaTeX\ source code for this document was generated automatically by the \texttt{python} script \texttt{gen\_ref\_list.py}.' + '\n')
   fh.write(r'\end{abstract}' + '\n')
   fh.write('\n')
   #fh.write(r'\begin{multicols}{2}' + '\n')
   fh.write(r'\tableofcontents' + '\n')
   #fh.write(r'\end{multicols}' + '\n')
   fh.write('\n')
   
   last_dir = ''
   
   for b in bib :
      # get the current directory
      current_dir = b.split('/')[0] + '/'
      
      if current_dir != last_dir:
         fh.write(r'\chapter*{' + current_dir + '}' + '\n')
         fh.write(r'\addcontentsline{toc}{chapter}{' + current_dir + '}' + '\n')
         fh.write('\n')
      last_dir = current_dir
      
      fh.write(r'\begin{refsection}[' + b + ']' + '\n')
      fh.write('\t' + r'\nocite{*}' + '\n')
      fh.write('\t' + r'\printbibliography[title = {' + b.replace(current_dir, '', 1) + '}, heading = subbibintoc]' + '\n')
      fh.write(r'\end{refsection}' + '\n')
      fh.write('\n')
   fh.write('\n')
   fh.write(r'\end{document}' + '\n')

