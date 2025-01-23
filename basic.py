#programming language
#Alphabets, words, numbers, special charcters, grammar rules

#Data Types in python launguage.....
#intigers  ---  int   Datatype
#float     ---  float Datatype
#string    ---  str   Datatype

#NUMERIC DATA TYPES
#int float complexnumbers booleans



#INTIGER Datatype
#Intigers are numbers are does not denoted  with decimal points...
#Ex : 2, 3 ,121 .... 
 
#FLOATS
#floats are numbers are denoted with decimal points
#Ex : 0.2 , 5.5 , 2.0 ....
 
#STRING
   # comination of groupn of characetrs is called string 
   # string is denoted with single qupotes '' or double quotes ""
   # ex-  a,b.c,d are four characters
   # str= "abcd" or 'abcd'
#string : one string  
#strings : muliple strings means 2 or more strings
#str

#COMPLEX NUMBERS
#in mathenatiucal terms we write it as a 1+1i
#here 1 - realpart...... i - imaginary part..
  
#in python code we write it as a 1+1j 
#here 1 - realpart...... j - imaginary part

#========================================================================================
  
#INTIGERS ADDITION , MULTIPICATION , DIVISION , QUOTIENT , REMINDER

num1 = 10
num2 = 10
print(num1+num2)  # addition of intigers 
output = 20
print(num1-num2)  # substraction of intiugers
output = 0
print(num1/num2)  # division of intigers
output = 1.0      # it given float
print(num1//num2) 
output =1        # it gives quotient
print(num1%num2)  # for finding reminder
output = 0
#========================================================================================

#STRING ADDITION , MULTIPICATION , DIVISON , 

str1="ji"
str2=' '
str3="balayya"
print(str1+str3) #addition of strings
output = 'jibalayya'
print(str1+str2+str3)
output = 'ji balayya' # beacuse str2 also have a character named as space 
print(str1*4) 
output = 'jijijiji' #it means ji is coming 4 types 
#print(str1*str3) 
# output = TypeError: cant multiply sequence by non-int of typr 'str'
#print(str1/str3)
# output = TypeError: unsupported operated type(s) for /: 'str' and 'str'
#========================================================================================

#LENGTH OF STRING  

# How to find length of string 
#length of string is nothing but total how many  charceters are there in string 
#let us take 2 strings named as string1 and string2 
str1="10kcoders"
str2="10k coders"
print(len(str1))
output = 9
print(len(str2))
output = 10     # here space bw 29r and batch is also a traeted as one character 
#=======================================================================================

#INDEX OF STRINGS
#Index is nothinf but length of string-1
#for ex length of string is 6 then index will be length-1 6-1=5
#example 
#let us take one string 
str1='stuedentnumber1'
print(len(str1))
output =15
#then index will be 14 becauuse 15-1=14
#that means index start from 0 and ends with 14
print(str1[0])
output = 's' #.....it means position of s character is 1st place ...index of  character s is 0
print(str1[14])
output= 1   #.....it means position of charector 1 is 15th place ...index of charcter 1 is 14
#print(str1[15])
#output = IndexError because length 15 ..this 15 is the position of last character of string means position of charcter 1
#so if u wont the index of that number you must enter the 14 instead of 15 beacause index is 15-1=14..like shown above 
#==========================================================================================

#SLICING OF STRINGS
# slicing is nithing but [from : end]
#Let us assume one string str1="sari gama pada nisa"
str1= "sari gama pada nisa"
print(str1[0])
output = 's'
print(str1[1])
output = 'a'
print(str1[0:1])
output = 's'
print(str1[18])
output = 'a'
print(str1[1:18]) # actually in 18th index a is there ... at 0th index s is there  
                  # but when u applying slicing to 1:18 ....output is start with... after the first immidiate character of 0th index... that merans 'a'
                  # """""""""""""""""""""""""""""" 1:18.....output is ends with.... before the first immidiate charcter of 18th index...that means 's'
                  # simply it means it neglect the both characters of 0th index and 18th index reaming will come in output   
output = 'ari gama pada nis'
print(str1[0:500])
output = 'sari gama pada nisa' #this is accetable beacuse we can give uppar bound greater than the lower bound
print(str1[1000:1])
output = '' #(empty string) this is also acceptable
print(str1[100:1:-1])
output = 'asin adap amag ir' # it will print  from first negative index means a to 2nd positive index r... except 0th positive index and 1st positive indexs of str1
print(str1[50:1:-2])
output = 'ai dpaa r' # it will print from first negastive index means 'a' to 3rd positive index means i ..we must ignore 0th ist and 2nd indexes of str1 
         # first neagative index of number a skip one step from right side of string means s will skipped after s ..i  is there it will come in second less like that ..
         #we can this upto 3rd index of number means  i after i... there ..r is there so r will come at last 
         # note no need of skip after the 2nd index of number of str1 
         # we must skip from right side means from nrgative index of string
print(str1[50:1:-3])
output = 'and ai' # it will print from first negastive index means 'a' to 4th positive index means m ..we must ignore 0th ist and 2nd indexes and also 3rd index  of str1 
         # first neagative index of number is a skip two step from right side of string means i will skipped after i ..n is there it will come in second less like that ..
         # we can this upto 4th index of number means g after g ..i is there so i will come at last 
         # no need to of skip after 3rd index of number
         # we must skip from right side means from negative index of string 
str2='this is a string'
print(len(str2))
print(str2[:])
output = 'this is a string' # whole string will come 
print(str2[-5:-1])
output = 'trin'
print(str2[-1:-5])
output = '' # empty string
print(str2[-1:-5:-1])
output = 'gnir'
print(str2[-1:-5:-2])
output = 'gi'
print(str2[-2:-5:-1])
output = 'nir'
print(str2[-5:-16:-2])
output = 'i  sh'

#===================================================================================================

#COMPLEX NUMBERS
#Complex number format 2+3j  here ---2 (is real part),3 (imaginary part) 
#examples
# let us assume img1 = 2+3j img2 = 3+4j

img1=2+3j
img2=3+4j
print(img1+img2)
output = (5+7j)
print(img1-img2)
output = (-1-1j)
print(img1*img2)
output = (-6+17j)
print(img1/img2)
output = (0.72+0.04j)

#==========================================================================================

#BOOLEAN 
#Means True or False 
#b       1  0r   0
# Example 
jamesbond_pin=7224
bruselee_pin=7224
print(jamesbond_pin == bruselee_pin)
output = 'true'

sachin_centuries=100
viratkohli_centuries=81
print(sachin_centuries == viratkohli_centuries)
output = 'false'

#===========================================================================================

#sequences ----- string, list, tuple, range

#LIST 
# List allows homogenious and hetrogenious are allowed
#list is mutable in python
#mutable we can change the existing value by giving new value ..
# Examples
 
List1=[1,10,True,False,'string1',2.0]
print(type(List1))
#output = <class 'List1'
print(List1[5])
output = 2.0
List1.append(100)
print(len(List1))
output =7
print(List1[5])
output = 100
print('for loop')
for i in List1:
   print(i)
#output = 1
#         10
#         True
#         False
#         string1
#         2.0
#         100

#========================================================================================

#LIST IN LIST
#Examples
#list is denoted with [] square brackets
List1= [1,2,6,7,True,[1,5],"apple"]
print(List1[5])
output = [1,5]
print(List1[5][1])
output = 5
print(List1[5][-2])
output = 1
print(List1[6])
output = 'apple'
print(List1[6][-5])
output = 'a'

List2=[[1,2,3],[4,5,6],[7,8,9]]
print(len(List2))
output = 2
print(List2[2][-2])
output = 8

#============================================================================================

#TUPLE
#tuple elements are written with in paranthesis
#tuple is immutable (we cant add value to existing mute)
# Examples
tup1=(1,2,6,7,True,[1,"ponting","symonds"])
print(tup1[-3])
output =7

#==============================================================================================

#RANGE
# Examples
r1=range(0,15)
print(r1)
output = range(0,15)
print(list(r1))
#output = [0,1,2,.............................,14]

#======================================================================================================

#SET
#collection of finite, unique, un ordered elements
# duplicagtes are not allowed
#elements are un ordered
# Examples
# denoted flower brackets
set1={2,3,2.0,True,"string1", "string1", 2+3j}
print(set1)
output = {True,2,3,'string1',2+3j}
#if we print again this order will change 
print(set1)
print(set1)
print(set1)
print(set1)
output= {True,2,3,2+3j,'string1'}

#==================================================================================================

#DICTIONARY
#KEY VALUE PAIRS
#KEY ----UNIQUE
#VALUE----MULTIPLE
#WE CAN ACCESS VALUE BY USING KEY
#WE CAN NOT ACCESS KEY BY USING VALUE 
# Example
#denoted with flower brackets
# key:value

d1={1:'sirivennela', 2:'ilayaraja', 3:'maisharma', 4:'devisriprasad', 5:'sp bala subramanyam'}
print(d1)
output = {1:'sirivennela', 2:'ilayaraja', 3:'manisharma', 4:'devisriprasad', 5:'sp bala subramanyam'}
d1[2]='bhabubali'
print(d1)
output = {1:'sirivennela', 2:'bhabubali', 3:'manisharma', 4:'devisriprasad', 5:'sp bala subramanyam'}

#==================================================================================================

#NONE
#none means null
# Example

num1=None
print(num1)
output = None

#=====================================================================================================

#ID .....Identification or Identity
# Example
num1=25
num2=25
print(id(num1))
output = 140730541868712
print(id(num2))
output = 140730541868712
name='avinash'
name2='avinash'
name3='avinash'
name4='avinash'
print(id(name))
print(id(name2))
print(id(name3))
print(id(name4))
print(id(num1))
#output = for all names id is same 
# if you run this again id is same for all numbers but id will change
         










  


