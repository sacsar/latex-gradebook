import csv, shlex, subprocess
from parse import *

#filename="grades.csv"
#name="Sebastian Csar"
#course="Math 1142"
#section="002"
#semester="Fall"
#year="2012"
gradelines=""
deffirsthwcol="HW1"
deffirstquizcol="Quiz1"

def setup():
    print "Enter the setup details.\n"
    filename = raw_input('Input file name: ')
    name = raw_input('Name: ')
    course = raw_input('Course: ')
    section = raw_input('Section number: ')
    semester = raw_input('Semester: ')
    year = raw_input('Year: ')
    firsthwcol = raw_input('%s' % deffirsthwcol)
    firstwhcol = firsthwcol or deffirsthwcol
    firstquizcol = raw_input('%s' %deffirstquizcol)
    firstquizcol = firstquizcol or deffristquizcol
    return (filename, name, course, section, semester, year, firsthwcol, firstquizcol)

def outputname(course,section,semester,year):
    coursenum = int(search('{:g}',course).fixed[0]) #this assumes only one number appears
    return str(coursenum)+'_'+str(section)+'_'+semester+year #note that there's no extension!

def writetable(filename,name,course,section,semester,year,gradelines,firsthwcol="HW1",firstquizcol="Quiz1"):
    header="\\documentclass[10pt]{article}\n \\usepackage[margin=.25in]{geometry}\n \\usepackage{longtable,rotating,fancyhdr,array,graphicx}\n \\renewcommand{\\tabcolsep}{2pt}\n \\begin{document}\n\\footnotesize"


    grades=csv.reader(open(filename,'rb'),delimiter='\t',quotechar='"')
    rows=[]
    for row in grades:
        rows.append(row)
    columns=[]
    for i in range(len(rows[0])):
        col=[]
        for row in rows:
            col.append(row[i])
        columns.append(col)
    tempfile = outputname(course,section,semester,year)+"temp.tex"
    f=open(tempfile,'w')
    f.write(header)
    f.write("\\begin{longtable}{|")
    for i in range(len(columns)):
        f.write("p{10pt}|")
    f.write("}\n \\hline\n")

    for col in columns:
        if col[0]==firsthwcol:
            f.write("\\pagebreak\n")
        if col[0]==firstquizcol:
            f.write("\\pagebreak\n")
        for i in reversed(range(len(col))):
            f.write("\\begin{turn}{-90}"+str(col[i])+"\ \ \\end{turn}")
            #if col[0]=="ID":
            #	f.write("\\\\n\\endhead")
            if i==0:
                f.write("\\\\\n \\hline\n")
                if col[0]=="ID":
                    f.write("\\endhead\n")
            else:
                f.write(" & ")
    f.write("\\end{longtable}\n\\end{document}")
    f.close()
    latexgrades="pdflatex "+tempfile
    args=shlex.split(latexgrades)
    p=subprocess.call(args)

def writebook(filename,name,course,section,semester,year,gradelines):
    bookfile = outputname(course,section,semester,year)+".tex"
    tempfile = outputname(course,section,semester,year)+"temp.tex"
    book="\\documentclass{article}\n\\usepackage[margin=1in,landscape]{geometry}\n\\usepackage{pdfpages,fancyhdr}\n\\pagestyle{fancy}\n \\renewcommand{\headrulewidth}{0pt}\n\\rhead{\\footnotesize "+str(name)+"\\\\"+str(course)+", Section "+str(section)+"\\\\"+str(semester)+" "+year+"}\n\\cfoot{}\n\\lfoot{"+gradelines+"}\n\n\\begin{document}\n\\includepdf[landscape,scale=.95,pagecommand=\\thispagestyle{fancy},pages=-]{"+tempfile+"}\n\\end{document}"
    f = open(bookfile, 'w')
    f.write( book )
    f.close()
    args.shlex.split("pdflatex "+bookfile)
    p = subprocess.call(args)

print "Done"
