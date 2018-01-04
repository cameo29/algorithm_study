import sys

a = lambda: sys.stdin.readline()
rl = int(a())
result = []

i = 0
while i < rl :
    i = i+1
    list = []
    text = lambda: sys.stdin.readline()
    rl2 = text()
    leng = len(rl2)-1
    lenghalf = int(leng/2)
    j = 0
    while j<leng:
        list.append(rl2[j:j+2])
        j = j+2
    list.sort()
    string = ""
    listlen = len(list)
    for k in range(listlen):
        string = string + list.pop(0)     
    result.append(string)

for i in range(len(result)):
    print(result[i])
# efabcdgg
    #for i in range(0,)
    #rl.


'''list = ['ef','ab','cd','gg']
print(list)
list.sort()
print(list)'''