latex-gradebook
===============

Python script to latex a gradebook in CSV format.

I find one of the most frustrating things about the end of the semester is printing one's gradebook. Inevitably, I manage to do something that makes the spreadsheet print not the way I wanted. Then it occurred to me that perhaps I could LaTeX the gradebook and the last thing on every semester's to do list would become painless. Of course, I first had to figure out how to do it.

This remains a work in progress and is currently fairly severely limited. It does, however, work on my current gradebooks, so perhaps it will work on yours. (Details of the limitations are below.) 

## What you need

- gradebook.py
- Python and LaTeX (obviously)
- Parse: https://pypi.python.org/pypi/parse
- longtable, rotating, pdfpages, fancyhdr, graphicx

## What to do/Notes

- The name and ID numbers of each student are repeated on each page, as is a header with the instructor name, course number, section number and semester. It assumes the first two columns of the gradebook are Name and ID (or vice versa).
- template.csv is a tab-delimited file that contains the header row of a gradebook
- Export your gradebook as a csv file. As written, gradebook.py has tab as the delimiter and " as the quote character for the csv.
- Run `python gradebook.py` from the directory where your csv files are.
- You'll be prompted for the name of your csv file, your name, the course, the section number, the semester and the year, as well as the name of the first homework column and first quiz column.
- Output: `CourseSectionSemesterYear_temp.tex` and `CourseSectionSemesterYear_temp.pdf`, which contain the table portion, and `CourseSectionSemesterYear.tex` and `CourseSectionSemesterYear.pdf`, which are the actual gradebook with the header.
- There are page breaks before the first homework column and the first quiz column.
- Depending on the table, longtable may require latex to be run a few times to get the table right. When I tested it on my gradebook, which isn't a complicated table, it only required one run. You may need to latex the temp file a few times manually before latexing the gradebook again.

## Limitations

The limitation most obvious to me (and it is a big one) is that I've used longtable to make a very wide table by rotating the cells. This has traded length for width--if you have a lot of students and your gradebook is two pages vertically, you'll just run off the page.

In the past, this has sometimes failed inexplicably, I think because it's highly reliant on the formatting of the csv. Hopefully using the template csv will alleviate this problem.

## To-Dos/Wishlist

- Add a final page to the the gradebook for the gradelines and any notes. Possible prompt for the gradelines.
- Figure out what to do about classes with a lot of students, i.e. when the table is too long.
- Make a proper example

    The idea of using pdfpages to help place the headers came from a helpful response I got on tex.stackexchange.com.
