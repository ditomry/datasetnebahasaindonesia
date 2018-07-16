bad_words = ['(angkutan', 'Daftar', 'Persemakmuran']
cek_clean = open('place_clean_report.txt', 'w+')
cek_clean.write('Berhasil melakukan cleaning entitas place pada kategori	:'+'\n')
with open('place.txt') as oldfile, open('place_clean.txt', 'w+') as newfile:
    for line in oldfile:
		words = line.split()
		if not any(bad_word in words for bad_word in bad_words):
			newfile.write(line)
		elif any(bad_word in words for bad_word in ['Daftar', 'Persemakmuran']):
			cek_clean.write('B5	:' + line)
		elif ('(angkutan' in words):
			cek_clean.write('B6	:' + line)
import re
file = open("place_clean.txt", "r")
normal = open( "place_normalize.txt", "w+")
cek_normalize = open('place_normalize_report.txt', 'w+')
cek_normalize.write('Berhasil melakukan normalize entitas place pada kategori	:'+'\n')
f = file.readlines()
for line in f:
	if ("Desa" in line):
		cek_normalize.write('B3	:' + line)
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '', line))
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '',  line.replace("Desa ","")))
		normal.write(re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '',  line.replace("Desa ","\n")))
	elif ("Kota" in line):
		cek_normalize.write('B3	:' + line)
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '', line))
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '',  line.replace("Kota ","")))
		normal.write(re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '',  line.replace("Kota ","\n")))
	elif ("Kecamatan" in line):
		cek_normalize.write('B3	:' + line)
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '', line))
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '',  line.replace("Kecamatan ","")))
		normal.write(re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '',  line.replace("Kecamatan ","\n")))
	elif ("Kabupaten" in line):
		cek_normalize.write('B3	:' + line)
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '', line))
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '',  line.replace("Kabupaten ","")))
		normal.write(re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '',  line.replace("Kabupaten ","\n")))
	elif ("Provinsi" in line):
		cek_normalize.write('B3	:' + line)
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '', line))
		cek_normalize.write('B3 normalize:' + re.sub(r' \((.*)\)', '',  line.replace("Provinsi ","")))
		normal.write(re.sub(r' \((.*)\)', '',  line))
		normal.write(re.sub(r' \((.*)\)', '',  line.replace("Provinsi ","\n")))
	else:
		if ('(' in line):
			cek_normalize.write('B2	:' + line)
			cek_normalize.write('B2 normalize:' + re.sub(r' \((.*)\)', '',  line))
			normal.write(re.sub(r' \((.*)\)', '', line))
		else:
			normal.write(re.sub(r' \((.*)\)', '',  line))
normal.close()

with open('place_normalize.txt') as infile, open('place_normalize2.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip():
            continue  # skip the empty line
        elif ("/" in line):
            cek_normalize.write("B7	:" + line)
            words = line.split()
            for w in words:
                if ("/" in w):
                    tempat = w.split("/")
                    for x in tempat:
                        if ("," in x):
                            cek_normalize.write("B7	normalize:"+line.replace(w, x))
                            outfile.write(line.replace(w, x))
                        else:
                            cek_normalize.write("B7	normalize:" + line.replace(w, x + ","))
                            outfile.write(line.replace(w, x + ","))
            cek_normalize.write("B7	normalize:"+line)
            outfile.write(line)
        else:
            outfile.write(line)  # non-empty line. Write it to output

filename = open("place_normalize2.txt")
newfile = open( "place_normalize3.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('place_normalize3.txt') as infile, open('place_normalize_final.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line.lstrip().replace("  "," ").replace('%22','').rstrip()+"\n")  # non-empty line. Write it to output

def ngrams(input, n):
    input = input.split(',')
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

file = open("place_normalize_final.txt", "r")
expansi = open("place_expansi.txt", "w+")
cek_expansi = open('place_expansi_report.txt', 'w+')
cek_expansi.write('Berhasil melakukan expansi entitas place pada kategori:'+'\n')
f = file.readlines()
for line in f:
    jumlah = len(line.split())
    cek_expansi.write("Nama	:" + line)
    for x in range(1, jumlah + 1):
        expan = ngrams(line, x)
        for name in expan:
            str1 = ','.join(name)
            cek_expansi.write("Nama	expansion:" + str1.lstrip() + "\n")
            expansi.write(str1.lstrip(',') + "\n")
file.close()
expansi.close()

filename = open("place_expansi.txt")
newfile = open("place_expansi2.txt", "w+")
li = list(filename)
st = " ".join(li)
se = set(st.split("\n"))
result = "\n".join(sorted(se))
newfile.write(result)
newfile.close()
with open('place_expansi2.txt') as infile, open('place_expansi3.txt', 'w+') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        line = line.rstrip()
        if line.endswith(','):
            line = replace_last(line, ",", "")
        outfile.write(line.lstrip().replace("  ", " ") + "\n")  # non-empty line. Write it to output

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
file = open("place_expansi3.txt", "r")
expansi = open( "place_expansi_final.txt", "w+")
cek_validation = open('place_validation_report.txt', 'w+')
cek_validation.write('Berhasil melakukan validasi entitas place dengan menghapus:'+'\n')
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
			if not (('.' in k) or (k.isupper()) or (len(k) == 1)  or (cekroman(k) is True) or (k.lower() in words.words()) or (k.lower() in kamus) or (k in bulan) or (k in agama)):
				expansi.write(line)
			else:
				cek_validation.write(line)
	else:
		expansi.write(line)