import csv
with open('students.csv') as f, open('students_new.csv','a') as nf:
    data = list(csv.reader(f,delimiter=';'))
    print(*data,sep='\n')