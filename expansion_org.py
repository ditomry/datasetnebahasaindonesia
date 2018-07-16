import re
file = open("org.txt", "r")
normal = open( "org_normalize.txt", "w+")
cek_normalize = open('org_normalize_report.txt', 'w+')
cek_normalize.write('Berhasil melakukan normalize entitas organization pada kategori	:'+'\n')
for line in file:
	if ('(' in line):
		cek_normalize.write('C5	:' + line)
		cek_normalize.write('C5 normalize:' + re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '', line))
	else:
		normal.write(re.sub(r' \((.*)\)', '',  line))
normal.close()

filename = open("org_normalize.txt")
newfile = open( "org_normalize2.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('org_normalize2.txt') as infile, open('org_normalize_final.txt', 'w+') as outfile:
    for line in infile:
		if not line.strip(): continue  # skip the empty line
		outfile.write(line.lstrip().replace('%22','').replace('%3','').replace('%60','').replace('  ',' ').rstrip()+'\n')  # non-empty line. Write it to output

import re
file = open("org_normalize_final.txt", "r")
expan = open( "org_expansi.txt", "w+")
cek_expansi = open('org_expansi_report.txt', 'w+')
cek_expansi.write('Berhasil melakukan expansi entitas organization pada kategori:'+'\n')
for line in file:
	words = line.split()
	if ('di' in words):
		cek_expansi.write("C4	:" + line)
		expan.write(line.replace(' di ',' '))
		cek_expansi.write("C4 expansion:" + line.replace(' di ',' '))
		line = line.split(' di ', 1)[0]
		cek_expansi.write("C4 expansion:" + line+"\n")
		expan.write(line+"\n")
	elif ("," in line):
		cek_expansi.write("C3	:" + line)
		expan.write(line.replace(',', ''))
		cek_expansi.write("C3 expansion:" + line.replace(',', ''))
		line = line.split(',', 1)[0]
		cek_expansi.write("C3 expansion:" + line + "\n")
		expan.write(line+"\n")
	elif ("Partai" in words):
		cek_expansi.write("C6	:" + line)
		expan.write(line)
		cek_expansi.write("C6 expansion:" + line)
		cek_expansi.write("C6 expansion:" + line.replace('Partai ', ''))
		expan.write(line.replace('Partai ', '\n'))
	else:
		expan.write(line)
expan.close()
filename = open("org_expansi.txt")
newfile = open( "org_expansi2.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('org_expansi2.txt') as infile, open('org_expansi3.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip().replace("   "," ").replace("  "," ").rstrip()+"\n")  # non-empty line. Write it to output

from nltk.corpus import words
import re

def cekroman(word):
	roman_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
	validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
	letter = list(word)
	if (re.search(roman_pattern, word.strip(), re.I)) and (l in validRomanNumerals for l in letter) and word.isupper():
		return (True)
	else:
		return (False)

bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember","January","February","March","April","May","June","July","August","September","October","November","December"]
agama =["Christianity", "Islam", "Hinduism", "Buddhism","Judaism","Kristen","Hindu","Buddha","Katolik","Yahudi"]
file = open("org_expansi3.txt", "r")
expansi = open( "org_expansi4.txt", "w+")
cek_validation = open('org_validation_report.txt', 'w+')
cek_validation.write('Berhasil melakukan validasi entitas organization dengan menghapus:'+'\n')
kbbi = open("kbbi.txt")
kamus = kbbi.read().split("\n")
f = file.readlines()
for line in f:
	kata = line.split()
	jumlah = len(line.split())
	if jumlah == 1:
		for k in kata:
			#k = k.decode('utf-8')
			k = unicode(k,errors='ignore')
			if not ((len(k) == 1) or ('.' in k) or (cekroman(k) is True) or (k.lower() in words.words()) or (k.lower() in kamus) or (k in bulan) or (k in agama)):
				expansi.write(line)
			else:
				cek_validation.write(line)
	else:
		expansi.write(line)
expansi.close()
filename = open("org_expansi4.txt")
expansi = open( "org_expansi5.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
expansi.write(result)
expansi.close()
with open('org_expansi5.txt') as infile, open('org_expansi_final.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output