f_org = open("org_expansi_final.txt", "r") 
f_person = open("person_expansi_final.txt", "r") 
f_place = open("place_expansi_final.txt", "r") 
org = f_org.read().split("\n")
person = f_person.read().split("\n")
place = f_place.read().split("\n")
with open("20k_wiki.txt", 'r+') as f, open('20k_wiki_pelabelan 2_1.txt', 'w+') as outfile:
	lines = f.read().split("\n")
	i=0
	while i < len(lines):
		line = lines[i]
		a = True
		if lines[i].istitle():
			while a == True:
				if lines[i+1].istitle():
					line = line+" "+lines[i+1]
					i+=1
					a = True
				elif not(lines[i+1].istitle()) and lines[i+2].istitle():
					line = line+" "+lines[i+1]
					i+=1
					a = True
				else:
					break
		if (' . ' in line) or (' , ' in line):
			line2 = line.replace(' . ','.').replace(' , ',', ')
			if (line2 in org) and not (line2 in person) and not (line2 in place) and line2[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					if (name in ['.',',']):
						outfile.write(name+"	O"+"\n")
					else:
						outfile.write(name+"	Organisation"+"\n")
			elif (line2 in person) and not (line2 in org) and not (line2 in place) and line2[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					if (name in ['.',',']):
						outfile.write(name+"	O"+"\n")
					else:
						outfile.write(name+"	Person"+"\n")
			elif (line2 in place) and not (line2 in person) and not (line2 in org) and line2[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					if (name in ['.',',']):
						outfile.write(name+"	O"+"\n")
					else:
						outfile.write(name+"	Place"+"\n")
			else:
				fullname = line.split(" ")
				for name in fullname:
					if (name + "	O") != '	O':
						outfile.write(name + "	O" + "\n")
		else:
			if (line in org) and not (line in person) and not (line in place) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Organisation"+"\n")
			elif (line in person) and not (line in org) and not (line in place) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Person"+"\n")
			elif (line in place) and not (line in person) and not (line in org) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Place"+"\n")
			else:
				fullname = line.split(" ")
				for name in fullname:
					if (name + "	O") != '	O':
						outfile.write(name + "	O" + "\n")
		i+=1

with open("20k_wiki_pelabelan 2_1.txt", 'r+') as f, open('20k_wiki_pelabelan 2_2.txt', 'w+') as outfile:
    lines = f.read().split("\n")
    i=0
    while i < len(lines):
        line = lines[i]
        label = lines[i].split("	")
        a = True
        if not line.strip(): break
        elif (line[0].isupper()) and ("O" in label):
            while a == True:
                line2 = lines[i+1]
                label2= lines[i+1].split("	")
                line3 = lines[i+2]
                label3= lines[i+2].split("	")
                if line2[0].isupper() and ("O" in label2) and ((i+2) == ((len(lines)) - 2)) and (('.' in line3)):
                    line = line.replace("	O","")+" "+lines[i+1].replace("	O","")
                    i+=1
                    break
                elif line2[0].isupper() and ("O" in label2) and ((i+2) == ((len(lines)) - 1)):
                    line = line.replace("	O","")+" "+lines[i+1].replace("	O","")
                    i+=1
                    break
                elif line2[0].isupper() and ("O" in label2):
                    line = line.replace("	O","")+" "+lines[i+1].replace("	O","")
                    i+=1
                    a = True
                elif not(line2[0].isupper()) and line3[0].isupper() and ("O" in label2) and ("O" in label3) and not(('.' in line2) or (',' in line2)) and ((i+2) == ((len(lines)) - 1)):
                    line = line.replace("	O","")+" "+lines[i+1].replace("	O","")+" "+lines[i+2].replace("	O","")
                    i+=2
                    break
                elif not(line2[0].isupper()) and line3[0].isupper() and ("O" in label2) and ("O" in label3) and not(('.' in line2) or (',' in line2)):
                    line = line.replace("	O","")+" "+lines[i+1].replace("	O","")
                    i+=1
                    a = True
                else:
                    line = line.replace("	O","")
                    break
            if (line in org) and not (line in person) and not (line in place) and line[0].isupper():
                fullname = line.split(" ")
                for name in fullname:
                    outfile.write(name+"	Organisation"+"\n")
            elif (line in person) and not (line in org) and not (line in place) and line[0].isupper():
                fullname = line.split(" ")
                for name in fullname:
                    outfile.write(name+"	Person"+"\n")
            elif (line in place) and not (line in person) and not (line in org) and line[0].isupper():
                fullname = line.split(" ")
                for name in fullname:
                    outfile.write(name+"	Place"+"\n")
            else:
                fullname = line.split(" ")
                for name in fullname:
                    if (name + "	O") != '	O':
                        outfile.write(name + "	O" + "\n")
        else:
            if (line + "	O") != '	O':
                outfile.write(line+"\n")
        i+=1

with open("20k_wiki_pelabelan 2_2.txt", 'r+') as f, open('20k_wiki_pelabelan 2_3.txt', 'w+') as outfile:
	lines = f.read().split("\n")
	i=0
	while i < len(lines):
		line = lines[i]
		label = lines[i].split("	")
		a = True
		if not line.strip(): break
		elif (line[0].isupper()) and ("O" in label):
			while a == True:
				line2 = lines[i+1]
				label2= lines[i+1].split("	")
				if line2[0].isupper() and ("O" in label2):
					line = line.replace("	O","")+" "+lines[i+1].replace("	O","")
					i+=1
					a = True
				else:
					line = line.replace("	O","")
					break
			if (line in org) and not (line in person) and not (line in place) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Organisation"+"\n")
			elif (line in person) and not (line in org) and not (line in place) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Person"+"\n")
			elif (line in place) and not (line in person) and not (line in org) and line[0].isupper():
				fullname = line.split(" ")
				for name in fullname:
					outfile.write(name+"	Place"+"\n")
			else:
				fullname = line.split(" ")
				for name in fullname:
					if (name + "	O") != '	O':
						outfile.write(name + "	O" + "\n")
		else:
			if (line + "	O") != '	O':
				outfile.write(line + "\n")
		i+=1

with open("20k_wiki_pelabelan 2_3.txt", 'r+') as f, open('20k_wiki_gazz.txt', 'w+') as outfile:
	lines = f.read().split("\n")
	i=0
	while i < len(lines):
		line = lines[i]
		label = lines[i].split("	")
		a = True
		if not line.strip(): break
		if (line[0].isupper()) and ("O" in label):
			line = line.replace("	O","")
			if (line in org) and not (line in person) and not (line in place) and line[0].isupper():
				outfile.write(line+"	Organisation"+"\n")
			elif (line in person) and not (line in org) and not (line in place) and line[0].isupper():
				outfile.write(line+"	Person"+"\n")
			elif (line in place) and not (line in person) and not (line in org) and line[0].isupper():
				outfile.write(line+"	Place"+"\n")
			else:
				outfile.write(line+"	O"+"\n")
		else:
			outfile.write(line+"\n")
		i+=1
