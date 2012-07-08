latex-gradebook
===============

Python script to latex a gradebook in CSV format.

Copied from http://math.umn.edu/~csar/gradebook.shtml
I find one of the most frustrating things about the end of the semester is printing one's gradebook. Inevitably, I manage to do something that makes the spreadsheet print not the way I wanted. Then it occurred to me that perhaps I could LaTeX the gradebook and the last thing on every semester's to do list would become painless. Of course, I first had to figure out how to do it.

This remains a work in progress and is currently fairly severely limited. It does, however, work on my current gradebooks, so perhaps it will work on yours. (Details of the limitations are below.) 

## What you need

- gradebook.py
- Python and LaTeX (obviously)
- longtable, rotating, pdfpages, fancyhdr, graphicx

## What to do/Notes

- The name and ID numbers of each student are repeated on each page, as is a header with the instructor name, course number, section number and semester. It assumes the first two columns of the gradebook are Name and ID, respectively.
- Export your gradebook as a csv file. As written, gradebook.py has tab as the delimiter and " as the quote character for the csv.
- Change the values of file, name, course, section, semester, year and gradelines in gradebook.py to what's appropriate. The new requirements want pagebreaks before homework and quizzes. Set the header for your first homework column and quiz column in firsthwcol and firstquizcol, respectively.
- With gradebook.py and your csv file in the same directory, run python gradebook.py.
- gradebook.py creates two tex files: grades.tex and gradebook.tex. gradebook.pdf will be the gradebook proper--grades.tex just contains the table.
- Depending on the table, longtable may require latex to be run a few times to get the table right. When I tested it on my gradebook, which isn't a complicated table, it only required one run. If things look funky, run pdflatex on grades.tex a few times (check the PDF) then recompile gradebook.tex

## Limitations

The limitation most obvious to me (and it is a big one) is that I've used longtable to make a very wide table by rotating the cells. This has traded length for width--if you have a lot of students and your gradebook is two pages vertically, you'll just run off the page.

This script has sometimes failed for me and my officemate inexplicably. I've assumed it has something to do with it being highly reliant on the CSV looking a precise way, but, of course, one only encounters this problem the day grades are due, so it hasn't gotten fixed.

## To-Dos/Wishlist

- Add a final page to gradebook.tex for the gradelines and any notes. Possibly have variables in gradebook.py to write the gradelines automatically.
- Re-write things to prompt for the file name and header information, rather than having to edit the variables.
- Figure out what to do about classes with a lot of students, i.e. when the table is too long.
- Have the output filenames depend on the input file name to make it more natural.
- Make an example. I've only used my actual gradebooks so far.

    The idea of using pdfpages to help place the headers came from a helpful response I got on tex.stackexchange.com.
