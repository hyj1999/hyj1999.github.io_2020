import re

f = open('Original.txt', 'r', encoding = 'UTF-8')
jdlist = []
n = 0
with open('OutFile.txt', 'w', encoding = 'UTF-8') as fo:
                fo.write('@[toc](目录)')
                
for i in range(9310,9335):
    jdlist.append(chr(i))

for eachline in f.readlines():
    match = re.search(r'[^ \n]', eachline)
    if isinstance(match, re.Match):
        if eachline[2] in jdlist:
            n = 0
            outstr = '### ' + eachline[2:-3]
            with open('OutFile.txt', 'a', encoding = 'UTF-8') as fo:
                fo.write('\n'+outstr+'\n'+'||||\n|--|--|--|\n')
        elif eachline[0]=='*':
            n = 0
            with open('OutFile.txt', 'a', encoding = 'UTF-8') as fo:
                fo.write('\n'+eachline+'\n'+'||||\n|--|--|--|\n')
        else:
            n += 1
            if n in range(1,3):
                with open('OutFile.txt', 'a', encoding = 'UTF-8') as fo:
                    fo.write('|'+eachline[0:-1])
            else:
                n = 0
                with open('OutFile.txt', 'a', encoding = 'UTF-8') as fo:
                    fo.write('|'+eachline[0:-1]+'|\n')
            
            
