'''1)
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

 
try:
    i = -1
    while (i := a.index(15, i + 1)) >= 0:
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')
    
    
    
     
    
    '''2)
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
'''Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True

Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False'''






#3) copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()               # shallow copy of list 'a'
print(b)                     # [10, 20, 15, 18]
print(a  is  b)              # False → different objects
print(a  ==  b)             # True → contents are same
c = a[:]                    # slicing creates a shallow copy
print(c)                     # [10, 20, 15, 18]
print(a  is  c)              # False → different objects
print(a  ==  c)                # True → contents are same
d = a                           # assignment → no new object created
print(d)                         # [10, 20, 15, 18]
print(a  is  d)                  # True → both names refer to same object
print(a  ==  d)                  # True → contents obviously same


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Returns  a  new  list  with  same  elements

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''








'''4)
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
    ctr = 5
'''


'''Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15'''

# Step 1: unique elements
unique = set(a)
print("Unique elements:", unique)

# Step 2: check frequency of each unique element
max_count = 0
mode = None
for x in unique:
    count = a.count(x)
    print(f"Element {x} is repeated {count} times")
    if count > max_count:
        max_count = count
        mode = x

# Step 3: final result
print("Mode =", mode)
print("Count =", max_count)





# 5) Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)                    # prints the whole nested list
print(len(a))                # number of inner lists
print(How  to  print  1st  inner  list)             #print(a[0])           # 1st inner list → [10, 20, 30, 40]
print(How  to  print  2nd  inner  list)             #print(a[1])           # 2nd inner list → [50, 60, 70, 80]
print(How  to  print  3rd  inner  list)             #print(a[2])           # 3rd inner list → [90, 100, 110, 120]
print(How  to  print  30)                          # print(a[0][2])        # 30  → from 1st list, 3rd element
print(How  to  print  80)                          # print(a[1][3])        # 80  → from 2nd list, 4th element
print(How  to  print  100)                         # print(a[2][1])        # 100 → from 3rd list, 2nd element


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''





# 6) Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)                # print(a[0])   # 1st inner list → [10, 20]                
print(How  to  print  2nd   inner  list)                # print(a[1])   # 2nd inner list → [30, 40, 50]
print(How  to  print  3rd   inner  list)                # print(a[2])   # 3rd inner list → [60, 70, 80, 90]
print(How  to  print  number  of  elements  in  1st  inner  list)       # print(len(a[0]))   # length of 1st inner list = 2
print(How  to  print  number  of  elements  in  2nd  inner  list)       # print(len(a[1]))   # length of 2nd inner list = 3
print(How  to  print  number  of  elements  in  3rd  inner  list)       # print(len(a[2]))   # length of 3rd inner list = 4






# 7) How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)



'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''






# 8) Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
 
 # Output:
'''[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80'''






# 9) Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
 
 # Output:
 
'''[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90'''






#  10) Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
 
 # Output:
 
'''[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20
ValueError: too many values to unpack (expected 2)'''






# 11) Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)
print(How  to  print  inner  list  in  another  way
      
      
# Output:

''' a = [[]]

# Print inner list (Method 1: direct index)
print(a[0])      # inner list = []

# Print inner list (Method 2: loop)
for x in a:
    print(x) # prints [] again'''
    
    
    
    
    
    
# 12) Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0]]
print(sorted(a))   # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))   # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)    # [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0]]