#由于我刚学习python时间不长，所以方法可能有些笨
f1 = open("log.txt")
data = f1.read()
f1.close()
len1 = len(data)
N = list(range(ord('A'),ord('Z')))+list(range(ord('a'),ord('z')))
num = 0
for i in range(1,len1):        
    num += 1
    if data[i] in ['a', 'b', 'c', 'd', 'e']\
       and ord(data[i-1]) not in N\
       and ord(data[i+1]) not in N:
        if data[i] == 'a':
            dat = 'x(1)'
        elif data[i] == 'b':
            dat = 'x(2)'
        elif data[i] == 'c':
            dat = 'x(3)'
        elif data[i] == 'd':
            dat = 'x(4)'
        elif data[i] == 'e':
            dat = 'x(5)'
        else:
            dat = data[i]
    else:
        dat = data[i]
    print("\r第{:5}个，{:2.2f}%".format(num,num/len1*100),end='')
            
    with open('lognew.txt','a') as f2:
        f2.write(dat)
        f2.close()
        
