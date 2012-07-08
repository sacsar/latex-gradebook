import csv, shlex, subprocess

file=".csv"
name=""
course="Math 1271"
section="11"
semester="Fall"
year="2010"
gradelines=""
firsthwcol="HW1"
firstquizcol="Q1"

header="\\documentclass[11pt]{article}\n \\usepackage[margin=.25in]{geometry}\n \\usepackage{longtable,rotating,fancyhdr,array,graphicx}\n \\renewcommand{\\tabcolsep}{2pt}\n \\begin{document}\n\\footnotesize"

book="\\documentclass{article}\n\\usepackage[margin=1in,landscape]{geometry}\n\\usepackage{pdfpages,fancyhdr}\n\\pagestyle{fancy}\n \\renewcommand{\headrulewidth}{0pt}\n\\rhead{\\footnotesize "+str(name)+"\\\\"+str(course)+", Section "+str(section)+"\\\\"+str(semester)+" "+year+"}\n\\cfoot{}\n\\lfoot{"+gradelines+"}\n\n\\begin{document}\n\\includepdf[landscape,scale=.95,pagecommand=\\thispagestyle{fancy},pages=-]{grades.pdf}\n\\end{document}"

grades=csv.reader(open(file,'rb'),delimiter='\t',quotechar='"')
rows=[]
for row in grades:
	rows.append(row)
columns=[]
for i in range(len(rows[0])):
	col=[]
	for row in rows:
		col.append(row[i])
	columns.append(col)

f=open('grades.tex','w')
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

latexgrades="pdflatex grades.tex"
args=shlex.split(latexgrades)
p=subprocess.call(args)

latexbook="pdflatex gradebook.tex"
f=open('gradebook.tex','w')
f.write(book)
f.close()
args=shlex.split(latexbook)
p=subprocess.call(args)
print "Done"
