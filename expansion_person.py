from nltk.corpus import words
import re
desk = ["Masyarakat","the","The","SD","TK","Universitas","Band","band","Music","music","grup","Grup","Group","group","company","Company",'(grup','musik)', '(Grup', 'Musik)', '(grup)', '(Grup)', '(band)','(Band)', 'SMA','SMP','Pemilihan']
tandabaca =["~","!","@","%","*","+","/",":"]
source = open('person.txt')
clean = open('person_clean.txt', 'w+')
cek_clean = open('person_clean_x.txt', 'w+')
cek_clean.write('Berhasil melakukan cleaning entitas person pada kategori	:'+'\n')
org = open('add_organization.txt', 'w+')
org_digit = open('A11-1_x.txt', 'w+')
org_kamus = open('A11-2.txt', 'w+')
kbbi = open("kbbi.txt")
kamus = kbbi.read().split("\n")
for line in source:
		nama = line.split()
		jumlah = len(nama)
		count = 0
		for n in nama:
			#n = n.decode('utf-8')
			n = unicode(n, errors='ignore')
			if ((n.lower() in words.words()) or (n.lower() in kamus)):
				count =  count + 1
		if (count == jumlah):
			cek_clean.write('A11-2	:' + line)
			org_kamus.write(line)
			org.write(line)
		elif any(d in nama for d in desk) or any(tanda in line for tanda in tandabaca):
			if any(d in nama for d in ["the", "The"]):
				cek_clean.write('A11-3	:' + line)
			if any(d in nama for d in ["Masyarakat","Band","band","Music","music","grup","Grup","Group","group","company","Company",'Pemilihan']):
				cek_clean.write('A11-7	:' + line)
			if any(d in nama for d in ["SD","TK","Universitas", 'SMA', 'SMP']):
				cek_clean.write('A11-5	:' + line)
			if any(d in nama for d in ['(grup','musik)', '(Grup', 'Musik)', '(grup)', '(Grup)', '(band)','(Band)']):
				cek_clean.write('A10	:' + line)
			if any(d in line for d in ["~","!","@","%","*","+","/",":"]):
				cek_clean.write('A15	:' + line)
			org.write(line)
		elif any(n.isdigit() for n in nama) or any(any(letter.isdigit() for letter in n) for n in nama):
			cek_clean.write('A11-1	:' + line)
			org_digit.write(line)
		else:
			clean.write(line)
org_digit.close()
cek_clean.close()
clean.close()
org.close()
file = open("A11-1_x.txt", "r")
normal = open("organisasi_digit_n.txt", "w+")
f = file.readlines()
for line in f:
	if ("ke-" in line):
		normal.write(re.sub(r' \((.*)\)', '', line.split(' ke-', 1)[0]) + "\n")
	else:
		normal.write(re.sub(r' \((.*)\)', '', line))
file.close()
normal.close()
with open('organisasi_digit_n.txt') as infile, open('A11-1.txt', 'w+') as outfile:
	for line in infile:
		nama = line.split()
		if any(n.isdigit() for n in nama) or any(any(letter.isdigit() for letter in n) for n in nama):
			outfile.write(line)
with open('organisasi_digit_n.txt') as infile, open('person_clean.txt', 'a') as outfile:
	for line in infile:
		nama = line.split()
		if not (any(n.isdigit() for n in nama) or any(any(letter.isdigit() for letter in n) for n in nama)):
			outfile.write(line)
with open('person_clean_x.txt') as infile, open('person_clean_report.txt', 'w+') as outfile:
	for line in infile:
		if not ('A11-1' in line):
			outfile.write(line)
with open('A11-1.txt') as infile, open('person_clean_report.txt', 'a') as outfile:
	for line in infile:
		outfile.write('A11-1	:' + line)
with open('A11-1.txt') as infile, open('add_organization.txt', 'a') as outfile:
	for line in infile:
		outfile.write(line)

