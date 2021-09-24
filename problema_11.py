n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[:5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
b=(a[::-1])
print(b)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(a)
c.sort(reverse=True)
print(c)
print('d)  afişează pe ecran doar componentele pare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        d.extend([y])
print(d)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(int(sum(d)/len(d)))
print('f)  afişează pe ecran doar componentele impare;')
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        f.extend([y])
print(f)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input('Dati valoarea lui x= '))
y=int(input('Dati valoarea lui y= '))
g=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]%y!=0)):
        z=a[i]
        g.extend([z])
print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x1=('Dati valoarea lui x= ')
y1=('Dati valoarea lui y= ')
h=[]
for i in range(0,len(a)):
    if ((a[i]>x) and (a[i]<y)):
        z1=a[i]
        h.extend([z1])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i in a:
    if i < 0 and i%2==1:
        print(a.index(i))
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;') 
for i in a:
    if (i>9 and i<100) or (i<-9 and i>-100) :
        print(a.index(i))
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a
x=min(k)
k.insert(0,x)
print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
l=a
l1=l.index(min(l))
l2=l[0]
l[l1]=l2
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
y2 = []
for i in a:
    if i%2==0:
        y2.append(i)
print(y2)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
y3 = []
for i in a:
    if i%3==0:
        y3.append(i)
print(y3)

