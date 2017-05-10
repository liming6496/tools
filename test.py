m = {}
f = open("config.property" ,"r")
for line in f.readlines():
    str = line.replace('\n','').split(":")
    m[str[0]] = str[1]
print(m)