#Exercise 9.8

#mengkonversi list ke dalam array.array
li = [10,20,30,40,50]
import array
C = array.array('i')
C.fromlist(li)
type(C)

for nilai in C:
    print("%d " % nilai, end='')
