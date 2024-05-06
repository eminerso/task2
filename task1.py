# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#  input:[-1,1,2,2,6,7,7,'say']

# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}

# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results=[ 2.5, 3.5, 4.5]

#/////////////////////////////////////////////////////////////
print("_"*50)
print("task 2")
#//////////////////////////////////////////////////////////////

mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

for x in mylist:
    if x>0:
        print(f"{(x**0.5)}--sqr--{x}")


#///////////////////////////////////////////////////
print("_"*50)
print("task 2")
#////////////////////////////////////////////////////

input=[-1,1,2,2,6,7,7,'say']

single=[]
for x in input:
    if x not in single:
        single.append(x)
print(single)

#/////////////////////////////////////////////////////
print("_"*50)
print("task 3")
#////////////////////////////////////////////////////////////////

inputt=4561238
listing=list(str(inputt))
start=1
col=[]
for x in listing:
    col.append(int(x))
for i in col:
    start*=i
print(start)

#////////////////////////////////////////////////////////////////////
print("_"*50)
print("task 4")
#////////////////////////////////////////////////////////////////////

inputtt=455
t=[]
for x in range(1,inputtt+1):
    if(inputtt/x)%1==0:
        t.append(x)
print(t)

#////////////////////////////////////////////////////
print("_"*50)
print("task 5")
#/////////////////////////////////////////////////////////////////
months=['january','february','march','april','may','june','july','august']
lenMonth=[]
v=list(map(lambda x:lenMonth.append(f"{x}"),months))
print(lenMonth)

#///////////////////////////////////////
print("_"*50)
print("task 6")
#////////////////////////////////////////////////
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

low=[]
for x in names:
    low.append(x.lower())
print(low)
#///////////////////////////////////////////////////////////////
print("_"*50)
print("task 7")
#//////////////////////////////////////////////

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum=[]
for i,x in enumerate(nums1):
    sum.append(nums2[i]+x)
print(sum)




