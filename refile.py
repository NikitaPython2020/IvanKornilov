import re
pattern = '.*/[0-9]{8}'
prog = re.compile(pattern)
stats = {}
with open('C:/users/user/Desktop/Нетология/01. Подготовка/DZ1/urls.txt','r') as f:
    for line in f:
        line= line.strip()
        if prog.match(line):
            endLine = line.find('/',1)
            newLine = line[1:endLine]
            stats.setdefault(newLine, 0)
            stats[newLine] += 1
print(sorted(stats.items(), key=lambda item: item[1], reverse=True))
