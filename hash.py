import csv
alf = sorted('йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁё')
d = {alf[i]:i+1 for  i in range(66)}
print(d)
def hash(s):
    s= s.replace(' ','')
    p = 67
    m = 10**9+9
    has_value = 0
    i=0
    for c in s:
        has_value+=d[c]*p**i
        i+=1
    return has_value % m
with open('students.csv')as f, open('students_new_hash.csv','w') as nf:
    data = list(csv.reader(f,delimiter=';'))
    res = csv.writer(nf, delimiter=',')
    print(data[1])
    res.writerow(data[0])
    for s in data[1:]:
        s[0] = hash(s[1])
        res.writerow(s)
    print(*data,sep='\n')

