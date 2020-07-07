# #1.soru:
b=int(input("1-31 arası bir gün giriniz:"))
if (1<=b<=31):
    print(b,". gün")
else:
    print("yanlış gün seçimi! hata yaptın düzelt")

e = int(input("1-12 arası bir ay giriniz:"))
if(1<=e<=12):
    print(e,". ay")
else:
    print("yanlış ay seçimi! hata yaptın düzelt")

y=int(input("lütfen 4 basamaklı bir yıl giriniz:"))
if(1000<=y<=9999):
    print(y,". yıl")

else:
    print("yanlış yıl seçimi! hata yaptın düzelt")


z = {1: "ocak", 2: "şubat", 3: "mart", 4: "nisan", 5: "mayıs", 6: "haziran",
        7: "temmuz", 8: "ağustos", 9: "eylül",10:"ekim", 11:"kasım", 12:"aralık"}
a=str(e)

if (0<e<=9):
    print("girilen tarih :",b,z[int(a[0])],y)
else:
    print("girilen tarih :",b,z[int(a[0]+a[1])],y)


print()

# #2. soru:
b=int(input("lütfen b sayısı giriniz:"))
if(b<0):
    print("sayı negatif olamaz, lütfen daha dikkatli olun.!!")
if(b>16):
    print("sayı 16'dan büyük olamaz, lütfen daha dikkatli olun.!!")
if (9>b>=0):
    e =1
    for y in range(b):
        e=e*(y+1)
        z=(e*3)
    print(z,"=",b,"sayısının faktöriyeli ile 3 ün çarpımıdır.")
if( 9<=b<16):
    z=2
    for y in range(b):
        z=b*(b+1)
    print(z,"= 2 den başlayıp",b,"sayısının 2 ile çarpımına kadarki sayıların toplamıdır.")
print()

# #  3. soru:
# 1 yöntem: hocam for yazdım ama toplamını yapamadım.
a=[[1,2,-1 ],
   [2 ,5 ,2],
   [-1 ,-2 ,2]]

B=[["b","e","y"],
   ["z","a","t"],
   ["u","z","c"],
   ["u","x","x"]]

e=[[2,5,25],
   [26,1,20],
   [21,26,3],
   [21,24,24]]

Y ={"b":2,"e":5,"y":25,"z":26,"a":1,"t":20,"c":3,"u":21,"x":24}

print("A")
for a in [a]:
    for b in a:
        print(b, end=" ")
        print()
print()
print("E")
for a in [e]:
    for b in a:
         print(b, end=" ")
         print()
print()
print("A*E")

for x in a:
    for i in x:
        top=0
        for y in e:
            for j in y:
                top=top+(i*j)
                print(top,i*j,end=' ')
            print()
        print()

# 3. soru 2. yöntem
A=[[1,2,-1 ],
   [2 ,5 ,2],
   [-1 ,-2 ,2]]

E=[[2,5,25],
   [26,1,20],
   [21,26,3],
   [21,24,24]]

sifre=[A[0][0]*E[0][0]+A[1][0]*E[0][1]+A[2][0]*E[0][2],
       A[0][1]*E[0][0]+A[1][1]*E[0][1]+A[2][1]*E[0][2],
       A[0][2]*E[0][0]+A[1][2]*E[0][1]+A[2][2]*E[0][2]],\
      \
      [A[0][0]*E[1][0]+A[1][0]*E[1][1]+A[2][0]*E[1][2],
       A[0][1]*E[1][0]+A[1][1]*E[1][1]+A[2][1]*E[1][2],
       A[0][2]*E[1][0]+A[1][2]*E[1][1]+A[2][2]*E[1][2]],\
      \
      [A[0][0]*E[2][0]+A[1][0]*E[2][1]+A[2][0]*E[2][2],
       A[0][1]*E[2][0]+A[1][1]*E[2][1]+A[2][1]*E[2][2],
       A[0][2]*E[2][0]+A[1][2]*E[2][1]+A[2][2]*E[2][2]],\
      \
      [A[0][0]*E[3][0]+A[1][0]*E[3][1]+A[2][0]*E[3][2],
       A[0][1]*E[3][0]+A[1][1]*E[3][1]+A[2][1]*E[3][2],
       A[0][2]*E[3][0]+A[1][2]*E[3][1]+A[2][2]*E[3][2]]
print("şifre:",sifre)

print()

# #  4. soru:
# # benim numaramın son 2 hanesi 05 olduğu için kullanıcıdan sayı girmesini istedim.
b=[]
e = int(input("lütfen bir sayı giriniz : "))
for y in range( e + 1):
    if y > 1:
        for z in range(2, y):
            if (y % z) == 0:
                break
        else:
            b.append(y)
print(b)