file = open("person_clean.txt", "r")
normal = open( "person_normalize.txt", "w+")
cek_normalize = open('person_normalize_report.txt', 'w+')
cek_normalize.write('Berhasil melakukan normalize entitas person pada kategori	:'+'\n')
f = file.readlines()
for line in f:
	if '(' in line:
		cek_normalize.write("A9	:" + line)
		line = line.split('(', 1)[0]
		cek_normalize.write("A9 normalize:" + line + "\n")
		normal.write(line + "\n")
	else:
		normal.write(line)
file.close()
normal.close()

file = open("person_normalize.txt", "r")
normal = open( "personnormalize.txt", "w+")
simpan = open("save_normalize.txt","w+")
for line in file:
	words = line.split()
	if ('of' in words):
		cek_normalize.write("A6	:" + line)
		line = line.split(' of ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('from' in words):
		cek_normalize.write("A6	:" + line)
		line = line.split(' from ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('dari' in words):
		cek_normalize.write("A6	:" + line)
		line = line.split(' dari ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('di' in words):
		cek_normalize.write("A6	:" + line)
		line = line.split(' di ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('at' in words):
		cek_normalize.write("A6	:" + line)
		line = line.split(' at ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('dan' in words):
		cek_normalize.write("A11-4	:" + line)
		pisah = line.split(' dan ')
		for nama in pisah:
			cek_normalize.write("A11-4 normalize:" + nama + "\n")
			normal.write(nama + "\n")
	elif ('and' in words):
		cek_normalize.write("A11-4	:" + line)
		pisah = line.split(' and ')
		for nama in pisah:
			cek_normalize.write("A11-4 normalize:" + nama + "\n")
			normal.write(nama + "\n")
	elif ('&' in words):
		cek_normalize.write("A11-4	:" + line)
		pisah = line.split(' & ')
		for nama in pisah:
			cek_normalize.write("A11-4 normalize:" + nama + "\n")
			normal.write(nama + "\n")
	elif ('bin' in words):
		simpan.write(line)
		cek_normalize.write("A5	:" + line)
		cek_normalize.write("A5 normalize:" + line + "\n")
		pisah = line.split(' bin ')
		for nama in pisah:
			cek_normalize.write("A5 normalize:" + nama + "\n")
			normal.write(nama + "\n")
	elif ('binti' in words):
		simpan.write(line)
		cek_normalize.write("A5	:" + line)
		cek_normalize.write("A5 normalize:" + line + "\n")
		pisah = line.split(' binti ')
		for nama in pisah:
			cek_normalize.write("A5 normalize:" + nama + "\n")
			normal.write(nama + "\n")
	elif ('dos' in words):
		simpan.write(line)
		cek_normalize.write("A7	:" + line)
		cek_normalize.write("A7 normalize:" + line + "\n")
		line = line.split(' dos ', 1)[0]
		cek_normalize.write("A7 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('de' in words):
		simpan.write(line)
		cek_normalize.write("A7	:" + line)
		cek_normalize.write("A7 normalize:" + line + "\n")
		line = line.split(' de ', 1)[0]
		cek_normalize.write("A7 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('der' in words):
		simpan.write(line)
		cek_normalize.write("A7	:" + line)
		cek_normalize.write("A7 normalize:" + line + "\n")
		line = line.split(' der ', 1)[0]
		cek_normalize.write("A7 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('van' in words):
		simpan.write(line)
		cek_normalize.write("A6	:" + line)
		cek_normalize.write("A6 normalize	:" + line)
		line = line.split(' van ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	elif ('von' in words):
		simpan.write(line)
		cek_normalize.write("A6	:" + line)
		cek_normalize.write("A6 normalize	:" + line)
		line = line.split(' von ', 1)[0]
		cek_normalize.write("A6 normalize:" + line + "\n")
		normal.write(line + "\n")
	else:
		normal.write(line)
normal.close()
file.close()
simpan.close()
with open('personnormalize.txt') as infile, open('person_normalize2.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output

file = open("person_normalize2.txt", "r")
normal = open( "personnormalize2.txt", "w+")
f = file.readlines()
for line in f:
	if (',' in line):
		words = line.split(', ')
		if len(words) > 2:
			cek_normalize.write("A11-6	:" + line)
			for nama in words:
				cek_normalize.write("A11-6 normalize:" + nama + "\n")
				normal.write(nama+"\n")
		else:
			if (", Sr." in line) or (", Jr." in line):
				cek_normalize.write("A8	:" + line)
				cek_normalize.write("A8 normalize:" + line.replace(',', '') + "\n")
				normal.write(line.replace(',', ''))
				line = line.split(',', 1)[0]
				cek_normalize.write("A8 normalize:" + line + "\n")
				normal.write(line+"\n")
			else:
				cek_normalize.write("A8	:" + line)
				line = line.split(',', 1)[0]
				cek_normalize.write("A8 normalize:" + line + "\n")
				normal.write(line+"\n")
	elif ('-' in line):
		cek_normalize.write("A12	:" + line)
		cek_normalize.write("A12 normalize:" + line + "\n")
		pisah = line.split('-')
		for nama in pisah:
			cek_normalize.write("A12 normalize:" + nama + "\n")
			normal.write(nama+"\n")
		normal.write(line)
	elif 'j' in line and not (ejaan in line for ejaan in ['dj','tj']) and 'oe' in line and 'ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('j','y')
		line = line.replace('oe','u')
		line = line.replace('ch','kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'j' in line and not (ejaan in line for ejaan in ['dj','tj']) and 'oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('j','y')
		line = line.replace('oe','u')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'j' in line and not (ejaan in line for ejaan in ['dj','tj']):
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('j','y')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'dj' in line and 'tj' in line and 'oe' in line and 'ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('dj','j')
		line = line.replace('tj','c')
		line = line.replace('oe','u')
		line = line.replace('ch','kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'dj' in line and 'tj' in line and 'oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('dj','j')
		line = line.replace('tj','c')
		line = line.replace('oe','u')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'dj' in line and 'tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('dj','j')
		line = line.replace('tj','c')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'dj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('dj','j')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'oe' in line and 'tj' in line and 'ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('oe','u')
		line = line.replace('tj','c')
		line = line.replace('ch','kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'oe' in line and 'tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('oe','u')
		line = line.replace('tj','c')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('oe','u')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'tj' in line and 'ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('tj','c')
		line = line.replace('ch','kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('tj','c')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line.replace('ch','kh'))
		cek_normalize.write("A14 normalize:" + line.replace('ch','kh') + "\n")
		normal.write(line)
	else:
		normal.write(line)
normal.close()
file.close()
with open('personnormalize2.txt') as infile, open('person_normalize3.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output

file = open("person_normalize3.txt", "r")
normal = open( "personnormalize3.txt", "w+")
f = file.readlines()
for line in f:
	if 'J' in line and not (ejaan in line for ejaan in ['Dj','Tj']) and 'Oe' in line and 'Ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('J','Y')
		line = line.replace('Oe','U')
		line = line.replace('Ch','Kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'J' in line and not (ejaan in line for ejaan in ['Dj','Tj']) and 'Oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('J','Y')
		line = line.replace('Oe','U')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'J' in line and not (ejaan in line for ejaan in ['Dj','Tj']):
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('J','Y')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Dj' in line and 'Tj' in line and 'Oe' in line and 'Ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Dj','J')
		line = line.replace('Tj','C')
		line = line.replace('Oe','U')
		line = line.replace('Ch','Kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Dj' in line and 'Tj' in line and 'Oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Dj','J')
		line = line.replace('Tj','C')
		line = line.replace('Oe','U')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Dj' in line and 'Tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Dj','J')
		line = line.replace('Tj','C')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Dj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Dj','J')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Oe' in line and 'Tj' in line and 'Ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Oe','U')
		line = line.replace('Tj','C')
		line = line.replace('Ch','Kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Oe' in line and 'Tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Oe','U')
		line = line.replace('Tj','C')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Oe' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Oe','U')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Tj' in line and 'Ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Tj','C')
		line = line.replace('Ch','Kh')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Tj' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
		line = line.replace('Tj','C')
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line)
	elif 'Ch' in line:
		cek_normalize.write("A14	:" + line)
		cek_normalize.write("A14 normalize:" + line + "\n")
		normal.write(line.replace('Ch','Kh'))
		cek_normalize.write("A14 normalize:" + line.replace('Ch','Kh') + "\n")
		normal.write(line)
	else:
		normal.write(line)
normal.close()
file.close()
with open('personnormalize3.txt') as infile, open('person_normalize4.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output

file = open("person_normalize4.txt", "r")
normal = open( "personnormalize4.txt", "w+")
f = file.readlines()
for line in f:
	words = line.split()
	if ('Dr.' in words):
		cek_normalize.write("A13	:" + line)
		normal.write(line.replace('Dr. ', ''))
		cek_normalize.write("A13 normalize:" + line.replace('Dr. ', '') + "\n")
	else:
		if not (line.startswith('.')):
			normal.write(line)
normal.close()
file.close()
with open('personnormalize4.txt') as infile, open('person_normalize5.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output

filename = open("person_normalize5.txt")
newfile = open( "personnormalize5.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('personnormalize5.txt') as infile, open('person_normalize_final.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip().rstrip()+"\n")  # non-empty line. Write it to output

def ngrams(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output
file = open("person_normalize_final.txt", "r")
expansi = open( "person_expansi.txt", "w+")
cek_expansi = open('person_expansi_report.txt', 'w+')
cek_expansi.write('Berhasil melakukan expansi entitas person:'+'\n')
f = file.readlines()
for line in f:
    cek_expansi.write("Nama	:" + line)
    jumlah = len(line.split())
    for x in range(1,jumlah+1):
        expan = ngrams(line, x)
        for name in expan:
            str1 = ' '.join(name)
            cek_expansi.write("Nama expansion:" + str1.lstrip() + "\n")
            expansi.write(str1.lstrip()+"\n")

file.close()
expansi.close()
with open('person_expansi.txt') as infile, open('person_expansi2.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

filename = open("person_expansi2.txt")
newfile = open( "person_expansi3.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('person_expansi3.txt') as infile, open('person_expansi4.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip())  # non-empty line. Write it to output

from nltk.corpus import words
import re
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember","January","February","March","April","May","June","July","August","September","October","November","December"]
agama =["Christianity", "Islam", "Hinduism", "Buddhism","Judaism","Kristen","Hindu","Buddha","Katolik","Yahudi"]
def cekroman(word):
	roman_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
	validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
	letter = list(word)
	if (re.search(roman_pattern, word.strip(), re.I)) and (l in validRomanNumerals for l in letter) and word.isupper():
		return (True)
	else:
		return (False)

file = open("person_expansi4.txt", "r")
expansi = open( "person_expansi_final.txt", "w+")
cek_validation = open('person_validation_report.txt', 'w+')
cek_validation.write('Berhasil melakukan validasi entitas person dengan menghapus:'+'\n')
kbbi = open("kbbi.txt")
kamus = kbbi.read().split("\n")
f = file.readlines()
for line in f:
	kata = line.split()
	jumlah = len(kata)
	if jumlah == 1:
		for k in kata:
			#k = k.decode('utf-8')
			k = unicode(k, errors='ignore')
			if not (('.' in k) or (k.isupper()) or (len(k) == 1) or (cekroman(k) is True) or (k.lower() in words.words()) or (k.lower() in kamus) or (k in bulan) or (k in agama)):
				expansi.write(line)
			else:
				cek_validation.write(line)
	else:
		expansi.write(line)
file.close()
expansi.close()
with open('save_normalize.txt') as infile, open('person_expansi_final.txt', 'a') as outfile:
	outfile.write("\n")
	for line in infile:
		outfile.write(line)