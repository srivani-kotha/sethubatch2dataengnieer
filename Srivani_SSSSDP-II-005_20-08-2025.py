
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
n=[2,4,6,8,10]
x=[i**3 for i in n ]
print(x)

'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
x=['hyd' , 'pune' , 'chennai' , 'vijayawada']
y=[]
for i in x:
    y.append(i[0].upper())
print(y)
    
'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''
x=['hyd' , 'pune' , 'chennai' , 'vijayawada']
y=[i[0].upper() for i in x]

print(y)
    
'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
x="hyd  is  green  city"
y=[]
for i in x.split():
    y.append([i.upper(),len(i)])
print(y)

'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
x="hyd  is  green  city"
y=[[i.upper(),len(i)] for i in x.split()]
print(y)

'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
x= [10 , 20 , 30 , 40 , 50 , 60 , 70]
y=[100 , 200 , 300 , 400]
z=[]
n=min(len(x),len(y))
for i in range(n):
    z.append(x[i]+y[i])
print(z)

'''
Write  a  program  to  add  two  lists  of  unequal  length  with  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''
x= [10 , 20 , 30 , 40 , 50 , 60 , 70]
y=[100 , 200 , 300 , 400]
z=[x[i]+y[i] for i in range(min(len(x),len(y)))]
print(z)

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
x=3
y=4
z=[]
for i in range(x):
    z.append([0]*y)
print(z)

'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  with comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
x=3
y=4
z=[[0]*y for i in range(x) ]
print(z)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
x=[10 , 20 , 15 , 18 , 25 , 32]
y=[30 , 40 , 10 , 25 , 15]
z=[]
for i in x:
    if i not in y:
        z.append(i)
print(z)

'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   with comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
x=[10 , 20 , 15 , 18 , 25 , 32]
y=[30 , 40 , 10 , 25 , 15]
z=[ i for i in x if i not in y]
print(z)

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
z=[i for i in range(1,21) if i%2==0]
print(z)

#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension and  without  using  if
z=[i for i in range(1,21,)[1::2] ]
print(z)

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
z=[i*2 for i in range(1,21) if i*2 % 2==0 ]
print(z)

'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension without if
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
z=[i**2 for i in range(1,21)[]]
print(z)

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
x=[10 , 20 , 15]
y= [30 , 40 , 35 , 32]
z=[]
for i in x:
    for j in y:
        z.append(i+j)
print(z)

'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]

Hint : Nested  for  loops
'''
x=[10 , 20 , 15]
y= [30 , 40 , 35 , 32]
z=[i+j for i in x for j in y]
print(z)

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a='HYD'
b='PUNE'
z=[]
for i in list(a):
    for j in list(b):
        z.append(i+j)
print(z)

'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''
a='HYD'
b='PUNE'
z=[i+j for i in list(a) for j in list(b)]
print(z)
        
'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
x= [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
z=[]
for i in x:
    for j in i:
        z.append(j)
print(z)

'''
Write  a  program  to  convert  a  nested  list  to  list  with comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
x= [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
z=[j  for i in x for j in i]
print(z)
# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) #[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

'''
Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' ,  , 'Z' , 'K' ]

2) c = []

3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''
x=['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
y = {name[0] for name in x}
z=[]
for i in y:
    group = [name for name in x if name.startswith(i)]
    z.append(group)
print(z)
'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list


                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
a=[10  ,  20  , 30   ,  40   ,  50]
b=[5  ,  12  , 20   ,  37]
c=[]
a.sort()
b.sort()
i=0;j=0
while i < len(a) and j < len(b):
    if(a[i]==b[j]):
        c.append(a[i])
        c.append(b[j])
        i+=1
        j+=1
    elif(a[i]<b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
c.extend(a[i:])
c.extend(b[j:])
print(c)
        
        
'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
a= [10,20,30,25,40,35,12,5]
a.sort(reverse=True)
b=int(input("enter a which number largest"))
print(a[b-1])

'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
a=[10,20,30,25,40,35,12,5]
c=[]
while a:
    c.append((min(a)))
    a.remove(min(a))
print(c)